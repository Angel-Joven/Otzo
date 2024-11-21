/*

Pagina Principal para saber quien se va a logear y en base a eso, darle acceso.
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { UsarAutenticadorNombre } from '../context/Autenticacion';

export function IndexPrincipal() {
  const navigate = useNavigate();
  const { userType, setUserType } = UsarAutenticadorNombre();

  useEffect(() => {
    if (userType) {
      if (userType === 'cliente') {
        navigate('/indexClientes');
      } else if (userType === 'administrador') {
        navigate('/indexAdministradores');
      }
    } else {
      setUserType(null);
    }
  }, [userType, navigate, setUserType]);

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-l from-red-400 to-orange-500 w-full z-0 relative">
      <h1 className="text-white text-6xl font-bold mb-8 ">Bienvenido a Otzo</h1>
      <div className="flex flex-col md:flex-row gap-8">
        
        <button
          onClick={() => navigate('/loginClientes')}
          className="bg-yellow-400 hover:bg-yellow-500 text-white font-bold py-4 px-6 rounded-lg flex items-center justify-center shadow-lg transition-transform transform hover:scale-105"
        >
          <img src="clientes.png" alt="Cliente" className="w-8 h-8 mr-2" />
          Acceder Clientes
        </button>
        
        <button
          onClick={() => navigate('/loginAdministradores')}
          className="bg-red-500 hover:bg-red-600 text-white font-bold py-4 px-6 rounded-lg flex items-center justify-center shadow-lg transition-transform transform hover:scale-105"
        >
          <img src="administracion.png" alt="Administrador" className="w-8 h-8 mr-2" />
          Acceder Administradores
        </button>
      </div>
    </div>
  );
}
