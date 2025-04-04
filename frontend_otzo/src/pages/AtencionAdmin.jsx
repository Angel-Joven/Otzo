import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import DataTable from "react-data-table-component";
import { Toaster, toast } from "react-hot-toast";

import {
  obtenerQuejasPendientes,
  responderQueja,
  responderSugerencia,
  obtenerSugerenciasPendientes
} from "../api/atencionData.api";
import { ObtenerTipoUsuario } from "../context/obtenerUsuarioTipo";

export function AtencionAdmin() {
  const { idEmpleado } = ObtenerTipoUsuario();
  const [quejas, setQuejas] = useState([]);
  const [sugerencias, setSugerencias] = useState([]);
  const [recargarQuejas, setRecargarQuejas] = useState(false);
  const [recargarSugerencias, setRecargarSugerencias] = useState(false);
  const [quejaAEditar, setQuejaAEditar] = useState({});
  const [sugerenciaAEditar, setSugerenciaAEditar] = useState({});

  useEffect(() => {
    obtenerQuejasPendientes().then((res) => {
      setQuejas(res.data);
    });
  }, [recargarQuejas]);

  useEffect(() => {
    obtenerSugerenciasPendientes().then((res) => {
      setSugerencias(res.data);
    });
  }, [recargarSugerencias]);

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
            setQuejaAEditar(row);
            // TODO: Llenar los campos del formulario con los datos de la queja
          }}
          className="bg-blue-500 text-white p-2"
        >
          Responder
        </motion.button>
      ),
    },
  ];

  const columnasSugerencias = [
    {
      name: "ID sugerencia",
      selector: (row) => row.idSugerencia,
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
      name: "Comentario de Seguimiento",
      selector: (row) => row.comentarioSeguimiento,
    },
    {
      name: "Acción",
      cell: (row) => (
        <motion.button
          whileHover={{ scale: 1.1 }}
          onClick={() => {
            setAbrirModalSugerencia(true);
            setSugerenciaAEditar(row);
            // TODO: Llenar los campos del formulario con los datos de la queja
          }}
          className="bg-blue-500 text-white p-2"
        >
          Responder
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
    const queja = {
      id_empleado: idEmpleado,
      estado: e.target.add_queja_categoria.value,
      comentarioSeguimiento: e.target.add_queja_descripcion.value,
      id_queja: e.target.id_queja.value,
    };

    toast.promise(responderQueja(queja).then(() => {
      setRecargarQuejas(!recargarQuejas);
      setAbrirModalQueja(false);
    }), {
      loading: "Cargando...",
      success: "¡Operación exitosa!",
      error: "Error al realizar la operación",
    })
  };

  const [abrirModalSugerencia, setAbrirModalSugerencia] = useState(false);
  const cerrarModalSugerencia = (e) => {
    if (e.target.id === "modalResponderSugerencia") {
      setAbrirModalSugerencia(false);
    }
  };
  const manejarResponderSugerencia = async (e) => {
    e.preventDefault();
    const sugerencia = {
      id_empleado: idEmpleado,
      estado: e.target.add_sugerencia_categoria.value,
      comentarioSeguimiento: e.target.add_sugerencia_descripcion.value,
      id_sugerencia: e.target.id_sugerencia.value,
    };

    toast.promise(responderSugerencia(sugerencia).then(() => {
      setRecargarSugerencias(!recargarSugerencias);
      setAbrirModalSugerencia(false);
    }), {
      loading: "Cargando...",
      success: "¡Operación exitosa!",
      error: "Error al realizar la operación",
    })
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
              <p className="font-bold text-xl">Responder una queja</p>
              <form onSubmit={manejarResponderQueja}>
                <label htmlFor="add_queja_descripcion" className="block">
                  Respuesta a la queja
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
                </textarea>
                <label htmlFor="add_queja_categoria" className="block">
                  Estado de la queja
                </label>
                <select
                  name="add_queja_categoria"
                  id="category"
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                  required
                >
                  <option defaultValue={quejaAEditar.estado} disabled>
                    Selecciona estado
                  </option>
                  <option value="Pendiente">
                    Pendiente
                  </option>
                  <option value="Activa">Activa</option>
                  <option value="Finalizada">Finalizada</option>
                </select>
                <input type="text" id="id_queja" hidden value={quejaAEditar.idQueja}/>
                <input
                  type="submit"
                  value="Actualizar queja"
                  className="block bg-blue-500 rounded-lg p-2 text-white font-bold my-2 cursor-pointer"
                />
              </form>
            </div>
          </dialog>
        )}

        {abrirModalSugerencia && (
          <dialog
            id="modalResponderSugerencia"
            className="absolute top-0 right-0 left-0 bottom-0 z-10 w-full h-full bg-slate-900/80 flex justify-center items-center"
            onMouseDown={cerrarModalSugerencia}
          >
            <div
              className="min-h-[50%] min-w-[50%] bg-white rounded-xl p-4 flex flex-col gap-4"
              onClick={(e) => e.stopPropagation()} // Evita cerrar al hacer clic dentro del recuadro
            >
              <p className="font-bold text-xl">Responder una sugerencia</p>
              <form onSubmit={manejarResponderSugerencia}>
                <label htmlFor="add_sugerencia_descripcion" className="block">
                  Respuesta a la sugerencia
                </label>
                <textarea
                  id="add_sugerencia_descripcion"
                  type="text"
                  placeholder="Escribe aquí..."
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400 resize-none"
                  required
                  minLength={2}
                  maxLength={512}
                >
                </textarea>
                <label htmlFor="add_sugerencia_categoria" className="block">
                  Estado de la sugerencia
                </label>
                <select
                  name="add_sugerencia_categoria"
                  id="category"
                  className="w-full max-w-md p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-gray-700 placeholder-gray-400"
                  required
                >
                  <option defaultValue={sugerenciaAEditar.estado} disabled>
                    Selecciona estado
                  </option>
                  <option value="Pendiente">
                    Pendiente
                  </option>
                  <option value="Activa">Activa</option>
                  <option value="Finalizada">Finalizada</option>
                </select>
                <input type="text" id="id_sugerencia" hidden value={sugerenciaAEditar.idSugerencia}/>
                <input
                  type="submit"
                  value="Actualizar sugerencia"
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
              </div>
              <div className="overflow-x-auto">
                <DataTable columns={columnasQuejas} data={quejas} pagination/>
              </div>
            </motion.div>
          </div>

          <div className="w-full h-full p-4">
            <motion.div
              initial={{ x: 200, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="w-full h-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900 flex justify-between items-center">
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-document"></i> Sugerencias
                </h2>
              </div>
              <div className="overflow-x-auto">
                <DataTable columns={columnasSugerencias} data={sugerencias} pagination/>
              </div>
            </motion.div>
          </div>
        </div>
      </div>
    </>
  );
}
