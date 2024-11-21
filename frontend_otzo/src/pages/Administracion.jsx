/*

Pagina Principal para el Modulo de Administracion
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import { React, useEffect, useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";

export function Administracion() {
  const [administradorActual, setAdministradorActual] = useState(null);
  const [listaAdministradores, setListaAdministradores] = useState([]);
  const [administradorParaEditar, setAdministradorParaEditar] = useState(null);
  const [administradorParaAñadir, setAdministradorParaAñadir] = useState(null);
  const administradorAlmacenado = localStorage.getItem('administrador');
  let idEmpleado = null;

  if (administradorAlmacenado && administradorAlmacenado !== 'undefined') {
    try {
      const administradorParseado = JSON.parse(administradorAlmacenado);
      console.log("Datos del administrador almacenado:", administradorParseado);
      if (administradorParseado && administradorParseado.id_empleado) {
        idEmpleado = administradorParseado.id_empleado;
      }
    } catch (error) {
      console.error('Error al parsear el administrador del localStorage:', error);
    }
  }
  console.log("ID del empleado obtenido:", idEmpleado);

  useEffect(() => {
    //Para obtener el id del administrador actual (el que inicio sesion)
    if (idEmpleado) {
      axios.get(`http://localhost:5000/api/administracion/sesionactualadmin/${idEmpleado}`)
        .then(respuesta => {
          if (respuesta.data && !respuesta.data.error) {
            setAdministradorActual(respuesta.data);
          } else {
            console.error("Error en la respuesta del servidor para el administrador actual:", respuesta.data);
          }
        })
        .catch(error => {
          console.error("Error al obtener el administrador actual:", error);
        });
    }

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

  const manejarClickModificar = (administrador) => {
    //Convertimos la fecha de nacimiento a formato "YYYY-MM-DD"
    if (administrador.fecha_nacimiento) {
      const fechaNacimiento = new Date(administrador.fecha_nacimiento);
      const dia = String(fechaNacimiento.getDate() + 1).padStart(2, '0');
      const mes = String(fechaNacimiento.getMonth() + 1).padStart(2, '0');
      const año = fechaNacimiento.getFullYear();
      administrador.fecha_nacimiento = `${año}-${mes}-${dia}`;
    }

    setAdministradorParaEditar(administrador);
  };

  const manejarConfirmarCambios = () => {
    const {
      nombre,
      apellido_paterno,
      contraseña,
      direccion_codigopostal,
      genero,
      area_Trabajo,
    } = administradorParaEditar;

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

    const areasValidas = ['Almacen', 'Administracion', 'Clientes', 'DBA', 'Fidelizacion', 'Reabastecimiento', 'Ventas', 'Servicio al cliente'];
    if (!areasValidas.includes(area_Trabajo)) {
      alert("Area de Trabajo invalida.");
      return;
    }

    axios.put(`http://localhost:5000/api/administracion/modificaradmin/${administradorParaEditar.id_empleado}`, administradorParaEditar)
      .then(respuesta => {
        alert("Cambios realizados exitosamente");
        setAdministradorParaEditar(null);
        window.location.reload();
      })
      .catch(error => {
        console.error("Error al modificar el administrador:", error);
        if (error.response) {
          alert("Error al modificar el administrador: " + (error.response.data.error || ''));
        } else {
          alert("Error al modificar el administrador");
        }
      });
  };

  const manejarCambioEntrada = (e) => {
    const { name, value } = e.target;
    if (administradorParaEditar) {
      setAdministradorParaEditar({ ...administradorParaEditar, [name]: value });
    } else {
      setAdministradorParaAñadir({ ...administradorParaAñadir, [name]: value });
    }
  };

  const manejarDarDeBaja = (id_empleado) => {
    axios.delete(`http://localhost:5000/api/administracion/darbajaadmin/${id_empleado}`)
      .then(respuesta => {
        alert(respuesta.data.mensaje);
        window.location.reload();
      })
      .catch(error => {
        console.error("Error al dar de baja al administrador:", error);
      });
  };

  const manejarClickAñadirAdministrador = () => {
    setAdministradorParaAñadir({
      nombre: "",
      apellido_paterno: "",
      apellido_materno: "",
      fecha_nacimiento: "",
      genero: "",
      direccion_calle: "",
      direccion_colonia: "",
      direccion_codigopostal: "",
      direccion_estado: "",
      direccion_municipio: "",
      contacto_correo: "",
      contraseña: "",
      contacto_telefono: "",
      area_Trabajo: ""
    });
  };

  const manejarConfirmarAñadir = () => {
    const {
      nombre,
      apellido_paterno,
      contraseña,
      direccion_codigopostal,
      genero,
      area_Trabajo,
    } = administradorParaAñadir;

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

    const areasValidas = ['Almacen', 'Administracion', 'Clientes', 'DBA', 'Fidelizacion', 'Reabastecimiento', 'Ventas', 'Servicio al cliente'];
    if (!areasValidas.includes(area_Trabajo)) {
      alert("Area de Trabajo invalida.");
      return;
    }

    console.log(administradorParaAñadir);
    axios.post('http://localhost:5000/api/administracion/crearadmin', administradorParaAñadir)
      .then(respuesta => {
        alert("Administrador añadido exitosamente");
        setAdministradorParaAñadir(null);
        window.location.reload();
      })
      .catch(error => {
        console.error("Error al Añadir el administrador:", error);
        if (error.response) {
          alert("Error al Añadir el administrador: " + (error.response.data.error || ''));
        } else {
          alert("Error al Añadir el administrador");
        }
      });
  };

  return (
    <div className='bg-gradient-to-r from-red-400 to-red-500 w-full min-h-screen z-0 relative'>
      <motion.h1 initial={{ scale: 0 }} animate={{ scale: 1, transition: { delay: 0.5 } }} className='text-center text-white text-4xl md:text-6xl font-bold p-4'>Administracion</motion.h1>
      
      <div className="flex flex-col gap-4 p-4 md:p-8">
        {/* Recuadro - Administrador actual */}
        <div className="w-full flex justify-center">
          <motion.div
            initial={{ x: 0, opacity: 0 }}
            animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
            className="w-full md:w-2/3 bg-white rounded-lg p-4 shadow-lg overflow-x-auto"
          >
            <div className="shadow-lg rounded-lg p-4 bg-gray-900">
              <center>
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-admin"></i> Administrador Actual
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
                    <th className="py-2 px-4 border-b text-center">Area de Trabajo</th>
                    <th className="py-2 px-4 border-b text-center">Estado de Cuenta</th>
                  </tr>
                </thead>
                <tbody>
                  {administradorActual ? (
                    <tr>
                      <td className="py-2 px-4 border-b text-center">{administradorActual.id_empleado}</td>
                      <td className="py-2 px-4 border-b text-center">{administradorActual.nombre}</td>
                      <td className="py-2 px-4 border-b text-center">{administradorActual.apellido_paterno}</td>
                      <td className="py-2 px-4 border-b text-center">{administradorActual.apellido_materno}</td>
                      <td className="py-2 px-4 border-b text-center">{administradorActual.contacto_correo}</td>
                      <td className="py-2 px-4 border-b text-center">{administradorActual.contacto_telefono}</td>
                      <td className="py-2 px-4 border-b text-center">{administradorActual.area_Trabajo}</td>
                      <td className="py-2 px-4 border-b text-center">{administradorActual.estado_cuenta}</td>
                    </tr>
                  ) : (
                    <tr>
                      <td colSpan="8" className="py-2 px-4 border-b text-center">No se encontro informacion del administrador actual.</td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </motion.div>
        </div>
        <div className="grid grid-cols-1 gap-4">
          {/* Recuadro - Lista de administradores */}
          <motion.div
            initial={{ x: -100, opacity: 0 }}
            animate={{ x: 0, opacity: 1, transition: { delay: 0.8 } }}
            className="w-full bg-white rounded-lg p-4 shadow-lg"
          >
            <div className="shadow-lg rounded-lg p-4 bg-gray-900">
              <center>
                <h2 className="font-bold text-white">
                  <i className="align-middle fi fi-sr-document"></i> Lista de Administradores
                </h2>
              </center>
            </div>
            <div className="flex justify-end mt-4">
              <button onClick={manejarClickAñadirAdministrador} className="bg-green-500 text-white px-4 py-2 rounded">Añadir Administrador</button>
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
                    <th className="py-2 px-4 border-b text-center">Area de Trabajo</th>
                    <th className="py-2 px-4 border-b text-center">Estado de Cuenta</th>
                    <th className="py-2 px-4 border-b text-center">Accion</th>
                  </tr>
                </thead>
                <tbody>
                  {listaAdministradores.length > 0 ? (
                    listaAdministradores.map((administrador, index) => (
                      <tr key={administrador.id_empleado} className={index % 2 === 0 ? "bg-gray-100" : "bg-gray-200"}>
                        <td className="py-2 px-4 border-b text-center">{administrador.id_empleado}</td>
                        <td className="py-2 px-4 border-b text-center">{administrador.nombre}</td>
                        <td className="py-2 px-4 border-b text-center">{administrador.apellido_paterno}</td>
                        <td className="py-2 px-4 border-b text-center">{administrador.apellido_materno}</td>
                        <td className="py-2 px-4 border-b text-center">{administrador.contacto_correo}</td>
                        <td className="py-2 px-4 border-b text-center">{administrador.contacto_telefono}</td>
                        <td className="py-2 px-4 border-b text-center">{administrador.area_Trabajo}</td>
                        <td className="py-2 px-4 border-b text-center">{administrador.estado_cuenta}</td>
                        <td className="py-2 px-4 border-b text-center">
                          <button onClick={() => manejarClickModificar(administrador)} className="bg-blue-500 text-white px-2 py-1 rounded mr-2">Modificar</button>
                          <button onClick={() => manejarDarDeBaja(administrador.id_empleado)} className="bg-red-500 text-white px-2 py-1 rounded">Dar de Baja</button>
                        </td>
                      </tr>
                    ))
                  ) : (
                    <tr>
                      <td colSpan="9" className="py-2 px-4 border-b text-center">No se encontraron administradores.</td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </motion.div>
        </div>
      </div>

      {/* Formulario para poder modificar o añadir administradores */}
      {(administradorParaEditar || administradorParaAñadir) && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-lg shadow-lg p-4 w-full max-w-md md:max-w-lg max-h-[90vh] overflow-y-auto">
            <h2 className="text-2xl font-bold mb-4 text-center">{administradorParaEditar ? "Modificar Administrador" : "Añadir Administrador"}</h2>
            <form>
              <div className="grid grid-cols-1 gap-4">
                <label>Nombre</label>
                <input
                  type="text"
                  name="nombre"
                  value={administradorParaEditar ? administradorParaEditar.nombre : administradorParaAñadir.nombre}
                  onChange={manejarCambioEntrada}
                  placeholder="Nombre"
                  className="p-2 border rounded"
                />
                <label>Apellido Paterno</label>
                <input
                  type="text"
                  name="apellido_paterno"
                  value={administradorParaEditar ? administradorParaEditar.apellido_paterno : administradorParaAñadir.apellido_paterno}
                  onChange={manejarCambioEntrada}
                  placeholder="Apellido Paterno"
                  className="p-2 border rounded"
                />
                <label>Apellido Materno</label>
                <input
                  type="text"
                  name="apellido_materno"
                  value={administradorParaEditar ? administradorParaEditar.apellido_materno : administradorParaAñadir.apellido_materno}
                  onChange={manejarCambioEntrada}
                  placeholder="Apellido Materno"
                  className="p-2 border rounded"
                />
                <label>Fecha de Nacimiento</label>
                <input
                  type="date"
                  name="fecha_nacimiento"
                  value={administradorParaEditar ? administradorParaEditar.fecha_nacimiento : administradorParaAñadir.fecha_nacimiento}
                  onChange={manejarCambioEntrada}
                  className="p-2 border rounded"
                />
                <label>Genero</label>
                <select
                  name="genero"
                  value={administradorParaEditar ? administradorParaEditar.genero : administradorParaAñadir.genero}
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
                  value={administradorParaEditar ? administradorParaEditar.direccion_calle : administradorParaAñadir.direccion_calle}
                  onChange={manejarCambioEntrada}
                  placeholder="Calle"
                  className="p-2 border rounded"
                />
                <label>Colonia</label>
                <input
                  type="text"
                  name="direccion_colonia"
                  value={administradorParaEditar ? administradorParaEditar.direccion_colonia : administradorParaAñadir.direccion_colonia}
                  onChange={manejarCambioEntrada}
                  placeholder="Colonia"
                  className="p-2 border rounded"
                />
                <label>Codigo Postal</label>
                <input
                  type="text"
                  name="direccion_codigopostal"
                  value={administradorParaEditar ? administradorParaEditar.direccion_codigopostal : administradorParaAñadir.direccion_codigopostal}
                  onChange={manejarCambioEntrada}
                  placeholder="Codigo Postal"
                  className="p-2 border rounded"
                />
                <label>Estado</label>
                <input
                  type="text"
                  name="direccion_estado"
                  value={administradorParaEditar ? administradorParaEditar.direccion_estado : administradorParaAñadir.direccion_estado}
                  onChange={manejarCambioEntrada}
                  placeholder="Estado"
                  className="p-2 border rounded"
                />
                <label>Municipio</label>
                <input
                  type="text"
                  name="direccion_municipio"
                  value={administradorParaEditar ? administradorParaEditar.direccion_municipio : administradorParaAñadir.direccion_municipio}
                  onChange={manejarCambioEntrada}
                  placeholder="Municipio"
                  className="p-2 border rounded"
                />
                <label>Correo Electronico</label>
                <input
                  type="email"
                  name="contacto_correo"
                  value={administradorParaEditar ? administradorParaEditar.contacto_correo : administradorParaAñadir.contacto_correo}
                  onChange={manejarCambioEntrada}
                  placeholder="Correo Electronico"
                  className="p-2 border rounded"
                />
                <label>Contraseña</label>
                <input
                  type="password"
                  name="contraseña"
                  value={administradorParaEditar ? administradorParaEditar.contraseña : administradorParaAñadir.contraseña}
                  onChange={manejarCambioEntrada}
                  placeholder="Contraseña"
                  className="p-2 border rounded"
                />
                <label>Telefono</label>
                <input
                  type="text"
                  name="contacto_telefono"
                  value={administradorParaEditar ? administradorParaEditar.contacto_telefono : administradorParaAñadir.contacto_telefono}
                  onChange={manejarCambioEntrada}
                  placeholder="Telefono"
                  className="p-2 border rounded"
                />
                <label>Area de Trabajo</label>
                <select
                  name="area_Trabajo"
                  value={administradorParaEditar ? administradorParaEditar.area_Trabajo : administradorParaAñadir.area_Trabajo}
                  onChange={manejarCambioEntrada}
                  className="p-2 border rounded"
                >
                  <option value="">Seleccione</option>
                  <option value="Almacen">Almacen</option>
                  <option value="Administracion">Administracion</option>
                  <option value="Clientes">Clientes</option>
                  <option value="DBA">DBA</option>
                  <option value="Fidelizacion">Fidelizacion</option>
                  <option value="Reabastecimiento">Reabastecimiento</option>
                  <option value="Ventas">Ventas</option>
                  <option value="Servicio al cliente">Servicio al cliente</option>
                </select>
              </div>
              <div className="flex justify-center mt-4">
                <button type="button" onClick={administradorParaEditar ? manejarConfirmarCambios : manejarConfirmarAñadir} className="bg-green-500 text-white px-4 py-2 rounded">
                  Confirmar {administradorParaEditar ? "Cambios" : ""}
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setAdministradorParaEditar(null);
                    setAdministradorParaAñadir(null);
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
