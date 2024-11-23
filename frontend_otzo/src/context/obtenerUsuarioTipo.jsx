/*

Contexto para saber que tipo de usuario se logeo en el Login de Clientes y/o Administradores
Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

Temas Especiales de Programacion 2 | 1061

*/

import { useEffect, useState } from "react";
import axios from "axios";

export function ObtenerTipoUsuario() {
  const [clienteActual, setClienteActual] = useState(null);
  const [idCliente, setIdCliente] = useState(null);
  const [administradorActual, setAdministradorActual] = useState(null);
  const [idEmpleado, setIdEmpleado] = useState(null);

  useEffect(() => {
    const administradorAlmacenado = localStorage.getItem("administrador");
    if (administradorAlmacenado && administradorAlmacenado !== "undefined") {
      try {
        const administradorParseado = JSON.parse(administradorAlmacenado);
        if (administradorParseado?.id_empleado) {
          setIdEmpleado(administradorParseado.id_empleado);
        }
      } catch (error) {
        console.error("Error al parsear el administrador del localStorage:", error);
      }
    }
  }, []);

  useEffect(() => {
    if (idEmpleado) {
      axios
        .get(`http://localhost:5000/api/administracion/sesionactualadmin/${idEmpleado}`)
        .then((respuesta) => {
          if (respuesta.data && !respuesta.data.error) {
            setAdministradorActual(respuesta.data);
          } else {
            console.error("Error en la respuesta del servidor:", respuesta.data);
          }
        })
        .catch((error) => {
          console.error("Error al obtener el administrador actual:", error);
        });
    }
  }, [idEmpleado]);

  useEffect(() => {
    const clienteAlmacenado = localStorage.getItem("cliente");
    if (clienteAlmacenado && clienteAlmacenado !== "undefined") {
      try {
        const clienteParseado = JSON.parse(clienteAlmacenado);
        if (clienteParseado?.idCliente) {
          setIdCliente(clienteParseado.idCliente);
        }
      } catch (error) {
        console.error("Error al parsear el cliente del localStorage:", error);
      }
    }
  }, []);

  useEffect(() => {
    if (idCliente) {
      axios.get(`http://localhost:5000/api/clientes/sesionactualcliente/${idCliente}`)
        .then(respuesta => {
          if (respuesta.data && !respuesta.data.error) {
            setClienteActual(respuesta.data);
          } else {
            console.error("Error en la respuesta del servidor:", respuesta.data);
          }
        })
        .catch(error => {
          console.error("Error al obtener el cliente actual:", error);
        });
      }
    }, [idCliente]);

  return { clienteActual, idCliente, administradorActual, idEmpleado };
}

/* 
----------------------

EJEMPLO DE USO:

//Si quieres tener la funcionalidad de poder obtener los datos del usuario que ha iniciado sesion, importa esto:
import { ObtenerTipoUsuario } from "../context/obtenerUsuarioTipo";

// Dentro de tu funcion principal, escribe esta linea:
const { clienteActual, idCliente, administradorActual, idEmpleado } = ObtenerTipoUsuario(); // Aqui mandamos a llamar a las variables que contienen la info del que inicio sesion.

----------------------

Retorno de variables:
- clienteActual : Sirve para almacenar los datos del cliente actual (Nombre, Apellido Paterno, Apellido Materno, etc.).
- idCliente : Sirve para almacenar el ID del cliente que ha iniciado sesion.
- administradorActual : Estado para almacenar los datos del administrador actual. (Nombre, Apellido Paterno, Apellido Materno, etc.).
- idEmpleado : Estado para almacenar el ID del administrador que ha iniciado sesion.

 */