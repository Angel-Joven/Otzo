/*

Pagina Principal para el Modulo de Administracion
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import React, { useState, useEffect } from "react";
import axios from "axios";
import { motion } from "framer-motion";

export function Administracion() {
  const [admin, setAdmin] = useState(null);
  const [error, setError] = useState("");

  //Esto sirve para obtener los datos del administrador activo
  const fetchAdmin = async () => {
    try {
      const adminData = JSON.parse(localStorage.getItem("administrador"));
      setAdmin(adminData);
    } catch (err) {
      setError("No se pudo cargar la informacion del administrador");
    }
  };

  useEffect(() => {
    fetchAdmin();
  }, []);

  return (
    <div className="bg-gradient-to-r from-red-400 to-red-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative">
      <div>
        <motion.h1
          initial={{ scale: 0 }}
          animate={{ scale: 1, transition: { delay: 0.5 } }}
          className="text-center text-white text-6xl font-bold"
        >
          Administracion
        </motion.h1>
        {error && <p className="text-center text-red-500">{error}</p>}
        {admin ? (
          <div className="text-white p-4">
            <h2 className="text-2xl font-bold mb-4">
              Administrador Activo: {admin.nombre}
            </h2>
            <table className="table-auto border-collapse border border-white w-full text-left">
              <thead>
                <tr>
                  <th className="border border-white px-4 py-2">ID</th>
                  <th className="border border-white px-4 py-2">Nombre</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="border border-white px-4 py-2">
                    {admin.id_empleado}
                  </td>
                  <td className="border border-white px-4 py-2">{admin.nombre}</td>
                  <td className="border border-white px-4 py-2">
                    {admin.contacto_correo}
                  </td>
                  <td className="border border-white px-4 py-2">
                    {admin.contacto_telefono}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        ) : (
          <p className="text-center text-white">Cargando datos...</p>
        )}
        <div className="flex justify-center mt-4 space-x-4">
          <button
            className="bg-blue-500 text-white px-4 py-2 rounded"
          >
            Crear Administrador
          </button>
          <button
            className="bg-red-500 text-white px-4 py-2 rounded"
          >
            Dar de baja a un Administrador
          </button>
          <button
            className="bg-yellow-500 text-white px-4 py-2 rounded"
          >
            Modificar Administrador
          </button>
        </div>
      </div>
    </div>
  );
}
