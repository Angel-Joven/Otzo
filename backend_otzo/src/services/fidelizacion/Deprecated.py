# Servicios Antiguos o Descartados para el Modulo de Fidelizacion y Marketing
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from src.models.fidelizacion.fidelizacionModels import PuntosModelo, RangosModelo
from src.db import get_connection
from pymysql import DatabaseError

# ---------------------------------------------------------------------------------------------------------------------------

class PuntosService(PuntosModelo):
    def obtener_porcentaje_compra(self, idCliente, idrango):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()

                cursor.execute("SELECT idCliente FROM clientes WHERE idCliente = %s", (idCliente,))
                cliente_existente = cursor.fetchone()

                if not cliente_existente:
                    raise ValueError("La cuenta del cliente no fue encontrado.")

                cursor.execute("SELECT porcentaje_puntos FROM rangos WHERE idrango = %s", (idrango,))
                # Confirmamos la transaccion
                conexion.commit()

                resultado = cursor.fetchone()
            
                if resultado:
                    return resultado[0]
                else:
                    raise ValueError("Porcentaje Puntos Compra no fue encontrado.")

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()

    def obtener_porcentaje_devolucion(self, idCliente, idrango):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()
                
                cursor.execute("SELECT idCliente FROM clientes WHERE idCliente = %s", (idCliente,))
                cliente_existente = cursor.fetchone()

                if not cliente_existente:
                    raise ValueError("La cuenta del cliente no fue encontrado.")

                cursor.execute("SELECT porcentaje_devolucionPuntos FROM rangos WHERE idrango = %s", (idrango,))
                #Confirmamos la transaccion
                conexion.commit()

                resultado = cursor.fetchone()
            
                if resultado:
                    return resultado[0]
                else:
                    raise ValueError("Porcentaje Puntos Devolucion no fue encontrado.")

        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()

# ---------------------------------------------------------------------------------------------------------------------------

class RangosService(RangosModelo):
    def obtener_rango_cliente(self, id_cliente):
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:
                #Comenzamos la transaccion
                conexion.begin()

                cursor.execute("SELECT idrango FROM puntos WHERE idclientes_puntos = %s", (id_cliente,))
                #Confirmamos la transaccion
                conexion.commit()

                resultado = cursor.fetchone()

                if resultado:
                    return {"rango": resultado[0]}
                else:
                    return {"mensaje": "Cliente no encontrado"}
        except DatabaseError as e:
            #Deshacemos la transaccion en caso de error
            conexion.rollback()
            raise e
        finally:
            conexion.close()

# ---------------------------------------------------------------------------------------------------------------------------