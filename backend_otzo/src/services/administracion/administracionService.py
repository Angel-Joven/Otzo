# Servicios para el Modulo de Administracion
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from src.models.administracion.administracionModels import *
from src.db import get_connection
from pymysql import DatabaseError
import json

# ---------------------------------------------------------------------------------------------------------------------------

class AdministracionService(AdministracionModelo):
    @staticmethod
    def altaAdministrador(data):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    """
                    INSERT INTO administracion (
                        nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero,
                        direccion_calle, direccion_colonia, direccion_codigopostal, direccion_estado,
                        direccion_municipio, contacto_correo, contraseña, contacto_telefono,
                        area_Trabajo, fechaDe_Alta, estado_cuenta
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), 'Activo')
                    """,
                    (
                        data['nombre'], data['apellido_paterno'], data['apellido_materno'], 
                        data['fecha_nacimiento'], data['genero'], data['direccion_calle'], 
                        data['direccion_colonia'], data['direccion_codigopostal'], data['direccion_estado'], 
                        data['direccion_municipio'], data['contacto_correo'], data['contraseña'], 
                        data['contacto_telefono'], data['area_Trabajo']
                    )
                )
                #Confirmamos la transaccion
                conexion.commit()
            return {"mensaje": "Administrador creado exitosamente"}
        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

    @staticmethod
    def bajaAdministrador(id_empleado):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    "UPDATE administracion SET estado_cuenta = 'Inactivo' WHERE id_empleado = %s",
                    (id_empleado,)
                )
                #Confirmamos la transaccion
                conexion.commit()
            return {"mensaje": "Administrador dado de baja satisfactoriamente"}
        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

    @staticmethod
    def suspenderAdministrador(id_empleado):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    "UPDATE administracion SET estado_cuenta = 'Suspendido' WHERE id_empleado = %s",
                    (id_empleado,)
                )
                #Confirmamos la transaccion
                conexion.commit()
            return {"mensaje": "Administrador suspendido"}
        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()
    
    @staticmethod
    def banearAdministrador(id_empleado):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    "UPDATE administracion SET estado_cuenta = 'Baneado' WHERE id_empleado = %s",
                    (id_empleado,)
                )
                #Confirmamos la transaccion
                conexion.commit()
            return {"mensaje": "Administrador Baneado"}
        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

    @staticmethod
    def modificarAdministrador(id_empleado, data):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    """
                    UPDATE administracion
                    SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, fecha_nacimiento = %s, genero = %s,
                        direccion_calle = %s, direccion_colonia = %s, direccion_codigopostal = %s, direccion_estado = %s,
                        direccion_municipio = %s, contacto_correo = %s, contraseña = %s, contacto_telefono = %s,
                        area_Trabajo = %s WHERE id_empleado = %s
                    """,
                    (
                        data['nombre'], data['apellido_paterno'], data['apellido_materno'], 
                        data['fecha_nacimiento'], data['genero'], data['direccion_calle'], 
                        data['direccion_colonia'], data['direccion_codigopostal'], data['direccion_estado'], 
                        data['direccion_municipio'], data['contacto_correo'], data['contraseña'], 
                        data['contacto_telefono'], data['area_Trabajo'], id_empleado
                    )
                )
                #Confirmamos la transaccion
                conexion.commit()
            return {"mensaje": "Administrador modificado exitosamente"}
        except Exception as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise DatabaseError(str(e))
        finally:
            conexion.close()

    @staticmethod
    def devolverAdministradorSesionActual(id_empleado):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    """
                    SELECT id_empleado, nombre, apellido_paterno, apellido_materno,
                        contacto_correo, contacto_telefono, area_Trabajo, estado_cuenta
                    FROM administracion
                    WHERE id_empleado = %s
                    """,
                    (id_empleado,)
                )
                #Confirmamos la transaccion
                conexion.commit()
                administrador = cursor.fetchone()

            if not administrador:
                resultado = {"error": "No se encontró el administrador actual"}
            else:
                resultado = {
                    "id_empleado": administrador[0],
                    "nombre": administrador[1],
                    "apellido_paterno": administrador[2],
                    "apellido_materno": administrador[3],
                    "contacto_correo": administrador[4],
                    "contacto_telefono": administrador[5],
                    "area_Trabajo": administrador[6],
                    "estado_cuenta": administrador[7],
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
    def devolverAdministrador(id_empleado):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    """
                    SELECT id_empleado, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, direccion_calle,
                        direccion_colonia, direccion_codigopostal, direccion_estado, direccion_municipio, contacto_correo,
                        contraseña, contacto_telefono, area_Trabajo, fechaDe_Alta, ultimo_acceso, estado_cuenta
                    FROM administracion
                    WHERE id_empleado = %s
                    """,
                    (id_empleado,)
                )
                #Confirmamos la transaccion
                conexion.commit()
                administrador = cursor.fetchone()

            if not administrador:
                resultado = {"error": "No se encontró el administrador con el ID proporcionado"}
            else:
                resultado = {
                    "id_empleado": administrador[0],
                    "nombre": administrador[1],
                    "apellido_paterno": administrador[2],
                    "apellido_materno": administrador[3],
                    "fecha_nacimiento": str(administrador[4]),
                    "genero": administrador[5],
                    "direccion_calle": administrador[6],
                    "direccion_colonia": administrador[7],
                    "direccion_codigopostal": administrador[8],
                    "direccion_estado": administrador[9],
                    "direccion_municipio": administrador[10],
                    "contacto_correo": administrador[11],
                    "contraseña": administrador[12],
                    "contacto_telefono": administrador[13],
                    "area_Trabajo": administrador[14],
                    "fechaDe_Alta": str(administrador[15]),
                    "ultimo_acceso": str(administrador[16]),
                    "estado_cuenta": administrador[17],
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
    def devolverListaAdministradores():
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                cursor.execute(
                    """
                    SELECT id_empleado, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, direccion_calle,
                        direccion_colonia, direccion_codigopostal, direccion_estado, direccion_municipio, contacto_correo,
                        contraseña, contacto_telefono, area_Trabajo, fechaDe_Alta, ultimo_acceso, estado_cuenta
                    FROM administracion
                    """
                )
                #Confirmamos la transaccion
                conexion.commit()
                administradores = cursor.fetchall()

            if not administradores:
                resultado = {"error": "No se encontraron los administradores"}
            else:
                administradores_lista = []
                for admin in administradores:
                    administradores_lista.append({
                        "id_empleado": admin[0],
                        "nombre": admin[1],
                        "apellido_paterno": admin[2],
                        "apellido_materno": admin[3],
                        "fecha_nacimiento": str(admin[4]),
                        "genero": admin[5],
                        "direccion_calle": admin[6],
                        "direccion_colonia": admin[7],
                        "direccion_codigopostal": admin[8],
                        "direccion_estado": admin[9],
                        "direccion_municipio": admin[10],
                        "contacto_correo": admin[11],
                        "contraseña": admin[12],
                        "contacto_telefono": admin[13],
                        "area_Trabajo": admin[14],
                        "fechaDe_Alta": str(admin[15]),
                        "ultimo_acceso": str(admin[16]),
                        "estado_cuenta": admin[17],
                    })
                resultado = administradores_lista

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
# FUNCIONALIDAD QUE DEVUELVE INFORMACION DE LOS ADMINISTRADORES

# REQUISITOS
# id_empleado

# ESE REQUISITO ES NECESARIO PARA QUE FUNCIONEN LOS SIGUIENTES SERVICIOS:

# AdministracionService.devolverAdministradorSesionActual(id_empleado)
# AdministracionService.devolverAdministrador(id_empleado)
# AdministracionService.devolverListaAdministradores()

# ----------------------

# EJEMPLO DE USO 1 - OBTENER INFO DEL ADMINISTRADOR QUE INICIO SESION
# PARA PODER VISUALIZAR LA INFORMACION, ES NECESARIO INGRESAR O TENER ALMACENADO LA INFORMACION
# DEL 'id_empleado' y de UsarAutenticadorNombre() PARA PASARLO A ESTE SERVICIO.
# Mas informacion en \Otzo\frontend_otzo\src\context\Autenticacion.jsx y en
# \Otzo\frontend_otzo\src\pages\Administracion.jsx

# LA ESTRUCTURA ES LA SIGUIENTE:
# AdministracionService.devolverAdministradorSesionActual(id_empleado)

# ----------------------

# EJEMPLO DE USO 2 - OBTENER INFO DE UN ADMINISTRADOR EN CONCRETO EN BASE AL ID EMPLEADO
# PARA PODER VISUALIZAR LA INFORMACION, ES NECESARIO INGRESAR O TENER ALMACENADO LA INFORMACION
# DEL 'id_empleado' PARA PASARLO A ESTE SERVICIO.

# LA ESTRUCTURA ES LA SIGUIENTE:
# AdministracionService.devolverAdministrador(id_empleado)

# ----------------------

# EJEMPLO DE USO 3 - OBTENER INFO DE TODOS LOS ADMINISTRADORES ALMACENADOS EN LA BD
# PARA PODER VISUALIZAR LA INFORMACION, SOLAMENTE ES NECESARIO MANDAR A LLAMAR A ESTE SERVICIO.
# NO REQUIERE DE MANDARLE VARIABLES NI NADA

# LA ESTRUCTURA ES LA SIGUIENTE:
# AdministracionService.devolverListaAdministradores()

# ---------------------------------------------------------------------------------------------------------------------------
