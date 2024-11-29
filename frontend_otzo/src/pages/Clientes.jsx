/*

Página Principal para el Modulo de Clientes
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programación 2 | 1061

*/

import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";
//Si quieres tener la funcionalidad de poder obtener los datos del usuario que ha iniciado sesion, importa esto:
import { ObtenerTipoUsuario } from "../context/obtenerUsuarioTipo";

export function Clientes() {
  const { clienteActual, idCliente } = ObtenerTipoUsuario(); // Aqui mandamos a llamar a las variables que contienen la info del que inicio sesion.
  const [clienteParaEditar, setClienteParaEditar] = useState(null);
  const [puntos, setPuntos] = useState([]);
  const [rangos, setRangos] = useState([]);

  useEffect(() => {
    //Para obtener los puntos y los rangos
    axios.get('http://localhost:5000/api/fidelizacion/obtenerpuntos')
      .then(response => {
        setPuntos(response.data.Puntos);
      })
      .catch(error => {
        console.error("Error al obtener los puntos:", error);
      });

    axios.get('http://localhost:5000/api/fidelizacion/obtenerrango')
      .then(response => {
        setRangos(response.data.Rangos);
      })
      .catch(error => {
        console.error("Error al obtener los rangos:", error);
      });
  }, [idCliente]);

  const validarCliente = (cliente) => {
    const {
      nombre,
      apellido_paterno,
      apellido_materno,
      fecha_nacimiento,
      genero,
      direccion_calle,
      direccion_colonia,
      direccion_codigopostal,
      direccion_estado,
      direccion_municipio,
      contacto_correo,
      contraseña,
      contacto_telefono,
    } = cliente;

    if (!nombre || !apellido_paterno || !apellido_materno) {
      //alert("Por favor, complete los campos: Nombre, Apellido Paterno y Apellido Materno.");
      return "Por favor, complete los campos: Nombre, Apellido Paterno y Apellido Materno.";
    }

    if (!fecha_nacimiento) {
      //alert("Ingrese una fecha de nacimiento.");
      return "Ingrese una fecha de nacimiento.";
    }

    if (fecha_nacimiento && !/^\d{4}-\d{2}-\d{2}$/.test(fecha_nacimiento)) {
      //alert("La fecha de nacimiento debe tener el formato AAAA-MM-DD.");
      return "La fecha de nacimiento debe tener el formato AAAA-MM-DD.";
    }

    if (genero !== "Masculino" && genero !== "Femenino") {
      //alert("Seleccione un genero. ('Masculino' o 'Femenino')");
      return "Seleccione un genero. ('Masculino' o 'Femenino')";
    }

    if (!direccion_calle || !direccion_colonia || !direccion_codigopostal || !direccion_estado || !direccion_municipio) {
      //alert("Por favor, complete los campos: Calle, Colonia, Codigo Postal, Estado y Municipio.");
      return "Por favor, complete los campos: Calle, Colonia, Codigo Postal, Estado y Municipio.";
    }

    if (direccion_codigopostal && (!/^\d{5,8}$/.test(direccion_codigopostal) || direccion_codigopostal.length > 10)) {
      //alert("El codigo postal debe tener entre 5 y 8 digitos.");
      return "El codigo postal debe tener entre 5 y 8 digitos.";
    }

    if (!contacto_correo) {
      //alert("Ingrese un correo electronico");
      return "Ingrese un correo electronico";
    }

    if (contacto_correo && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(contacto_correo)) {
      //alert("Ingrese un correo electronico valido.");
      return "Ingrese un correo electronico valido.";
    }

    if (!contraseña) {
      //alert("Ingrese una contraseña");
      return "Ingrese una contraseña";
    }

    if (contraseña && (contraseña.length > 255 || contraseña.length < 6)) {
      //alert("La contraseña debe tener entre 6 y 255 caracteres.");
      return "La contraseña debe tener entre 6 y 255 caracteres.";
    }

    if (!contacto_telefono) {
      //alert("Ingrese un numero telefonico");
      return "Ingrese un numero telefonico";
    }

    if (contacto_telefono && !/^\d{8,15}$/.test(contacto_telefono)) {
      //alert("El telefono debe ser un numero valido de entre 8 y 15 digitos.");
      return "El telefono debe ser un numero valido de entre 8 y 15 digitos.";
    }

    return null;
  };

  const manejarCambioEntrada = (e) => {
    const { name, value } = e.target;
    if (clienteParaEditar) {
      setClienteParaEditar({ ...clienteParaEditar, [name]: value });
    }
  };

  const manejarConfirmarCambios = () => {
    const error = validarCliente(clienteParaEditar);
    if (error) {
      alert(error);
      return;
    }

  const datosActualizados = { ...clienteParaEditar };

  axios.put(`http://localhost:5000/api/clientes/modificarcliente/${clienteParaEditar.idCliente}`, datosActualizados)
      .then(() => {
        alert("Cambios realizados exitosamente.");
        setClienteParaEditar(null);
        window.location.reload();
      })
      .catch(error => {
        console.error("Error al modificar el cliente:", error);
        alert("Error al modificar el cliente.");
      });
  };
  
  const manejarClickModificar = (cliente) => {
    setClienteParaEditar(cliente);
  };

  return (
    <div className='bg-gradient-to-r from-yellow-400 to-yellow-500 w-full min-h-screen z-0 relative'>
      <motion.h1 initial={{ scale: 0 }} animate={{ scale: 1, transition: { delay: 0.5 } }} className='text-center text-white text-4xl md:text-6xl font-bold p-4'>Clientes</motion.h1>

      <div className="flex flex-col gap-4 p-4 md:p-8">
        {/* Recuadro - Cliente actual */}
        <div className="w-full flex justify-center">
          <motion.div
            initial={{ x: 0, opacity: 0 }}
            animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
            className="w-full md:w-2/3 bg-white rounded-lg p-4 shadow-lg overflow-x-auto"
          >
            <div className="shadow-lg rounded-lg p-4 bg-gray-900">
              <center>
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-user"></i> Cliente Actual
                </h2>
              </center>
            </div>
            <div className="overflow-x-auto">
              <table className="min-w-full bg-white">
                <thead>
                  <tr>
                    <th className="py-2 px-4 border-b text-center">ID</th>
                    <th className="py-2 px-4 border-b text-center">Nombre</th>
                    <th className="py-2 px-4 border-b text-center">Apellido Paterno</th>
                    <th className="py-2 px-4 border-b text-center">Apellido Materno</th>
                    <th className="py-2 px-4 border-b text-center">Correo Electronico</th>
                    <th className="py-2 px-4 border-b text-center">Telefono</th>
                    <th className="py-2 px-4 border-b text-center">Total de Puntos</th>
                    <th className="py-2 px-4 border-b text-center">Rango Actual</th>
                    <th className="py-2 px-4 border-b text-center">Estado de la Cuenta</th>
                    <th className="py-2 px-4 border-b text-center">Accion</th>
                  </tr>
                </thead>
                <tbody>
                  {clienteActual ? (
                    <tr>
                      <td className="py-2 px-4 border-b text-center">{clienteActual.idCliente}</td>
                      <td className="py-2 px-4 border-b text-center">{clienteActual.nombre}</td>
                      <td className="py-2 px-4 border-b text-center">{clienteActual.apellido_paterno}</td>
                      <td className="py-2 px-4 border-b text-center">{clienteActual.apellido_materno}</td>
                      <td className="py-2 px-4 border-b text-center">{clienteActual.contacto_correo}</td>
                      <td className="py-2 px-4 border-b text-center">{clienteActual.contacto_telefono}</td>
                      {/* Para poder mostrar el total de puntos y el rango del cliente actual */}
                      <td className="py-2 px-4 border-b text-center">
                        {(() => {
                          const puntosCliente = puntos.find(p => p.idclientes_puntos === clienteActual.idCliente);
                          return puntosCliente ? puntosCliente.total_puntos : "N/A (Cierre e inicie sesion de nuevo para actualizar su cuenta. Si no funciona, contacte a Atencion al Cliente)";
                        })()}
                      </td>
                      <td className="py-2 px-4 border-b text-center">
                        {(() => {
                          const puntosCliente = puntos.find(p => p.idclientes_puntos === clienteActual.idCliente);
                          if (puntosCliente) {
                            const rangoCliente = rangos.find(r => r.idrango === puntosCliente.idrango);
                            return rangoCliente ? rangoCliente.nombre_rango : "N/A (Cierre e inicie sesion de nuevo para actualizar su cuenta. Si no funciona, contacte a Atencion al Cliente)";
                          }
                          return "N/A (Cierre e inicie sesion de nuevo para actualizar su cuenta. Si no funciona, contacte a Atencion al Cliente)";
                        })()}
                      </td>
                      <td className="py-2 px-4 border-b text-center">{clienteActual.estado_cuenta}</td>
                      <td className="py-2 px-4 border-b text-center">
                        <button onClick={() => manejarClickModificar(clienteActual)} className="bg-blue-500 text-white px-2 py-1 rounded mr-2">Modificar Informacion</button>
                      </td>
                    </tr>
                  ) : (
                    <tr>
                      <td colSpan="9" className="py-2 px-4 border-b text-center">No se encontro informacion del cliente actual.</td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </motion.div>
        </div>

        {/* Recuadro - Lista de clientes */}
        {/*<div className="grid grid-cols-1 gap-4">
          <motion.div
            initial={{ x: -100, opacity: 0 }}
            animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
            className="w-full bg-white rounded-lg p-4 shadow-lg"
          >
            <div className="shadow-lg rounded-lg p-4 bg-gray-900">
              <center>
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-users"></i> Lista de Clientes
                </h2>
              </center>
            </div>
            <div className="overflow-x-auto">
              <table className="min-w-full bg-white">
                <thead>
                  <tr>
                    <th className="py-2 px-4 border-b text-center">ID</th>
                    <th className="py-2 px-4 border-b text-center">Nombre</th>
                    <th className="py-2 px-4 border-b text-center">Apellido Paterno</th>
                    <th className="py-2 px-4 border-b text-center">Apellido Materno</th>
                    <th className="py-2 px-4 border-b text-center">Correo Electronico</th>
                    <th className="py-2 px-4 border-b text-center">Telefono</th>
                    <th className="py-2 px-4 border-b text-center">Accion</th>
                  </tr>
                </thead>
                <tbody>
                  {listaClientes.length > 0 ? (
                    listaClientes.map((cliente, index) => (
                      <tr key={cliente.idCliente} className={index % 2 === 0 ? "bg-gray-100" : "bg-gray-200"}>
                        <td className="py-2 px-4 border-b text-center">{cliente.idCliente}</td>
                        <td className="py-2 px-4 border-b text-center">{cliente.nombre}</td>
                        <td className="py-2 px-4 border-b text-center">{cliente.apellido_paterno}</td>
                        <td className="py-2 px-4 border-b text-center">{cliente.apellido_materno}</td>
                        <td className="py-2 px-4 border-b text-center">{cliente.contacto_correo}</td>
                        <td className="py-2 px-4 border-b text-center">{cliente.contacto_telefono}</td>
                        <td className="py-2 px-4 border-b text-center">
                          <button onClick={() => manejarClickModificar(cliente)} className="bg-blue-500 text-white px-2 py-1 rounded mr-2">Modificar</button>
                        </td>
                      </tr>
                    ))
                  ) : (
                    <tr>
                      <td colSpan="7" className="py-2 px-4 border-b text-center">No se encontraron clientes.</td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </motion.div>
        </div>*/}
        {/* Recuadro - Lista de todos los rangos */}
        <motion.div
          initial={{ x: 100, opacity: 0 }}
          animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
          className="w-full bg-white/100 rounded-lg p-4 shadow-[0px_4px_6px_0px_rgba(0,_0,_0,_0.1)]"
        >
          <div className="shadow-lg rounded-lg p-4 bg-gray-900">
            <center>
              <h2 className="font-bold text-white">
                <i className="align-middle fi fi-sr-document"></i> Rangos Que Usted Puede Obtener y sus Beneficios
              </h2>
            </center>
          </div>
          <div className="h-[calc(25vh)] md:h-[calc(50vh)] overflow-y-auto">
            <table className="min-w-full bg-white">
              <thead>
                <tr>
                  <th className="py-2 px-4 border-b text-center">Nombre del Rango</th>
                  <th className="py-2 px-4 border-b text-center">
                    Porcentaje de Puntos<br />a obtener de una Compra (%)
                  </th>
                  <th className="py-2 px-4 border-b text-center">
                    Porcentaje de Puntos<br />a obtener de una Devolucion (%)
                  </th>
                  <th className="py-2 px-4 border-b text-center">
                    Numero Total de<br />Compras Necesarias<br />para obtener este Rango
                  </th>
                </tr>
              </thead>
              <tbody>
                {rangos.map((rango, index) => (
                  <tr
                    key={rango.idrango}
                    className={index % 2 === 0 ? "bg-gray-100" : "bg-gray-200"}
                  >
                    <td className="py-2 px-4 border-b text-center">{rango.nombre_rango}</td>
                    <td className="py-2 px-4 border-b text-center">{rango.porcentaje_puntos}</td>
                    <td className="py-2 px-4 border-b text-center">{rango.porcentaje_devolucionPuntos}</td>
                    <td className="py-2 px-4 border-b text-center">{rango.num_ComprasRequisito}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </motion.div>
      </div>
      {/* Formulario para poder modificar el cliente */}
      {clienteParaEditar && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-lg shadow-lg p-4 w-full max-w-md md:max-w-lg max-h-[90vh] overflow-y-auto">
            <h2 className="text-2xl font-bold mb-4 text-center">Modificar Cliente</h2>
            <form>
              <div className="grid grid-cols-1 gap-4">
                <label>Nombre</label>
                <input
                  type="text"
                  name="nombre"
                  value={clienteParaEditar?.nombre || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Nombre"
                  className="p-2 border rounded"
                />
                <label>Apellido Paterno</label>
                <input
                  type="text"
                  name="apellido_paterno"
                  value={clienteParaEditar?.apellido_paterno || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Apellido Paterno"
                  className="p-2 border rounded"
                />
                <label>Apellido Materno</label>
                <input
                  type="text"
                  name="apellido_materno"
                  value={clienteParaEditar?.apellido_materno || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Apellido Materno"
                  className="p-2 border rounded"
                />
                <label>Fecha de Nacimiento</label>
                <input
                  type="date"
                  name="fecha_nacimiento"
                  value={clienteParaEditar?.fecha_nacimiento || ''}
                  onChange={manejarCambioEntrada}
                  className="p-2 border rounded"
                />
                <label>Genero</label>
                <select
                  name="genero"
                  value={clienteParaEditar?.genero || ''}
                  onChange={manejarCambioEntrada}
                  className="p-2 border rounded"
                >
                  <option value="">Seleccione</option>
                  <option value="Masculino">Masculino</option>
                  <option value="Femenino">Femenino</option>
                </select>
                <label>Calle</label>
                <input
                  type="text"
                  name="direccion_calle"
                  value={clienteParaEditar?.direccion_calle || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Calle"
                  className="p-2 border rounded"
                />
                <label>Colonia</label>
                <input
                  type="text"
                  name="direccion_colonia"
                  value={clienteParaEditar?.direccion_colonia || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Colonia"
                  className="p-2 border rounded"
                />
                <label>Codigo Postal</label>
                <input
                  type="text"
                  name="direccion_codigopostal"
                  value={clienteParaEditar?.direccion_codigopostal || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Codigo Postal"
                  className="p-2 border rounded"
                />
                <label>Estado</label>
                <input
                  type="text"
                  name="direccion_estado"
                  value={clienteParaEditar?.direccion_estado || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Estado"
                  className="p-2 border rounded"
                />
                <label>Municipio</label>
                <input
                  type="text"
                  name="direccion_municipio"
                  value={clienteParaEditar?.direccion_municipio || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Municipio"
                  className="p-2 border rounded"
                />
                <label>Correo Electronico</label>
                <input
                  type="email"
                  name="contacto_correo"
                  value={clienteParaEditar?.contacto_correo || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Correo Electronico"
                  className="p-2 border rounded"
                />
                <label>Contraseña</label>
                <input
                  type="password"
                  name="contraseña"
                  value={clienteParaEditar?.contraseña || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Contraseña"
                  className="p-2 border rounded"
                />
                <label>Telefono</label>
                <input
                  type="text"
                  name="contacto_telefono"
                  value={clienteParaEditar?.contacto_telefono || ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Telefono"
                  className="p-2 border rounded"
                />
              </div>
              <div className="flex justify-center mt-4">
                <button type="button" onClick={manejarConfirmarCambios} className="bg-green-500 text-white px-4 py-2 rounded">
                  Confirmar Cambios
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setClienteParaEditar(null);
                  }}
                  className="ml-4 bg-gray-500 text-white px-4 py-2 rounded"
                >
                  Cancelar
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
