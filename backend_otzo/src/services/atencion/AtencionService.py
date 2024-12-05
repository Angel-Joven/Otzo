from src.models.atencion.atencionModels import QuejasModelo, SugerenciasModelo
from src.models.atencion.atencionDTO import QuejasDTO, SugerenciasDTO
from dataclasses import dataclass
from pymysql.cursors import DictCursor
from src.db import get_connection
from datetime import datetime


@dataclass
class QuejasService(QuejasModelo):

    def listarQuejasCliente(self, idCliente: int):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute("SELECT * FROM quejas WHERE id_Cliente = %s", idCliente)

            return cursor.fetchall()

        except Exception as e:
            print("No se pudo consultar las quejas, error:", e)
            conexion.rollback()
            return False
        finally:
            conexion.close()

    def listarQuejasPendientes(self):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute("SELECT * FROM quejas WHERE estado = 'Pendiente' OR estado = 'Activa'")

            return cursor.fetchall()

        except Exception as e:
            print("No se pudo consultar las quejas, error:", e)
            conexion.rollback()
            return False
        finally:
            conexion.close()

    def crearQueja(self, queja: QuejasDTO):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute(
                "INSERT INTO quejas (id_cliente, id_empleado, fechaHora, descripcion, categoria, estado, prioridad, comentarioSeguimiento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    queja.idCliente,
                    queja.idEmpleado,
                    datetime.now(),
                    queja.descripcion,
                    queja.categoria,
                    queja.estado,
                    queja.prioridad,
                    queja.comentarioSeguimiento,
                ),
            )

            conexion.commit()

            return True

        except Exception as e:
            print("No se pudo agregar la queja, error:", e)
            conexion.rollback()
            return False
        finally:
            conexion.close()

    def actualizarQueja(self, queja: QuejasDTO):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute(
                "UPDATE quejas SET estado = %s, comentarioSeguimiento = %s, id_empleado = %s WHERE idQueja = %s",
                (
                    queja.estado,
                    queja.comentarioSeguimiento,
                    queja.idEmpleado,
                    queja.idQueja,
                ),
            )

            conexion.commit()

            return True

        except Exception as e:
            print("No se pudo actualizar la queja, error:", e)
            conexion.rollback()
            return False
        finally:
            conexion.close()

@dataclass
class SugerenciasService(SugerenciasModelo):

    def crearSugerencia(self, sugerencia: SugerenciasDTO):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute(
                "INSERT INTO sugerencias (id_cliente, id_empleado, fechaHora, descripcion, categoria, estado, comentarioSeguimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    sugerencia.idCliente,
                    sugerencia.idEmpleado,
                    datetime.now(),
                    sugerencia.descripcion,
                    sugerencia.categoria,
                    sugerencia.estado,
                    sugerencia.comentarioSeguimiento,
                ),
            )

            conexion.commit()

            return True

        except Exception as e:
            print("No se pudo agregar la sugerencia, error:", e)
            conexion.rollback()
            return False
        finally:
            conexion.close()
    
    def actualizarEstado(self):
        pass

    """def crearSugerencia(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO sugerencias (id_cliente, id_trabajador, descripcion) VALUES (%s, %s, %s)",
                (self.id_cliente, self.id_trabajador, self.descripcion),
            )
            connection.commit()
        connection.close()

    def actualizarEstado(self, id_sugerencia: int):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE sugerencias SET estado = 'Resuelta' WHERE id_sugerencia = (%s)",
                (id_sugerencia),
            )
            connection.commit()
        connection.close()"""
