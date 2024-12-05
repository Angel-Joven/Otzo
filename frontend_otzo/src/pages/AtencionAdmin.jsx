import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import DataTable from "react-data-table-component";
import { Toaster, toast } from "react-hot-toast";

import {
  crearQueja,
  obtenerQuejasCliente,
  obtenerQuejasPendientes,
} from "../api/atencionData.api";
import { ObtenerTipoUsuario } from "../context/obtenerUsuarioTipo";

export function AtencionAdmin() {
  const { idEmpleado } = ObtenerTipoUsuario();
  const [quejas, setQuejas] = useState([]);
  const [recargarQuejas, setRecargarQuejas] = useState(false);
  const [quejaAEditar, setQuejaAEditar] = useState();

  useEffect(() => {
    obtenerQuejasPendientes().then((res) => {
      setQuejas(res.data);
    });
  }, []);

  const columnasQuejas = [
    {
      name: "ID queja",
      selector: (row) => row.idQueja,
    },
    {
      name: "ID empleado",
      selector: (row) => row.id_empleado,
    },
    {
      name: "Fecha y hora",
      selector: (row) => row.fechaHora,
    },
    {
      name: "Descripción",
      selector: (row) => row.descripcion,
    },
    {
      name: "Categoria",
      selector: (row) => row.categoria,
    },
    {
      name: "Estado",
      selector: (row) => row.estado,
    },
    {
      name: "Respuesta",
      selector: (row) => row.comentarioSeguimiento,
    },
    {
      name: "Acción",
      cell: (row) => (
        <motion.button
          whileHover={{ scale: 1.1 }}
          onClick={() => {
            setAbrirModalQueja(true);
            setQuejaAEditar(row.idQueja);
            // TODO: Llenar los campos del formulario con los datos de la queja
          }}
          className="bg-blue-500 text-white p-2"
        >
          Responder {row.idQueja}, {idEmpleado}
        </motion.button>
      ),
    },
  ];

  //MODALES

  const [abrirModalQueja, setAbrirModalQueja] = useState(false);
  const cerrarModalQueja = (e) => {
    if (e.target.id === "modalResponderQueja") {
      setAbrirModalQueja(false);
    }
  };
  const manejarResponderQueja = async (e) => {
    e.preventDefault();

    /* const queja = {
      id_cliente: idCliente,
      id_empleado: 0,
      rango_usuario: 0,
      descripcion: e.target.add_queja_descripcion.value,
      categoria: e.target.add_queja_categoria.value,
      estado: "Pendiente",
      prioridad: 1,
      comentario_seguimiento: "",
    };

    toast
      .promise(crearQueja(queja), {
        loading: "Cargando...", // Mensaje mientras la promesa está pendiente
        success: "¡Operación exitosa!", // Mensaje cuando la promesa se resuelve con éxito
        error: "Error al realizar la operación", // Mensaje cuando la promesa es rechazada
      })
      .finally(() => {
        setRecargarQuejas(!recargarQuejas);
        setAbrirModalQueja(false);
      }); */
  };

  return (
    <>
      <Toaster position="top-center" />
      <div className="bg-gradient-to-r from-blue-400 to-blue-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative">
        {abrirModalQueja && (
          <dialog
            id="modalResponderQueja"
            className="absolute top-0 right-0 left-0 bottom-0 z-10 w-full h-full bg-slate-900/80 flex justify-center items-center"
            onMouseDown={cerrarModalQueja}
          >
            <div
              className="min-h-[50%] min-w-[50%] bg-white rounded-xl p-4 flex flex-col gap-4"
              onClick={(e) => e.stopPropagation()} // Evita cerrar al hacer clic dentro del recuadro
            >
              <p className="font-bold text-xl">Agrega un producto:</p>
              <form onSubmit={manejarResponderQueja}>
                <label htmlFor="add_queja_descripcion" className="block">
                  Describa su queja:
                </label>
                <textarea
                  id="add_queja_descripcion"
                  type="text"
                  placeholder="Escribe aquí..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400 resize-none"
                  required
                  minLength={2}
                  maxLength={512}
                >
                  {quejaAEditar}
                </textarea>
                <label htmlFor="add_queja_categoria" className="block">
                  Categoria de la queja:
                </label>
                <select
                  name="add_queja_categoria"
                  id="category"
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                  required
                >
                  <option value="" disabled selected>
                    Selecciona una categoría
                  </option>
                  <option value="Servicio al cliente">
                    Servicio al cliente
                  </option>
                  <option value="Instalaciones">Instalaciones</option>
                  <option value="Productos">Productos</option>
                  <option value="Otros">Otros</option>
                  <option value="Servicio al cliente">
                    Servicio al cliente
                  </option>
                  <option value="Cobros indebidos">Cobros indebidos</option>
                </select>
                <input
                  type="submit"
                  value="Crear producto"
                  className="block bg-blue-500 rounded-lg p-2 text-white font-bold my-2 cursor-pointer"
                />
              </form>
            </div>
          </dialog>
        )}

        <div>
          <motion.h1
            initial={{ scale: 0 }}
            animate={{ scale: 1, transition: { delay: 0.5 } }}
            className="text-center text-white text-6xl font-bold"
          >
            Atención al Cliente
          </motion.h1>
        </div>
        <div className="grid grid-cols-1 grid-rows-1 gap-x-2.5 md:grid-cols-1">
          <div className="w-full h-full p-4">
            <motion.div
              initial={{ x: 200, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="w-full h-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900 flex justify-between items-center">
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-document"></i> Quejas
                </h2>
                <button
                  className="text-white bg-blue-500 rounded-xl p-2"
                  onClick={() => setAbrirModalQueja(true)}
                >
                  + Agregar queja
                </button>
              </div>
              <div className="overflow-x-auto">
                <DataTable columns={columnasQuejas} data={quejas} />
              </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)]"></div>
            </motion.div>
          </div>

          <div className="w-full h-full p-4">
            <motion.div
              initial={{ x: 200, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="w-full h-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900">
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-document"></i> Sugerencias
                </h2>
              </div>
              <div className="overflow-x-auto">
                <table className="min-w-full bg-white">
                  <thead>
                    <tr>
                      <th className="py-2 px-4 border-b text-center">
                        ID Sugerencia
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        ID Cliente
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        ID Empleado
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Descripción
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Categoría
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Estado de la Sugerencia
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Seguimiento
                      </th>
                    </tr>
                  </thead>
                  <tbody></tbody>
                </table>
              </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)]"></div>
            </motion.div>
          </div>
        </div>
      </div>
    </>
  );
}
