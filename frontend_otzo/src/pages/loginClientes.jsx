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
  const [nombre, setNombre] = useState('');
  const [contraseña, setContraseña] = useState('');
  const [error, setError] = useState('');
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
        //Guardamos la informacion del cliente en el estado o en el 'localStorage' y le asignamos el tipo de usuario
        setUserType('cliente');
        localStorage.setItem('administrador', JSON.stringify(response.data));
        localStorage.setItem('cliente', JSON.stringify(response.data));
        //Lo mandamos a la ruta de clientes
        navigate('/indexClientes');
      }
    } catch (err) {
      setError(err.response?.data?.error || 'Error al iniciar sesion');
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
        <form onSubmit={handleSubmit} className="space-y-4">
          <motion.input
            initial={{ x: -50, opacity: 0 }}
            animate={{ x: 0, opacity: 1, transition: { delay: 0.4 } }}
            type="text"
            placeholder="Nombre de usuario"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-500"
          />
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
      </div>
    </motion.div>
  );
}
