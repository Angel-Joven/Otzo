from src.models.atencion.atencionModels import QuejasModelo, SugerenciasModelo

from src.db import get_connection

class QuejasService(QuejasModelo):
    def __init__(
        self, 
        id_cliente: int, 
        id_trabajador: int, 
        descripcion: str
    ):
        self.id_cliente = id_cliente
        self.id_trabajador = id_trabajador
        self.descripcion = descripcion

    def crearQueja(self):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO quejas (id_cliente, id_trabajador, descripcion) VALUES (%s, %s, %s)",
                (self.id_cliente, self.id_trabajador, self.descripcion),
            )
            connection.commit()
        connection.close()

    def actualizarEstado(self, id_queja: int):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE quejas SET estado = 'Resuelta' WHERE id_queja = (%s)",
                (id_queja),
            )
            connection.commit()
        connection.close()

class SugerenciasService(SugerenciasModelo):
    def __init__(
        self, 
        id_cliente: int, 
        id_trabajador: int, 
        descripcion: str
    ):
        self.id_cliente = id_cliente
        self.id_trabajador = id_trabajador
        self.descripcion = descripcion

    def crearSugerencia(self):
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
        connection.close()