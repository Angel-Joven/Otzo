/*

Login para el Modulo de Administracion
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { UsarAutenticadorNombre } from '../context/Autenticacion';
import { motion } from 'framer-motion';

export function LoginAdministradores() {
  const [nombre, setNombre] = useState('');
  const [contraseña, setContraseña] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { userType, setUserType } = UsarAutenticadorNombre();
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    if (userType === 'administrador') {
      navigate('/indexAdministradores');
    } else {
      setUserType(null);
    }
  }, [userType, navigate, setUserType]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/api/administracion/login', { nombre, contraseña });
      if (response.status === 200) {
        setUserType('administrador');
        localStorage.setItem('administrador', JSON.stringify(response.data));
        localStorage.setItem('cliente', JSON.stringify(response.data.cliente));
        navigate('/indexAdministradores');
      }
    } catch (err) {
      setError(err.response?.data?.error || 'Error al iniciar sesión');
    }
  };

  return (
    <>
      <motion.div 
        initial={{ opacity: 0 }} 
        animate={{ opacity: 1, transition: { duration: 0.5 } }} 
        className="flex items-center justify-center min-h-screen bg-gradient-to-r from-red-400 to-red-500 p-6"
      >
        <div className="bg-white rounded-lg shadow-xl p-8 w-full max-w-md">
          <motion.h1 
            initial={{ y: -50, opacity: 0 }} 
            animate={{ y: 0, opacity: 1, transition: { delay: 0.3 } }}
            className="text-2xl font-bold text-gray-900 text-center mb-4"
          >
            Iniciar Sesion - Administradores
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
              className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500"
            />
            <motion.input
              initial={{ x: 50, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.5 } }}
              type="password"
              placeholder="Contraseña"
              value={contraseña}
              onChange={(e) => setContraseña(e.target.value)}
              className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500"
            />
            <motion.button
              initial={{ scale: 0.9, opacity: 0 }}
              animate={{ scale: 1, opacity: 1, transition: { delay: 0.6 } }}
              type="submit"
              className="w-full py-2 bg-orange-500 text-white font-semibold rounded-lg hover:bg-orange-600 transition"
            >
              Ingresar
            </motion.button>
          </form>
          {/* Texto */}
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1, transition: { delay: 0.7 } }}
            className="text-center mt-4"
          >
            <button
              onClick={() => setShowModal(true)}
              className="text-blue-500 hover:underline focus:outline-none"
            >
              ¿Olvidaste algun dato o no tienes cuenta?
            </button>
          </motion.p>
        </div>
      </motion.div>
      {/* Modal */}
      {showModal && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="bg-white rounded-lg shadow-xl p-6 w-full max-w-md"
          >
            <h2 className="text-xl font-bold mb-4 text-center">
            ¿Olvidaste algun dato o no tienes cuenta?
            </h2>
            <p className="text-gray-700 mb-6">
              Contacta al DBA para el reseteo de contraseña o nombre de usuario o para la generacion de su cuenta para poder acceder al panel de administracion.
            </p>
            <div className="flex justify-center">
              <button
                onClick={() => setShowModal(false)}
                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
              >
                Cerrar
              </button>
            </div>
          </motion.div>
        </div>
      )}
    </>
  );
}
