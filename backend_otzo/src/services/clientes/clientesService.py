# Servicios para el Modulo de Clientes
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from src.models.clientes.clientesModels import ClientesModelo
from src.db import get_connection
from pymysql import DatabaseError
import json

# ---------------------------------------------------------------------------------------------------------------------------

class ClientesService(ClientesModelo):
    @staticmethod
    def altaCliente(data):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    """
                    INSERT INTO clientes (
                        nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero,
                        direccion_calle, direccion_colonia, direccion_codigopostal, direccion_estado,
                        direccion_municipio, contacto_correo, contraseña, contacto_telefono,
                        fechaDe_Alta, estado_cuenta
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), 'Activo')
                    """,
                    (
                        data['nombre'], data['apellido_paterno'], data['apellido_materno'],
                        data['fecha_nacimiento'], data['genero'], data['direccion_calle'],
                        data['direccion_colonia'], data['direccion_codigopostal'], data['direccion_estado'],
                        data['direccion_municipio'], data['contacto_correo'], data['contraseña'],
                        data['contacto_telefono']
                    )
                )
                #Confirmamos la transaccion
                conexion.commit()
            return {"mensaje": "Cliente creado exitosamente"}
        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

    @staticmethod
    def bajaCliente(id_cliente):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    "UPDATE clientes SET estado_cuenta = 'Inactivo' WHERE idCliente = %s",
                    (id_cliente,)
                )
                #Confirmamos la transaccion
                conexion.commit()
            return {"mensaje": "Cliente dado de baja satisfactoriamente"}
        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

    @staticmethod
    def suspenderCliente(id_cliente):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    "UPDATE clientes SET estado_cuenta = 'Suspendido' WHERE idCliente = %s",
                    (id_cliente,)
                )
                #Confirmamos la transaccion
                conexion.commit()
            return {"mensaje": "Cliente suspendido"}
        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

    @staticmethod
    def modificarCliente(id_cliente, data):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    """
                    UPDATE clientes
                    SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, fecha_nacimiento = %s, genero = %s,
                        direccion_calle = %s, direccion_colonia = %s, direccion_codigopostal = %s, direccion_estado = %s,
                        direccion_municipio = %s, contacto_correo = %s, contraseña = %s, contacto_telefono = %s
                    WHERE idCliente = %s
                    """,
                    (
                        data['nombre'], data['apellido_paterno'], data['apellido_materno'],
                        data['fecha_nacimiento'], data['genero'], data['direccion_calle'],
                        data['direccion_colonia'], data['direccion_codigopostal'], data['direccion_estado'],
                        data['direccion_municipio'], data['contacto_correo'], data['contraseña'],
                        data['contacto_telefono'], id_cliente
                    )
                )
                #Confirmamos la transaccion
                conexion.commit()
            return {"mensaje": "Cliente modificado exitosamente"}
        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

    @staticmethod
    def devolverClienteSesionActual(id_cliente):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    """
                    SELECT idCliente, nombre, apellido_paterno, apellido_materno,
                        contacto_correo, contacto_telefono, estado_cuenta
                    FROM clientes
                    WHERE idCliente = %s
                    """,
                    (id_cliente,)
                )
                #Confirmamos la transaccion
                conexion.commit()
                cliente = cursor.fetchone()

            if not cliente:
                resultado = {"error": "No se encontro el cliente actual"}
            else:
                resultado = {
                    "idCliente": cliente[0],
                    "nombre": cliente[1],
                    "apellido_paterno": cliente[2],
                    "apellido_materno": cliente[3],
                    "contacto_correo": cliente[4],
                    "contacto_telefono": cliente[5],
                    "estado_cuenta": cliente[6],
                }

            print(json.dumps(resultado, indent=4, ensure_ascii=False))
            return resultado

        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

    @staticmethod
    def devolverCliente(id_cliente):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    """
                    SELECT idCliente, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, direccion_calle,
                        direccion_colonia, direccion_codigopostal, direccion_estado, direccion_municipio, contacto_correo,
                        contraseña, contacto_telefono, fechaDe_Alta, ultimo_acceso, estado_cuenta
                    FROM clientes
                    WHERE idCliente = %s
                    """,
                    (id_cliente,)
                )
                #Confirmamos la transaccion
                conexion.commit()
                cliente = cursor.fetchone()

            if not cliente:
                resultado = {"error": "No se encontro el cliente con el ID proporcionado"}
            else:
                resultado = {
                    "idCliente": cliente[0],
                    "nombre": cliente[1],
                    "apellido_paterno": cliente[2],
                    "apellido_materno": cliente[3],
                    "fecha_nacimiento": str(cliente[4]),
                    "genero": cliente[5],
                    "direccion_calle": cliente[6],
                    "direccion_colonia": cliente[7],
                    "direccion_codigopostal": cliente[8],
                    "direccion_estado": cliente[9],
                    "direccion_municipio": cliente[10],
                    "contacto_correo": cliente[11],
                    "contraseña": cliente[12],
                    "contacto_telefono": cliente[13],
                    "fechaDe_Alta": str(cliente[14]),
                    "ultimo_acceso": str(cliente[15]),
                    "estado_cuenta": cliente[16],
                }

            print(json.dumps(resultado, indent=4, ensure_ascii=False))
            return resultado

        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

    @staticmethod
    def devolverListaClientes():
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    """
                    SELECT idCliente, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, direccion_calle,
                        direccion_colonia, direccion_codigopostal, direccion_estado, direccion_municipio, contacto_correo,
                        contraseña, contacto_telefono, fechaDe_Alta, ultimo_acceso, estado_cuenta
                    FROM clientes
                    """
                )
                #Confirmamos la transaccion
                conexion.commit()
                clientes = cursor.fetchall()

            if not clientes:
                resultado = {"error": "No se encontraron clientes"}
            else:
                clientes_lista = []
                for cli in clientes:
                    clientes_lista.append({
                        "idCliente": cli[0],
                        "nombre": cli[1],
                        "apellido_paterno": cli[2],
                        "apellido_materno": cli[3],
                        "fecha_nacimiento": str(cli[4]),
                        "genero": cli[5],
                        "direccion_calle": cli[6],
                        "direccion_colonia": cli[7],
                        "direccion_codigopostal": cli[8],
                        "direccion_estado": cli[9],
                        "direccion_municipio": cli[10],
                        "contacto_correo": cli[11],
                        "contraseña": cli[12],
                        "contacto_telefono": cli[13],
                        "fechaDe_Alta": str(cli[14]),
                        "ultimo_acceso": str(cli[15]),
                        "estado_cuenta": cli[16],
                    })
                resultado = clientes_lista

            print(json.dumps(resultado, indent=4, ensure_ascii=False))
            return resultado

        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

# -> ¡PARA TODOS LOS MODULOS! <-
# FUNCIONALIDADES QUE DEVUELVEN INFORMACION DE LOS CLIENTES DEPENDIENDO DEL CASO

# REQUISITOS
# id_cliente

# ESE REQUISITO ES NECESARIO PARA QUE FUNCIONEN LOS SIGUIENTES SERVICIOS:

# ClientesService.devolverClienteSesionActual(id_cliente)
# ClientesService.devolverCliente(id_cliente)
# ClientesService.devolverListaClientes()

# ----------------------

# EJEMPLO DE USO 1 - OBTENER INFO DEL CLIENTE QUE INICIO SESION
# PARA PODER VISUALIZAR LA INFORMACION, ES NECESARIO INGRESAR O TENER ALMACENADO LA INFORMACION
# DEL 'id_cliente' y de UsarAutenticadorNombre() PARA PASARLO A ESTE SERVICIO.
# Mas informacion en \Otzo\frontend_otzo\src\context\Autenticacion.jsx y en
# \Otzo\frontend_otzo\src\pages\Clientes.jsx o \Otzo\frontend_otzo\src\pages\ClientesAdministracion.jsx

# LA ESTRUCTURA ES LA SIGUIENTE:
# ClientesService.devolverClienteSesionActual(id_cliente)

# ----------------------

# EJEMPLO DE USO 2 - OBTENER INFO DE UN CLIENTE EN CONCRETO EN BASE AL ID CLIENTE
# PARA PODER VISUALIZAR LA INFORMACION, ES NECESARIO INGRESAR O TENER ALMACENADO LA INFORMACION
# DEL 'id_cliente' PARA PASARLO A ESTE SERVICIO.

# LA ESTRUCTURA ES LA SIGUIENTE:
# ClientesService.devolverCliente(id_cliente)

# ----------------------

# EJEMPLO DE USO 3 - OBTENER INFO DE TODOS LOS CLIENTES ALMACENADOS EN LA BD
# PARA PODER VISUALIZAR LA INFORMACION, SOLAMENTE ES NECESARIO MANDAR A LLAMAR A ESTE SERVICIO.
# NO REQUIERE DE MANDARLE VARIABLES NI NADA

# LA ESTRUCTURA ES LA SIGUIENTE:
# ClientesService.devolverListaClientes()

# ---------------------------------------------------------------------------------------------------------------------------
