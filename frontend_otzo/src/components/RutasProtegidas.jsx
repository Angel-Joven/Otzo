/*

Proteccion de rutas para evitar que el usuario se salte el login
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import React from 'react';
import { Navigate } from 'react-router-dom'; // Usa Navigate para redirigir
import { UsarAutenticadorNombre } from '../context/Autenticacion';

export function RutaProtegida({ children }) {
  const { userType } = UsarAutenticadorNombre(); // Verifica si hay un tipo de usuario autenticado

  if (!userType) {
    // Si no hay usuario autenticado, redirige a la página principal usando Navigate
    return <Navigate to="/" />;
  }

  // Si hay un usuario autenticado, renderiza el contenido de la ruta
  return children;
}
