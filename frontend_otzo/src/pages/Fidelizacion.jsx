/*

Pagina Principal para el Modulo de Fidelizacion y Marketing
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import { React, useEffect, useState } from "react";
import { motion } from "framer-motion";
import { FidelizacionData } from "../api/fidelizacionData.api.js";
import axios from "axios";
//Si quieres tener la funcionalidad de poder obtener los datos del usuario que ha iniciado sesion, importa esto:
import { ObtenerTipoUsuario } from "../context/obtenerUsuarioTipo";

export function Fidelizacion() {
  const { clienteActual, idCliente, administradorActual, idEmpleado } = ObtenerTipoUsuario(); // Aqui mandamos a llamar a las variables que contienen la info del que inicio sesion.
  const [mostrarMensajeModalAutorizacion, setmostrarMensajeModalAutorizacion] = useState(false);
  const [modalMessage, setModalMessage] = useState('');
  const [clientes, setClientes] = useState([]);
  const [puntos, setPuntos] = useState([]);
  const [rangos, setRangos] = useState([]);
  const [loadingClientes, setLoadingClientes] = useState(true);
  const [loadingPuntos, setLoadingPuntos] = useState(true);
  const [loadingRangos, setLoadingRangos] = useState(true);

  useEffect(() => {
    //Para obtener la lista de todos los administradores
    axios.get('http://localhost:5000/api/administracion/administradores')
      .then(respuesta => {
        if (Array.isArray(respuesta.data)) {
          setListaAdministradores(respuesta.data);
        } else {
          console.error("Error en la respuesta del servidor para la lista de administradores:", respuesta.data);
        }
      })
      .catch(error => {
        console.error("Error al obtener la lista de todos los administradores:", error);
      });
  }, [idEmpleado]);

  const verificarPermisosAdministrador = () => {
    const estadosRestringidos = ['Suspendido', 'Inactivo', 'Baneado'];
    const areasPermitidas = ['Fidelizacion', 'Administracion', 'DBA'];
  
    if (administradorActual && estadosRestringidos.includes(administradorActual.estado_cuenta)) {
      setModalMessage(
        `No puede usar este boton porque su cuenta tiene el estado: "${administradorActual.estado_cuenta}"\n
         Por favor, contacte al DBA o a algun otro Administrador para poder resolver este problema.`
      );
      setmostrarMensajeModalAutorizacion(true);
      return false;
    }
  
    if (!administradorActual || !areasPermitidas.includes(administradorActual.area_Trabajo)) {
      setModalMessage(
        `No puede usar este boton debido a que no tiene el area de trabajo necesario para poder usar estos botones.\n
        Solo los usuarios con las areas de trabajo: ${areasPermitidas.join(', ')} tienen acceso.\n
        Su area de trabajo actual es: ${administradorActual ? administradorActual.area_Trabajo : 'Desconocida'}.`
      );
      setmostrarMensajeModalAutorizacion(true);
      return false;
    }
  
    return true;
  };

  const asignarRangoInicial = async () => {
    if (!verificarPermisosAdministrador()) return;
    try {
      const response = await axios.get("http://localhost:5000/api/fidelizacion/asigrnginiauto");
      alert(response.data.mensaje || "Clientes nuevos añadidos exitosamente");
      console.log("Clientes nuevos añadidos:", response.data);
      window.location.reload();
    } catch (error) {
      console.error("Error al añadir clientes nuevos:", error.response?.data || error.message);
      alert("Hubo un error al intentar añadir clientes nuevos.");
    }
  };

  useEffect(() => {
    FidelizacionData()
      .then((response) => {
        console.log("Respuesta de fidelizacion:", response.data);
      })
      .catch((error) =>
        console.error(
          "Error al obtener la respuesta de la API de fidelizacion:",
          error
        )
      );

    axios
      .get("http://localhost:5000/api/fidelizacion/obtcli")
      .then((response) => {
        setClientes(response.data.Clientes);
        setLoadingClientes(false);
      })
      .catch((error) => {
        console.error("Error al obtener los clientes:", error);
        setLoadingClientes(false);
      });

    axios
      .get("http://localhost:5000/api/fidelizacion/obtenerpuntos")
      .then((response) => {
        setPuntos(response.data.Puntos);
        setLoadingPuntos(false);
      })
      .catch((error) => {
        console.error("Error al obtener los puntos:", error);
        setLoadingPuntos(false);
      });

    axios
      .get("http://localhost:5000/api/fidelizacion/obtenerrango")
      .then((response) => {
        setRangos(response.data.Rangos);
        setLoadingRangos(false);
      })
      .catch((error) => {
        console.error("Error al obtener los rangos:", error);
        setLoadingRangos(false);
      });
  }, []);

  return (
    <div className="bg-gradient-to-r from-purple-400 to-purple-500 w-full h-full min-h-[calc(100vh-5rem)] z-0 relative">
      <motion.h1
        initial={{ scale: 0 }}
        animate={{ scale: 1, transition: { delay: 0.5 } }}
        className="text-center text-white text-6xl font-bold"
      >
        Fidelizacion y Marketing
      </motion.h1>
      <br />
      <div className="flex justify-center mt-4">
        <motion.div
          initial={{ scale: 0 }}
          animate={{ scale: 1, transition: { delay: 0.6 } }}
          className="text-center"
        >
          <button
            onClick={asignarRangoInicial}
            className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-6 rounded-lg shadow-lg transition-transform transform hover:scale-105"
          >
            Añadir clientes nuevos
          </button>
        </motion.div>
      </div>
      <div className="flex flex-col gap-4">
        <div className="flex flex-col gap-2 p-4 md:p-8">
          {/* Recuadro - Cliente actual */}
          {/*<div className="w-full flex justify-center">
            <motion.div
              initial={{ x: 0, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="w-full md:w-2/3 bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
              style={{ minHeight: "auto", overflowX: "auto" }}
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900">
                <center>
                  <h2 className="font-bold text-white">
                    <i className="align-middle fi fi-sr-user"></i> Cliente
                    actual
                  </h2>
                </center>
              </div>
               <div className="overflow-x-auto">
                <table className="min-w-full bg-white">
                  <thead>
                    <tr>
                      <th className="py-2 px-4 border-b text-center">
                        ID Cliente
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Nombre Completo
                      </th>
                      <th className="py-2 px-4 border-b text-center">Rango</th>
                      <th className="py-2 px-4 border-b text-center">
                        Total de Puntos
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Estado de la Cuenta
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Fecha de Ultima Actualizacion de Puntos
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Fecha de Ultima Actualizacion de Rango
                      </th>
                      <th className="py-2 px-3 border-b text-center">
                        Cuenta Habilitada
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    {clientes.slice(0, 1).map((cliente, index) => {
                      const puntosCliente = puntos.find(
                        (p) => p.idclientes_puntos === cliente.idCliente
                      );
                      const rangoCliente = puntosCliente
                        ? rangos.find(
                            (r) => r.idrango === puntosCliente.idrango
                          )
                        : null;
                      return (
                        <tr
                          key={cliente.idCliente}
                          className={
                            index % 2 === 0 ? "bg-gray-100" : "bg-gray-200"
                          }
                        >
                          <td className="py-2 px-4 border-b text-center">
                            {cliente.idCliente}
                          </td>
                          <td className="py-2 px-4 border-b text-center">{`${cliente.nombre} ${cliente.apellido_paterno} ${cliente.apellido_materno}`}</td>
                          <td className="py-2 px-4 border-b text-center">
                            {rangoCliente
                              ? rangoCliente.nombre_rango
                              : "Este cliente NO puede obtener rango debido al estado de su cuenta."}
                          </td>
                          <td className="py-2 px-4 border-b text-center">
                            {puntosCliente
                              ? puntosCliente.total_puntos
                              : "Este Cliente NO puede obtener puntos debido al estado de su cuenta."}
                          </td>
                          <td className="py-2 px-4 border-b text-center">
                            {cliente.estado_cuenta}
                          </td>
                          <td className="py-2 px-4 border-b text-center">
                            {puntosCliente
                              ? puntosCliente.ultima_actualizacionPuntos
                              : "Este Cliente NO puede consultar su ultimo movimiento de puntos debido al estado de su cuenta."}
                          </td>
                          <td className="py-2 px-4 border-b text-center">
                            {puntosCliente
                              ? puntosCliente.ultima_actualizacionRangos
                              : "Este Cliente NO puede consultar su ultimo movimiento de rangos debido al estado de su cuenta."}
                          </td>
                          <td className="py-2 px-4 border-b text-center">
                            {puntosCliente && puntosCliente.habilitado
                              ? "SI"
                              : "NO (Este cliente NO puede obtener rangos ni puntos debido al estado de su cuenta)"}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </motion.div>
          </div>*/}

          {/* div para los recuadros inferiores */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/*  Recuadro - Info de todos los clientes */}
            <motion.div
              initial={{ x: -100, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="w-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900">
                <center>
                  <h2 className="font-bold text-white">
                    <i className="align-middle fi fi-sr-document"></i>{" "}
                    Informacion de todos los clientes que se encuentran en la tabla "puntos"
                  </h2>
                </center>
              </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)] overflow-y-auto">
                {/* TABLA - Info clientes */}
                <table className="min-w-full bg-white">
                  <thead>
                    <tr>
                      <th className="py-2 px-4 border-b text-center">
                        ID Cliente
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Nombre Completo
                      </th>
                      <th className="py-2 px-4 border-b text-center">Rango</th>
                      <th className="py-2 px-4 border-b text-center">
                        Total de Puntos
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Estado de la Cuenta
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Fecha de Ultima Actualizacion de Puntos
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Fecha de Ultima Actualizacion de Rango
                      </th>
                      <th className="py-2 px-3 border-b text-center">
                        Cuenta Habilitada
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    {clientes.map((cliente, index) => {
                      const puntosCliente = puntos.find(
                        (p) => p.idclientes_puntos === cliente.idCliente
                      );
                      const rangoCliente = puntosCliente
                        ? rangos.find(
                            (r) => r.idrango === puntosCliente.idrango
                          )
                        : null;
                      return (
                        <tr
                          key={cliente.idCliente}
                          className={
                            index % 2 === 0 ? "bg-gray-100" : "bg-gray-200"
                          }
                        >
                          <td className="py-2 px-4 border-b text-center">
                            {cliente.idCliente}
                          </td>
                          <td className="py-2 px-4 border-b text-center">{`${cliente.nombre} ${cliente.apellido_paterno} ${cliente.apellido_materno}`}</td>
                          <td className="py-2 px-4 border-b text-center">
                            {rangoCliente
                              ? rangoCliente.nombre_rango
                              : "Este cliente NO puede obtener rango debido al estado de su cuenta. (No se encuentra en la BD o en la tabla)"}
                          </td>
                          <td className="py-2 px-4 border-b text-center">
                            {puntosCliente
                              ? puntosCliente.total_puntos
                              : "Este Cliente NO puede obtener puntos debido al estado de su cuenta. (No se encuentra en la BD o en la tabla)"}
                          </td>
                          <td className="py-2 px-4 border-b text-center">
                            {cliente.estado_cuenta}
                          </td>
                          <td className="py-2 px-4 border-b text-center">
                            {puntosCliente
                              ? puntosCliente.ultima_actualizacionPuntos
                              : "Este Cliente NO puede consultar su ultimo movimiento de puntos debido al estado de su cuenta. (No se encuentra en la BD o en la tabla)"}
                          </td>
                          <td className="py-2 px-4 border-b text-center">
                            {puntosCliente
                              ? puntosCliente.ultima_actualizacionRangos
                              : "Este Cliente NO puede consultar su ultimo movimiento de rangos debido al estado de su cuenta. (No se encuentra en la BD o en la tabla)"}
                          </td>
                          <td className="py-2 px-4 border-b text-center">
                            {puntosCliente && puntosCliente.habilitado
                              ? "SI"
                              : "NO (Este cliente NO puede obtener rangos ni puntos debido al estado de su cuenta)"}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </motion.div>

            {/*  Recuadro - Info de todos los rangos */}
            <motion.div
              initial={{ x: 100, opacity: 0 }}
              animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
              className="w-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
            >
              <div className="shadow-lg rounded-lg p-4 bg-gray-900">
                <center>
                  <h2 className="font-bold text-white">
                    <i className="align-middle fi fi-sr-document"></i>{" "}
                    Informacion de todos los rangos
                  </h2>
                </center>
              </div>
              <div className="h-[calc(25vh)] md:h-[calc(50vh)] overflow-y-auto">
                {/* TABLA - Info rangos */}
                <table className="min-w-full bg-white">
                  <thead>
                    <tr>
                      <th className="py-2 px-4 border-b text-center">
                        ID Rango
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Nombre del Rango
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Porcentaje de Puntos
                        <br />a obtener de una Compra (%)
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Porcentaje de Puntos
                        <br />a obtener de una Devolucion (%)
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Numero Total de
                        <br />
                        Compras Necesarias
                        <br />
                        para obtener este Rango
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    {rangos.map((rango, index) => (
                      <tr
                        key={rango.idrango}
                        className={
                          index % 2 === 0 ? "bg-gray-100" : "bg-gray-200"
                        }
                      >
                        <td className="py-2 px-4 border-b text-center">
                          {rango.idrango}
                        </td>
                        <td className="py-2 px-4 border-b text-center">
                          {rango.nombre_rango}
                        </td>
                        <td className="py-2 px-4 border-b text-center">
                          {rango.porcentaje_puntos}
                        </td>
                        <td className="py-2 px-4 border-b text-center">
                          {rango.porcentaje_devolucionPuntos}
                        </td>
                        <td className="py-2 px-4 border-b text-center">
                          {rango.num_ComprasRequisito}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </motion.div>
          </div>
        </div>
      </div>
      {/* Modal - autorizacion */}
      {mostrarMensajeModalAutorizacion && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
            <div className="bg-white rounded-lg shadow-lg p-4 w-full max-w-md">
              <h2 className="text-2xl font-bold mb-4 text-center">Acceso Denegado</h2>
              <p className="mb-4 text-center">
                {modalMessage.split('\n').map((line, index) => (
                  <span key={index}>
                    {line.trim()}
                    <br />
                  </span>
                ))}
              </p>
              <div className="flex justify-center mt-4">
                <button
                  type="button"
                  onClick={() => setmostrarMensajeModalAutorizacion(false)}
                  className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                  Cerrar
                </button>
              </div>
            </div>
          </div>
        )}
    </div>
  );
}