/*

Pagina Principal para el Modulo de Fidelizacion y Marketing
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import { React, useEffect, useState } from "react";
import { motion } from "framer-motion";
import { FidelizacionData } from "../api/fidelizacionData.api.js";
import axios from "axios";

export function Fidelizacion() {
  const [clientes, setClientes] = useState([]);
  const [puntos, setPuntos] = useState([]);
  const [rangos, setRangos] = useState([]);
  const [loadingClientes, setLoadingClientes] = useState(true);
  const [loadingPuntos, setLoadingPuntos] = useState(true);
  const [loadingRangos, setLoadingRangos] = useState(true);

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
                        <br />a obtener de una Compra
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Porcentaje de Puntos
                        <br />a obtener de una Devolucion
                      </th>
                      <th className="py-2 px-4 border-b text-center">
                        Numero Total de
                        <br />
                        Compras Realizadas
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
    </div>
  );
}