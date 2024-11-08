from src.models.fidelizacion.fidelizacionModels import PuntosModelo, RangosModelo
from src.db import get_connection
from pymysql import DatabaseError

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
        try:
            with connection.cursor() as cursor:
                #Comenzamos la transaccion
                connection.begin()

                #Validamos si el cliente existe en la tabla de puntos
                cursor.execute("SELECT COUNT(*) FROM puntos WHERE idclientes_puntos = %s", (id_cliente,))
                cliente_existe = cursor.fetchone()[0] > 0

                if not cliente_existe:
                    raise ValueError("La cuenta del cliente no fue encontrada para añadir sus puntos de compra.")

                cursor.execute(
                    "UPDATE puntos SET total_puntos = total_puntos + %s, ultima_actualizacionPuntos = NOW() WHERE idclientes_puntos = %s",
                    (puntos_compra, id_cliente),
                )
                #Confirmamos la transaccion
                connection.commit()
        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            connection.rollback()
            raise e
        finally:
            connection.close()

    def añadir_puntos_devolucion(self, id_cliente, puntos_devolucion):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                #Comenzamos la transaccion
                connection.begin()

                #Validamos si el cliente existe en la tabla de puntos
                cursor.execute("SELECT COUNT(*) FROM puntos WHERE idclientes_puntos = %s", (id_cliente,))
                cliente_existe = cursor.fetchone()[0] > 0

                if not cliente_existe:
                    raise ValueError("La cuenta del cliente no fue encontrada para añadir sus puntos de devolucion.")

                cursor.execute(
                    "UPDATE puntos SET total_puntos = total_puntos + %s, ultima_actualizacionPuntos = NOW() WHERE idclientes_puntos = %s",
                    (puntos_devolucion, id_cliente),
                )
                #Confirmamos la transaccion
                connection.commit()
        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            connection.rollback()
            raise e
        finally:
            connection.close()

    def descontar_puntos(self, id_cliente, precio_compra_total):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                #Comenzamos la transaccion
                connection.begin()

                #Validamos si el cliente existe
                cursor.execute(
                    "SELECT Estado FROM clientes WHERE idCliente = %s", (id_cliente,)
                )
                estado_cliente = cursor.fetchone()
                if not estado_cliente:
                    raise ValueError("La cuenta del cliente no fue encontrada para realizar el descuento de puntos.")
                elif estado_cliente[0] == 'Suspendido':
                    raise ValueError("La cuenta del cliente esta suspendida y no puede realizar operaciones de puntos.")
                elif estado_cliente[0] == 'Inactivo':
                    raise ValueError("La cuenta del cliente esta inactiva y no puede realizar operaciones de puntos.")

                #Obtenemos los puntos totales del cliente
                cursor.execute(
                    "SELECT total_puntos FROM puntos WHERE idclientes_puntos = %s", (id_cliente,)
                )
                resultado = cursor.fetchone()

                if not resultado:
                    raise ValueError("La cuenta del cliente no fue encontrada para realizar el descuento de puntos.")

                puntos_totales = resultado[0]
                if puntos_totales >= precio_compra_total:
                    puntos_restantes = puntos_totales - precio_compra_total
                    cursor.execute(
                        "UPDATE puntos SET total_puntos = %s, ultima_actualizacionPuntos = NOW() WHERE idclientes_puntos = %s",
                        (puntos_restantes, id_cliente),
                    )
                    #Confirmamos la transaccion
                    connection.commit()
                    return {
                        "exito": True,
                        "mensaje": f"Compra realizada con exito. Puntos Restantes: {puntos_restantes}.",
                        }
                else:
                    return {
                        "exito": False,
                        "mensaje": f"La compra no fue realizada con exito. Puntos Insuficientes. (Puntos actuales: {puntos_totales}).",
                    }
        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            connection.rollback()
            raise e
        finally:
            connection.close()
            
# ---------------------------------------------------------------------------------------------------------------------------

class RangosService(RangosModelo):

    def asignarRangoInicialAuto(self):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                #Comenzamos la transaccion
                connection.begin()

                #Obtenemos todos los usuarios de la tabla clientes que no tienen un registro en la tabla puntos
                cursor.execute(
                    """
                    INSERT INTO puntos (idclientes_puntos, idrango, total_puntos)
                    SELECT idCliente, 1, 0
                    FROM clientes
                    WHERE idCliente NOT IN (SELECT idclientes_puntos FROM puntos) AND Estado = 'Activo'
                    """
                )
                #Confirmamos la transaccion
                connection.commit()
                return {"mensaje": "Rango 1 asignado a todos los usuarios sin rango y que sus cuentas esten activas"}
        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            connection.rollback()
            raise e
        finally:
            connection.close()

    def actualizarRangoPorHistorialCompras(self, id_cliente):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                #Comenzamos la transaccion
                connection.begin()

                #Verificar si el cliente existe antes de proceder
                cursor.execute("SELECT Estado FROM clientes WHERE idCliente = %s", (id_cliente,))
                estado_cliente = cursor.fetchone()

                if estado_cliente is None:
                    raise ValueError("La cuenta del cliente no se encontro para actualizar su rango.")
                elif estado_cliente[0] == 'Suspendido':
                    return {"mensaje": "La cuenta del cliente no puede recibir un rango debido a que su cuenta esta suspendida."}
                elif estado_cliente[0] == 'Inactivo':
                    return {"mensaje": "La cuenta del cliente no puede recibir un rango debido a que su cuenta esta inactiva."}

                #Obtenemos la cantidad total de compras del cliente
                cursor.execute(
                    "SELECT COUNT(*) FROM ventas WHERE id_cliente = %s", (id_cliente,)
                )
                compras_totales = cursor.fetchone()[0]

                #Determinamos el nuevo rango en función del número total de compras
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

                #Validamos el rango actual y actualizamos si es necesario
                cursor.execute("SELECT idrango FROM puntos WHERE idclientes_puntos = %s", (id_cliente,))
                rango_actual = cursor.fetchone()[0]

                if nuevo_rango > rango_actual:
                    cursor.execute(
                        "UPDATE puntos SET idrango = %s, ultima_actualizacionRangos = NOW() WHERE idclientes_puntos = %s",
                        (nuevo_rango, id_cliente)
                    )
                    #Confirmamos la transaccion
                    connection.commit()
                    return {
                        "mensaje": f"Rango actualizado a {nuevo_rango} despues de {compras_totales} compras.",
                        "nuevo_rango": nuevo_rango,
                    }
                else:
                    return {"mensaje": "La cuenta del cliente ya tiene el rango adecuado para su numero total de compras."}

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            connection.rollback()
            raise e
        finally:
            connection.close()

    def obtener_rango_cliente(self, id_cliente):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                #Comenzamos la transaccion
                connection.begin()

                cursor.execute(
                    "SELECT idrango FROM puntos WHERE idclientes_puntos = %s", (id_cliente,)
                )
                #Confirmamos la transaccion
                connection.commit()

                resultado = cursor.fetchone()

                if resultado:
                    return {"rango": resultado[0]}
                else:
                    return {"mensaje": "Cliente no encontrado"}
        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            connection.rollback()
            raise e
        finally:
            connection.close()

# ---------------------------------------------------------------------------------------------------------------------------
    
    # FUNCIONALIDAD QUE DEVUELVE EL IDRANGO Y EL NOMBRE_RANGO
    # EN BASE AL IDCLIENTE PROPORCIONADO

    def obtener_rango_cliente_atencion(self, id_cliente):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                #Comenzamos la transaccion
                connection.begin()

                cursor.execute(
                    """
                    SELECT p.idclientes_puntos, p.idrango, r.nombre_rango 
                    FROM puntos p
                    JOIN rangos r ON p.idrango = r.idrango
                    WHERE p.idclientes_puntos = %s
                    """,
                    (id_cliente,)
                )
                #Confirmamos la transaccion
                connection.commit()

                resultado = cursor.fetchone()

                if resultado:
                    return {"idcliente_puntos": resultado[0], "idrango": resultado[1], "nombre_rango": resultado[2]}
                else:
                    return {"mensaje": "Cliente no encontrado en la tabla 'puntos'. Esto se debe a que su cuenta esta Inactiva/Suspendida y por ende no se le asigno un rango."}

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            connection.rollback()
            raise e
        finally:
            connection.close()

# ---------------------------------------------------------------------------------------------------------------------------

    def obtener_porcentaje_compra(self, idrango):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                #Comenzamos la transaccion
                connection.begin()

                cursor.execute(
                    "SELECT porcentaje_puntos FROM rangos WHERE idrango = %s", (idrango,)
                )
                # Confirmamos la transaccion
                connection.commit()

                resultado = cursor.fetchone()
            
                if resultado:
                    return resultado[0]
                else:
                    raise ValueError("Porcentaje Puntos Compra no fue encontrado.")

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            connection.rollback()
            raise e
        finally:
            connection.close()

    def obtener_porcentaje_devolucion(self, idrango):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                #Comenzamos la transaccion
                connection.begin()
                
                cursor.execute(
                    "SELECT porcentaje_devolucionPuntos FROM rangos WHERE idrango = %s", (idrango,)
                )
                # Confirmamos la transaccion
                connection.commit()

                resultado = cursor.fetchone()
            
                if resultado:
                    return resultado[0]
                else:
                    raise ValueError("Porcentaje Puntos Devolucion no fue encontrado.")

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            connection.rollback()
            raise e
        finally:
            connection.close()

# ---------------------------------------------------------------------------------------------------------------------------
