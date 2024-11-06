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
            #Validamos si el cliente existe en la tabla de puntos
            cursor.execute("SELECT COUNT(*) FROM puntos WHERE idclientes_puntos = %s", (id_cliente,))
            cliente_existe = cursor.fetchone()[0] > 0

            if not cliente_existe:
                connection.close()
                raise ValueError("Cliente no encontrado para añadir puntos de compra.")

            cursor.execute(
                "UPDATE puntos SET total_puntos = total_puntos + %s WHERE idclientes_puntos = %s",
                (puntos_compra, id_cliente),
            )
            connection.commit()
        connection.close()
    
    def añadir_puntos_devolucion(self, id_cliente, puntos_devolucion):
        connection = get_connection()
        with connection.cursor() as cursor:
            # Validamos si el cliente existe en la tabla de puntos
            cursor.execute("SELECT COUNT(*) FROM puntos WHERE idclientes_puntos = %s", (id_cliente,))
            cliente_existe = cursor.fetchone()[0] > 0

            if not cliente_existe:
                connection.close()
                raise ValueError("Cliente no encontrado para añadir puntos de devolución.")

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
                    "mensaje": f"Puntos Insuficientes (Puntos actuales: {puntos_totales}).",
                }
            
# ---------------------------------------------------------------------------------------------------------------------------

class RangosService(RangosModelo):

    def asignarRangoInicialAuto(self):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                #Obtenemos todos los usuarios de la tabla clientes que no tienen un registro en la tabla puntos
                cursor.execute(
                    """
                    INSERT INTO puntos (idclientes_puntos, idrango, total_puntos)
                    SELECT idCliente, 1, 0
                    FROM clientes
                    WHERE idCliente NOT IN (SELECT idclientes_puntos FROM puntos) AND Estado = 'Activo'
                    """
                )
                connection.commit()
                return {"mensaje": "Rango 1 asignado a todos los usuarios sin rango y que sus cuentas esten activos"}
        except Exception as e:
            raise Exception(f"Error al asignar el rango 1 a usuarios sin rango: {str(e)}")
        finally:
            connection.close()

    def actualizarRangoPorHistorialCompras(self, id_cliente):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                #Obtenemos la cantidad total de compras del cliente
                cursor.execute(
                    "SELECT COUNT(*) FROM ventas WHERE id_cliente = %s", (id_cliente,)
                )
                compras_totales = cursor.fetchone()[0]

                #Determinamos el nuevo rango en funcion con su numero total de compras
                if compras_totales >= 25:
                    nuevo_rango = 6
                elif compras_totales >= 20:
                    nuevo_rango = 5
                elif compras_totales >= 15:
                    nuevo_rango = 4
                elif compras_totales >= 10:
                    nuevo_rango = 3
                elif compras_totales >= 5:
                    nuevo_rango = 2
                else:
                    nuevo_rango = 1

                #Obtenemos el rango actual del cliente
                cursor.execute(
                    "SELECT idrango FROM puntos WHERE idclientes_puntos = %s", (id_cliente,)
                )
                rango_actual = cursor.fetchone()[0]

                #Actualizamos el rango si el nuevo rango es mayor que el actual
                if nuevo_rango > rango_actual:
                    cursor.execute(
                        "UPDATE puntos SET idrango = %s WHERE idclientes_puntos = %s",
                        (nuevo_rango, id_cliente)
                    )
                    connection.commit()
                    return {
                        "mensaje": f"Rango actualizado a {nuevo_rango} después de {compras_totales} compras.",
                        "nuevo_rango": nuevo_rango,
                    }
                else:
                    return {"mensaje": "El cliente ya tiene el rango adecuado para su numero de compras."}

        except Exception as e:
            print("Error al actualizar el rango:", e)
            return {"mensaje": "Error al actualizar el rango", "error": str(e)}
        finally:
            connection.close()

    def obtener_rango_cliente(self, id_cliente):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT idrango FROM puntos WHERE idclientes_puntos = %s", (id_cliente,)
                )
                resultado = cursor.fetchone()

                if resultado:
                    return {"rango": resultado[0]}
                else:
                    return {"mensaje": "Cliente no encontrado"}
        finally:
            connection.close()

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
            raise ValueError("Rango no encontrado.")

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
            raise ValueError("Rango no encontrado.")

# ---------------------------------------------------------------------------------------------------------------------------