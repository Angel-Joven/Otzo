/*

Login para el Modulo de Clientes
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { UsarAutenticadorNombre } from '../context/Autenticacion';
import { motion } from 'framer-motion';

export function LoginClientes() {
  //Le asignamos un rango a todos los clientes que se hayan registrado de manera automatizada
  const asignarRangoInicial = async () => {
    try {
      const response = await axios.get("http://localhost:5000/api/fidelizacion/asigrnginiauto");
      console.log("Rango inicial asignado automaticamente:", response.data.mensaje);
    } catch (error) {
      console.error("Error al asignar rango inicial automatico:", error.response?.data || error.message);
    }
  };

  const [nombre, setNombre] = useState('');
  const [contraseña, setContraseña] = useState('');
  const [error, setError] = useState('');
  const [mostrarModal, setMostrarModal] = useState(false);
  const [mostrarReset, setMostrarReset] = useState(false);
  const [resetData, setResetData] = useState({
    nombre: '',
    apellido_paterno: '',
    apellido_materno: '',
    nueva_contraseña: '',
  });
  const [nuevaCuenta, setNuevaCuenta] = useState({
    nombre: '',
    apellido_paterno: '',
    apellido_materno: '',
    contacto_correo: '',
    contraseña: '',
  });
  const navigate = useNavigate();
  const { userType, setUserType } = UsarAutenticadorNombre();

  useEffect(() => {
    if (userType === 'cliente') {
      navigate('/indexClientes');
    } else {
      setUserType(null);
    }
  }, [userType, navigate, setUserType]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/api/clientes/login', { nombre, contraseña });
      if (response.status === 200) {
        asignarRangoInicial(); // Asignamos el rango default
        setUserType('cliente');
        localStorage.setItem('administrador', JSON.stringify(response.data));
        localStorage.setItem('cliente', JSON.stringify(response.data));
        navigate('/indexClientes');
      }
    } catch (err) {
      setError(err.response?.data?.error || 'Error al iniciar sesion');
    }
  };

  const manejarCambioEntrada = (e) => {
    const { name, value } = e.target;
    setNuevaCuenta({ ...nuevaCuenta, [name]: value });
  };

  const manejarCrearCuenta = async () => {
    const { nombre, apellido_paterno, apellido_materno, contacto_correo, contraseña } = nuevaCuenta;

    if (!nombre) {
      alert("Por favor ingresa tu nombre");
      return;
    }

    if (!apellido_paterno) {
      alert("Por favor ingresa tu apellido paterno");
      return;
    }

    if (!apellido_materno) {
      alert("Por favor ingresa tu apellido materno");
      return;
    }

    if (!contacto_correo) {
      alert("Ingrese un correo electronico");
      return "Ingrese un correo electronico";
    }

    if (contacto_correo && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(contacto_correo)) {
      alert("Ingrese un correo electronico valido.");
      return "Ingrese un correo electronico valido.";
    }

    if (!contraseña) {
      alert("Ingrese una contraseña");
      return "Ingrese una contraseña";
    }

    if (contraseña && (contraseña.length > 255 || contraseña.length < 6)) {
      alert("La contraseña debe tener entre 6 y 255 caracteres.");
      return "La contraseña debe tener entre 6 y 255 caracteres.";
    }

    try {
      const response = await axios.post('http://localhost:5000/api/clientes/verificarcliente', nuevaCuenta);
      if (response.data.existe) {
        alert('Esta cuenta ya existe. Por favor, inicie sesion con esta cuenta.');
        return;
      }

      await axios.post('http://localhost:5000/api/clientes/crearclientelogin', nuevaCuenta);
      alert('Cuenta creada con éxito. Por favor, inicie sesion.');
      setNuevaCuenta({
        nombre: '',
        apellido_paterno: '',
        apellido_materno: '',
        contacto_correo: '',
        contraseña: '',
      });
      setMostrarModal(false);
    } catch (error) {
      console.error('Error al crear la cuenta:', error);
      alert(error.response?.data?.error || 'Error al crear la cuenta.');
    }
  };

  const manejarResetearContraseña = async () => {
    const { nombre, apellido_paterno, apellido_materno, nueva_contraseña } = resetData;

    if (!nombre) {
      alert("Por favor ingresa tu nombre");
      return;
    }

    if (!apellido_paterno) {
      alert("Por favor ingresa tu apellido paterno");
      return;
    }

    if (!apellido_materno) {
      alert("Por favor ingresa tu apellido materno");
      return;
    }

    if (!nueva_contraseña) {
      alert("Ingrese una nueva contraseña");
      return "Ingrese una nueva contraseña";
    }

    if (nueva_contraseña && (nueva_contraseña.length > 255 || nueva_contraseña.length < 6)) {
      alert("La nueva contraseña debe tener entre 6 y 255 caracteres.");
      return "La nueva contraseña debe tener entre 6 y 255 caracteres.";
    }

    try {
      const response = await axios.post('http://localhost:5000/api/clientes/resetearcontraseña', resetData);
      alert(response.data.mensaje || 'Contraseña actualizada con wxito. Por favor, inicie sesion.');
      setResetData({
        nombre: '',
        apellido_paterno: '',
        apellido_materno: '',
        nueva_contraseña: '',
      });
      setMostrarReset(false);
    } catch (error) {
      console.error('Error al resetear la contraseña:', error);
      alert(error.response?.data?.error || 'Error al resetear la contraseña.');
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1, transition: { duration: 0.5 } }}
      className="flex items-center justify-center min-h-screen bg-gradient-to-r from-yellow-400 to-yellow-500 p-6"
    >
      <div className="bg-white rounded-lg shadow-xl p-8 w-full max-w-md">
        <motion.h1
          initial={{ y: -50, opacity: 0 }}
          animate={{ y: 0, opacity: 1, transition: { delay: 0.3 } }}
          className="text-2xl font-bold text-gray-900 text-center mb-4"
        >
          Iniciar Sesion - Clientes
        </motion.h1>
        {error && (
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1, transition: { delay: 0.2 } }}
            className="text-red-600 text-center mb-4"
          >
            {error}
          </motion.p>
        )}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1, transition: { delay: 0.2 } }}
          className="text-center text-blue-500 font-semibold cursor-pointer mb-4"
          onClick={() => setMostrarReset(true)}
        >
          ¿Olvido su contraseña?
        </motion.p>
        <form onSubmit={handleSubmit} className="space-y-4">
          <label>Nombre</label>
          <motion.input
            initial={{ x: -50, opacity: 0 }}
            animate={{ x: 0, opacity: 1, transition: { delay: 0.4 } }}
            type="text"
            placeholder="Nombre de usuario"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-500"
          />
          <label>Contraseña</label>
          <motion.input
            initial={{ x: 50, opacity: 0 }}
            animate={{ x: 0, opacity: 1, transition: { delay: 0.5 } }}
            type="password"
            placeholder="Contraseña"
            value={contraseña}
            onChange={(e) => setContraseña(e.target.value)}
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-500"
          />
          <motion.button
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1, transition: { delay: 0.6 } }}
            type="submit"
            className="w-full py-2 bg-yellow-500 text-white font-semibold rounded-lg hover:bg-yellow-600 transition"
          >
            Ingresar
          </motion.button>
        </form>
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1, transition: { delay: 0.7 } }}
          className="text-center mt-4"
        >
          ¿Es nuevo y no tiene cuenta?{' '}
          <span
            className="text-yellow-600 font-bold cursor-pointer hover:underline"
            onClick={() => setMostrarModal(true)}
          >
            ¡De clic aqui para crear una nueva cuenta!
          </span>
        </motion.p>
      </div>

      {mostrarModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-lg shadow-lg p-4 w-full max-w-md md:max-w-lg">
            <h2 className="text-2xl font-bold mb-4 text-center">Crear Cuenta</h2>
            <div className="grid gap-4">
              <label>Nombre(s)</label>
              <input
                type="text"
                name="nombre"
                value={nuevaCuenta.nombre}
                onChange={manejarCambioEntrada}
                placeholder="Nombre"
                className="p-2 border rounded"
              />
              <label>Apellido Paterno</label>
              <input
                type="text"
                name="apellido_paterno"
                value={nuevaCuenta.apellido_paterno}
                onChange={manejarCambioEntrada}
                placeholder="Apellido Paterno"
                className="p-2 border rounded"
              />
              <label>Apellido Materno</label>
              <input
                type="text"
                name="apellido_materno"
                value={nuevaCuenta.apellido_materno}
                onChange={manejarCambioEntrada}
                placeholder="Apellido Materno"
                className="p-2 border rounded"
              />
              <label>Correo Electronico</label>
              <input
                type="email"
                name="contacto_correo"
                value={nuevaCuenta.contacto_correo}
                onChange={manejarCambioEntrada}
                placeholder="Correo Electronico"
                className="p-2 border rounded"
              />
              <label>Contraseña</label>
              <input
                type="password"
                name="contraseña"
                value={nuevaCuenta.contraseña}
                onChange={manejarCambioEntrada}
                placeholder="Contraseña"
                className="p-2 border rounded"
              />
              <button
                onClick={manejarCrearCuenta}
                className="bg-green-500 text-white py-2 rounded hover:bg-green-600"
              >
                Crear Cuenta
              </button>
              <button
                onClick={() => setMostrarModal(false)}
                className="bg-gray-500 text-white py-2 rounded hover:bg-gray-600"
              >
                Cancelar
              </button>
            </div>
          </div>
        </div>
      )}

      {mostrarReset && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-lg shadow-lg p-4 w-full max-w-md md:max-w-lg">
            <h2 className="text-2xl font-bold mb-4 text-center">Resetear Contraseña</h2>
            <div className="grid gap-4">
              <label>Nombre(s)</label>
              <input
                type="text"
                name="nombre"
                value={resetData.nombre}
                onChange={(e) => setResetData({ ...resetData, [e.target.name]: e.target.value })}
                placeholder="Nombre"
                className="p-2 border rounded"
              />
              <label>Apellido Paterno</label>
              <input
                type="text"
                name="apellido_paterno"
                value={resetData.apellido_paterno}
                onChange={(e) => setResetData({ ...resetData, [e.target.name]: e.target.value })}
                placeholder="Apellido Paterno"
                className="p-2 border rounded"
              />
              <label>Apellido Materno</label>
              <input
                type="text"
                name="apellido_materno"
                value={resetData.apellido_materno}
                onChange={(e) => setResetData({ ...resetData, [e.target.name]: e.target.value })}
                placeholder="Apellido Materno"
                className="p-2 border rounded"
              />
              <label>Nueva Contraseña</label>
              <input
                type="password"
                name="nueva_contraseña"
                value={resetData.nueva_contraseña}
                onChange={(e) => setResetData({ ...resetData, [e.target.name]: e.target.value })}
                placeholder="Nueva Contraseña"
                className="p-2 border rounded"
              />
              <button
                onClick={manejarResetearContraseña}
                className="bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
              >
                Resetear Contraseña
              </button>
              <button
                onClick={() => setMostrarReset(false)}
                className="bg-gray-500 text-white py-2 rounded hover:bg-gray-600"
              >
                Cancelar
              </button>
            </div>
          </div>
        </div>
      )}
    </motion.div>
  );
}

