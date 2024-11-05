from src.models.fidelizacion.fidelizacionModels import PuntosModelo, RangosModelo
from src.db import get_connection

# ---------------------------------------------------------------------------------------------------------------------------

class PuntosService(PuntosModelo):
    def calcular_puntos_compra(self, id_cliente, idrango, precio_compra_total, porcentaje_compra_puntos):
        puntos_obtenidos = (precio_compra_total * porcentaje_compra_puntos) / 100
        return round(puntos_obtenidos)

    def calcular_puntos_devolucion(self, id_cliente, idrango, precio_producto, porcentaje_devolucion_puntos):
        puntos_devolucion = (precio_producto * porcentaje_devolucion_puntos) / 100
        return round(puntos_devolucion)

    def añadir_puntos_compra(self, id_cliente, puntos_compra):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE puntos SET total_puntos = total_puntos + %s WHERE idclientes_puntos = %s",
                (puntos_compra, id_cliente),
            )
            connection.commit()
        connection.close()
    
    def añadir_puntos_devolucion(self, id_cliente, puntos_devolucion):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE puntos SET total_puntos = total_puntos + %s WHERE idclientes_puntos = %s",
                (puntos_devolucion, id_cliente),
            )
            connection.commit()
        connection.close()

    def descontar_puntos(self, id_cliente, precio_compra_total):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT total_puntos FROM puntos WHERE idclientes_puntos = %s", (id_cliente,)
            )
            resultado = cursor.fetchone()

            if not resultado:
                connection.close()
                return {"exito": False, "mensaje": "Cliente no encontrado."}

            puntos_totales = resultado[0]
            if puntos_totales >= precio_compra_total:
                puntos_restantes = puntos_totales - precio_compra_total
                cursor.execute(
                    "UPDATE puntos SET total_puntos = %s WHERE idclientes_puntos = %s",
                    (puntos_restantes, id_cliente),
                )
                connection.commit()
                connection.close()
                return {"exito": True, "puntos_restantes": puntos_restantes}
            else:
                connection.close()
                return {
                    "exito": False,
                    "mensaje": f"Puntos Insuficientes (actual: {puntos_totales}).",
                }

# ---------------------------------------------------------------------------------------------------------------------------

class RangosService(RangosModelo):
    def obtener_porcentaje_compra(self, idrango):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT porcentaje_puntos FROM rangos WHERE idrango = %s", (idrango,)
            )
            resultado = cursor.fetchone()
        connection.close()
        
        if resultado:
            return resultado[0]
        else:
            return None

    def obtener_porcentaje_devolucion(self, idrango):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT porcentaje_devolucionPuntos FROM rangos WHERE idrango = %s", (idrango,)
            )
            resultado = cursor.fetchone()
        connection.close()
        
        if resultado:
            return resultado[0]
        else:
            return None

# ---------------------------------------------------------------------------------------------------------------------------