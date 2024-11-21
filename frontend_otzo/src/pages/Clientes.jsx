/*
Página Principal para el Módulo de Clientes
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programación 2 | 1061
*/

import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";

export function Clientes() {
  const [clienteActual, setClienteActual] = useState(null);
  const [clienteParaEditar, setClienteParaEditar] = useState(null);
  const [idCliente, setIdCliente] = useState(null);
  const [listaClientes, setListaClientes] = useState([]);
  const [puntos, setPuntos] = useState([]);
  const [rangos, setRangos] = useState([]);

  useEffect(() => {
    const clienteAlmacenado = localStorage.getItem('cliente');
    if (clienteAlmacenado && clienteAlmacenado !== 'undefined') {
      try {
        const clienteParseado = JSON.parse(clienteAlmacenado);
        console.log("Datos del cliente almacenado:", clienteParseado);
        if (clienteParseado && clienteParseado.idCliente) {
          setIdCliente(clienteParseado.idCliente);
        }
      } catch (error) {
        console.error('Error al parsear el cliente del localStorage:', error);
      }
    }
  }, []);

  useEffect(() => {
    //Para obtener el id del cliente actual (el que inicio sesion)
    if (idCliente) {
      axios.get(`http://localhost:5000/api/clientes/sesionactualcliente/${idCliente}`)
        .then(respuesta => {
          if (respuesta.data && !respuesta.data.error) {
            console.log("Datos del cliente actual:", respuesta.data);
            setClienteActual(respuesta.data);
          } else {
            console.error("Error en la respuesta del servidor para el cliente actual:", respuesta.data);
          }
        })
        .catch(error => {
          console.error("Error al obtener el cliente actual:", error);
        });
    }

    //Para obtener la lista de todos los clientes
    axios.get('http://localhost:5000/api/clientes/clientes')
      .then(respuesta => {
        if (Array.isArray(respuesta.data)) {
          setListaClientes(respuesta.data);
        } else {
          console.error("Error en la respuesta del servidor para la lista de clientes:", respuesta.data);
        }
      })
      .catch(error => {
        console.error("Error al obtener la lista de todos los clientes:", error);
      });

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

  const manejarClickModificar = (cliente) => {
    //Convertimos la fecha de nacimiento a formato "YYYY-MM-DD"
    if (cliente.fecha_nacimiento) {
      const fechaNacimiento = new Date(cliente.fecha_nacimiento);
      const dia = String(fechaNacimiento.getDate() + 1).padStart(2, '0');
      const mes = String(fechaNacimiento.getMonth() + 1).padStart(2, '0');
      const año = fechaNacimiento.getFullYear();
      cliente.fecha_nacimiento = `${año}-${mes}-${dia}`;
    }

    setClienteParaEditar(cliente);
  };

  const manejarConfirmarCambios = () => {
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
    } = clienteParaEditar;

    if (!nombre || !apellido_paterno || !contraseña) {
      alert("Por favor, completa todos los campos obligatorios.");
      return;
    }

    if (contraseña.length > 255) {
      alert("La contraseña no puede tener mas de 255 caracteres.");
      return;
    }

    if (isNaN(direccion_codigopostal)) {
      alert("El codigo postal debe ser un numero.");
      return;
    }

    if (genero !== 'Masculino' && genero !== 'Femenino') {
      alert("El genero debe ser 'Masculino' o 'Femenino'.");
      return;
    }

    axios.put(`http://localhost:5000/api/clientes/modificarcliente/${clienteParaEditar.idCliente}`, clienteParaEditar)
      .then(respuesta => {
        alert("Cambios realizados exitosamente");
        setClienteParaEditar(null);
        window.location.reload();
      })
      .catch(error => {
        console.error("Error al modificar el cliente:", error);
        if (error.response) {
          alert("Error al modificar el cliente: " + (error.response.data.error || ''));
        } else {
          alert("Error al modificar el cliente");
        }
      });
  };

  const manejarCambioEntrada = (e) => {
    const { name, value } = e.target;
    if (clienteParaEditar) {
      setClienteParaEditar({ ...clienteParaEditar, [name]: value });
    }
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
                          return puntosCliente ? puntosCliente.total_puntos : "N/A";
                        })()}
                      </td>
                      <td className="py-2 px-4 border-b text-center">
                        {(() => {
                          const puntosCliente = puntos.find(p => p.idclientes_puntos === clienteActual.idCliente);
                          if (puntosCliente) {
                            const rangoCliente = rangos.find(r => r.idrango === puntosCliente.idrango);
                            return rangoCliente ? rangoCliente.nombre_rango : "N/A";
                          }
                          return "N/A";
                        })()}
                      </td>
                      <td className="py-2 px-4 border-b text-center">{clienteActual.estado_cuenta}</td>
                      <td className="py-2 px-4 border-b text-center">
                        <button onClick={() => manejarClickModificar(clienteActual)} className="bg-blue-500 text-white px-2 py-1 rounded mr-2">Modificar</button>
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
        <div className="grid grid-cols-1 gap-4">
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
        </div>
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
                  value={clienteParaEditar?.nombre ?? ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Nombre"
                  className="p-2 border rounded"
                />
                <label>Apellido Paterno</label>
                <input
                  type="text"
                  name="apellido_paterno"
                  value={clienteParaEditar?.apellido_paterno ?? ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Apellido Paterno"
                  className="p-2 border rounded"
                />
                <label>Apellido Materno</label>
                <input
                  type="text"
                  name="apellido_materno"
                  value={clienteParaEditar?.apellido_materno ?? ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Apellido Materno"
                  className="p-2 border rounded"
                />
                <label>Fecha de Nacimiento</label>
                <input
                  type="date"
                  name="fecha_nacimiento"
                  value={clienteParaEditar?.fecha_nacimiento ?? ''}
                  onChange={manejarCambioEntrada}
                  className="p-2 border rounded"
                />
                <label>Genero</label>
                <select
                  name="genero"
                  value={clienteParaEditar?.genero ?? ''}
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
                  value={clienteParaEditar?.direccion_calle ?? ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Calle"
                  className="p-2 border rounded"
                />
                <label>Colonia</label>
                <input
                  type="text"
                  name="direccion_colonia"
                  value={clienteParaEditar?.direccion_colonia ?? ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Colonia"
                  className="p-2 border rounded"
                />
                <label>Codigo Postal</label>
                <input
                  type="text"
                  name="direccion_codigopostal"
                  value={clienteParaEditar?.direccion_codigopostal ?? ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Codigo Postal"
                  className="p-2 border rounded"
                />
                <label>Estado</label>
                <input
                  type="text"
                  name="direccion_estado"
                  value={clienteParaEditar?.direccion_estado ?? ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Estado"
                  className="p-2 border rounded"
                />
                <label>Municipio</label>
                <input
                  type="text"
                  name="direccion_municipio"
                  value={clienteParaEditar?.direccion_municipio ?? ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Municipio"
                  className="p-2 border rounded"
                />
                <label>Correo Electronico</label>
                <input
                  type="email"
                  name="contacto_correo"
                  value={clienteParaEditar?.contacto_correo ?? ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Correo Electronico"
                  className="p-2 border rounded"
                />
                <label>Contraseña</label>
                <input
                  type="password"
                  name="contraseña"
                  value={clienteParaEditar?.contraseña ?? ''}
                  onChange={manejarCambioEntrada}
                  placeholder="Contraseña"
                  className="p-2 border rounded"
                />
                <label>Telefono</label>
                <input
                  type="text"
                  name="contacto_telefono"
                  value={clienteParaEditar?.contacto_telefono ?? ''}
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
