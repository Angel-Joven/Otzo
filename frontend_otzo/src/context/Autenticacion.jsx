/*

Contexto de Auntenticacion para el Login de Clientes y Administradores
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import { createContext, useContext, useState, useEffect } from 'react';

const AutenticadorNombre = createContext();

export function ObtenerAutenticadorNombre({ children }) {
  const [userType, setUserType] = useState(() => localStorage.getItem('userType') || null);

  useEffect(() => {
    if (userType) {
      localStorage.setItem('userType', userType);
    } else {
      localStorage.removeItem('userType');
    }
  }, [userType]);

  const logout = () => {
    setUserType(null);
    localStorage.removeItem('userType');
  };

  return (
    <AutenticadorNombre.Provider value={{ userType, setUserType, logout }}>
      {children}
    </AutenticadorNombre.Provider>
  );
}

export function UsarAutenticadorNombre() {
  return useContext(AutenticadorNombre);
}
