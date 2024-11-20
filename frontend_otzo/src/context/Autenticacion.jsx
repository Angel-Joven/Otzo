/*

Contexto de Auntenticacion para el Login de Clientes y Administradores
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import { createContext, useContext, useState, useEffect } from 'react';

const AutenticadorNombre = createContext();

export function ObtenerAutenticadorNombre({ children }) {
  const [userType, setUserType] = useState(null);

  useEffect(() => {
    //Guardamos el tipo de usuario en localStorage despues de logearse
    if (userType) {
      localStorage.setItem('userType', userType);
    }
  }, [userType]);

  return (
    <AutenticadorNombre.Provider value={{ userType, setUserType }}>
      {children}
    </AutenticadorNombre.Provider>
  );
}

export function UsarAutenticadorNombre() {
  return useContext(AutenticadorNombre);
}
