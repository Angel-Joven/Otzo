/*

Proteccion de rutas para evitar que el usuario se salte el login
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import { Navigate } from 'react-router-dom';
import { UsarAutenticadorNombre } from '../context/Autenticacion';

export function RutaProtegida({ children, allowedUserTypes }) {
  const { userType } = UsarAutenticadorNombre();

  if (!userType) {
    return <Navigate to="/" />;
  }

  if (allowedUserTypes && !allowedUserTypes.includes(userType)) {
    return <Navigate to="/" />;
  }

  return children;
}
