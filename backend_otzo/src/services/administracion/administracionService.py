# Servicios para el Modulo de Administracion
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from src.models.administracion.administracionModels import *
from src.db import get_connection
from pymysql import DatabaseError

# ---------------------------------------------------------------------------------------------------------------------------

class AdministracionService(AdministracionModelo):
    def altaAdministrador(self, data):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
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
                connection.commit()
            return {"mensaje": "Administrador creado exitosamente"}
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            connection.close()

    def bajaAdministrador(self, id_empleado):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE administracion SET estado_cuenta = 'Inactivo' WHERE id_empleado = %s",
                    (id_empleado,)
                )
                connection.commit()
            return {"mensaje": "Administrador Inactivo"}
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            connection.close()
    
    def suspenderAdministrador(self, id_empleado):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE administracion SET estado_cuenta = 'Suspendido' WHERE id_empleado = %s",
                    (id_empleado,)
                )
                connection.commit()
            return {"mensaje": "Administrador suspendido"}
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            connection.close()
    
    def banearAdministrador(self, id_empleado):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE administracion SET estado_cuenta = 'Baneado' WHERE id_empleado = %s",
                    (id_empleado,)
                )
                connection.commit()
            return {"mensaje": "Administrador Baneado"}
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            connection.close()

    def modificarAdministrador(self, id_empleado, data):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE administracion
                    SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, 
                        contacto_correo = %s, contacto_telefono = %s
                    WHERE id_empleado = %s
                    """,
                    (
                        data['nombre'], data['apellido_paterno'], data['apellido_materno'], 
                        data['contacto_correo'], data['contacto_telefono'], id_empleado
                    )
                )
                connection.commit()
            return {"mensaje": "Administrador modificado exitosamente"}
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            connection.close()

    def devolverAdministradorSesionActual(self, id_empleado):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id_empleado, nombre, apellido_paterno, apellido_materno,
                           contacto_correo, contacto_telefono, area_Trabajo
                    FROM administracion
                    WHERE id_empleado = %s
                    """,
                    (id_empleado,)
                )
                administrador = cursor.fetchone()

            if not administrador:
                return {"error": "No se encontro el administrador actual"}

            return {
                "id_empleado": administrador[0],
                "nombre": administrador[1],
                "apellido_paterno": administrador[2],
                "apellido_materno": administrador[3],
                "contacto_correo": administrador[4],
                "contacto_telefono": administrador[5],
                "area_Trabajo": administrador[6],
            }
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            connection.close()
    
    def devolverAdministrador(self, id_empleado):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id_empleado, nombre, apellido_paterno, apellido_materno,
                           contacto_correo, contacto_telefono, area_Trabajo, estado_cuenta
                    FROM administracion
                    WHERE id_empleado = %s
                    """,
                    (id_empleado,)
                )
                administrador = cursor.fetchone()

            if not administrador:
                return {"error": "No se encontro el administrador con el ID proporcionado"}

            return {
                "id_empleado": administrador[0],
                "nombre": administrador[1],
                "apellido_paterno": administrador[2],
                "apellido_materno": administrador[3],
                "contacto_correo": administrador[4],
                "contacto_telefono": administrador[5],
                "area_Trabajo": administrador[6],
                "estado_cuenta": administrador[7],
            }
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            connection.close()