from flask import request, jsonify, Response
from . import fidelizacion_bp # Importar el Blueprint de fidelizacion
from src.services.fidelizacion.fidelizacionService import PuntosService, RangosService
from src.db import get_connection

from src.utils.Logger import Logger
from pymysql.cursors import DictCursor

# ---------------------------------------------------------------------------------------------------------------------------

@fidelizacion_bp.route("/", methods=["GET"])
def index():
    try:
        return jsonify({"mensaje": "Hola - Fidelizacion"}), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

@fidelizacion_bp.route("/asigrnginiauto", methods=["GET"])
def asignarRangoInicialAutomatico():
    try:
        rangos_service = RangosService()
        resultado = rangos_service.asignarRangoInicialAuto()
        return jsonify(resultado), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@fidelizacion_bp.route("/actualizarrango", methods=["POST"])
def actualizarRango():
    try:
        data = request.json
        id_cliente = data["id_cliente"]

        rangos_service = RangosService()
        resultado = rangos_service.actualizarRangoPorHistorialCompras(id_cliente)

        if "nuevo_rango" in resultado:
            return jsonify(resultado), 200
        else:
            return jsonify(resultado), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para calcular los puntos obtenidos de una compra
@fidelizacion_bp.route("/calcularptscompra", methods=["POST"])
def calcularPuntosCompra():
    try:
        data = request.json
        id_cliente = data["id_cliente"]
        id_rango = data["id_rango"]
        precio_compra_total = data["precioCompraTotal"]

        if precio_compra_total < 0:
            return jsonify({"error": "El precio de la compra no puede ser negativo"}), 400
        
        rangos_service = RangosService()
        porcentaje_compra_puntos = rangos_service.obtener_porcentaje_compra(id_rango)
        
        if porcentaje_compra_puntos is None:
            return jsonify({"error": "Rango no encontrado"}), 400

        puntos_service = PuntosService()
        puntos_obtenidos = puntos_service.calcular_puntos_compra(id_cliente, id_rango, precio_compra_total, porcentaje_compra_puntos)
        return jsonify({"message": "Puntos de una compra calculados con exito", 'Puntos obtenidos': puntos_obtenidos}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

#Ruta para añadir los puntos obtenidos de una compra
@fidelizacion_bp.route("/addptscompra", methods=["POST"])
def añadirPuntosCompra():
    try:
        data = request.json
        id_cliente = data["id_cliente"]
        puntos_compra = data["puntosCompra"]

        puntos_service = PuntosService()
        puntos_service.añadir_puntos_compra(id_cliente, puntos_compra)
        return jsonify({"message": "Puntos de una compra añadidos con exito", "Puntos Compra": puntos_compra}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para calcular los puntos obtenidos de una devolucion
@fidelizacion_bp.route("/calcularptsdevolucion", methods=["POST"])
def calcularPuntosDevolucion():
    try:
        data = request.json
        id_cliente = data["id_cliente"]
        id_rango = data["id_rango"]
        precio_producto = data["precioProducto"]

        if precio_producto < 0:
            return jsonify({"error": "El precio del producto no puede ser negativo"}), 400

        rangos_service = RangosService()
        porcentaje_devolucion_puntos = rangos_service.obtener_porcentaje_devolucion(id_rango)
        
        if porcentaje_devolucion_puntos is None:
            return jsonify({"error": "Rango no encontrado"}), 400

        puntos_service = PuntosService()
        puntos_devolucion = puntos_service.calcular_puntos_devolucion(id_cliente, id_rango, precio_producto, porcentaje_devolucion_puntos)
        return jsonify({"message": "Puntos de una devolucion calculados con exito", 'Puntos devolucion': puntos_devolucion}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

#Ruta para añadir los puntos obtenidos de una devolucion
@fidelizacion_bp.route("/añadirPuntosDevolucion", methods=["POST"])
def añadirPuntosDevolucion():
    try:
        data = request.json
        id_cliente = data["id_cliente"]
        puntos_devolucion = data["puntosDevolucion"]

        puntos_service = PuntosService()
        puntos_service.añadir_puntos_devolucion(id_cliente, puntos_devolucion)
        return jsonify({"message": "Puntos de una devolucion añadidos con exito"}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para descontar puntos de una compra
@fidelizacion_bp.route("/descontarpuntos", methods=["POST"])
def descontarPuntos():
    try:
        data = request.json
        id_cliente = data["id_cliente"]
        precio_compra_total = data["precioCompraTotal"]

        if precio_compra_total < 0:
            return jsonify({"error": "El precio de la compra no puede ser negativo"}), 400

        puntos_service = PuntosService()
        resultado = puntos_service.descontar_puntos(id_cliente, precio_compra_total)
        
        if resultado["exito"]:
            return jsonify({"message": resultado["mensaje"]}), 200
        else:
            return jsonify({"message": resultado["mensaje"]}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

# ---------------------------------------------------------------------------------------------------------------------------

@fidelizacion_bp.route("/historialpuntos/<int:id_cliente>", methods=["GET"])
def obtener_historial_puntos(id_cliente):
    connection = get_connection()
    if not connection:
        Logger.add_to_log("error", "No se pudo obtener la conexion a la base de datos")
        return jsonify({"error": "No se pudo obtener la conexion a la base de datos"}), 500

    try:
        with connection.cursor(DictCursor) as cursor:
            query = """
                SELECT p.idclientes_puntos, p.total_puntos, p.ultima_actualizacionPuntos, p.ultima_actualizacionRangos, r.nombre_rango
                FROM puntos p
                JOIN rangos r ON p.idrango = r.idrango
                WHERE p.idclientes_puntos = %s
            """
            cursor.execute(query, (id_cliente,))
            resultado = cursor.fetchone()

            if resultado:
                return jsonify(resultado), 200
            else:
                return jsonify({"mensaje": "Cliente no encontrado"}), 404

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as ex:
        Logger.add_to_log("error", f"Error al obtener el historial de puntos del cliente: {str(ex)}")
        return jsonify({"error": f"Error al obtener el historial de puntos del cliente: {str(ex)}"}), 500
    finally:
        connection.close()

# ---------------------------------------------------------------------------------------------------------------------------

# TEST para ver si hay registros en la tabla 'clientes' - BORRAR O COMENTAR EN PRODUCCION
@fidelizacion_bp.route("/obtcli", methods=["GET"])
def obtcli():
    connection = get_connection()
    if not connection:
        Logger.add_to_log("error", "No se pudo obtener la conexion a la base de datos")
        return jsonify({"error": "No se pudo obtener la conexion a la base de datos"}), 500

    try:
        with connection.cursor(DictCursor) as cursor:
            query = "SELECT * FROM clientes"
            cursor.execute(query)
            #result = cursor.fetchone()
            result = cursor.fetchall()
            
            if result:
                return jsonify({"Clientes": result}), 200
            else:
                return jsonify({"message": "No se encontraron clientes", "Clientes": []}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as ex:
        Logger.add_to_log("error", f"Error al obtener los clientes: {str(ex)}")
        return jsonify({"error": f"Error al obtener los clientes: {str(ex)}"}), 500
    finally:
        connection.close()

# TEST para ver si hay registros en la tabla 'puntos' - BORRAR O COMENTAR EN PRODUCCION
@fidelizacion_bp.route("/obtpts", methods=["GET"])
def obtpts():
    connection = get_connection()
    if not connection:
        Logger.add_to_log("error", "No se pudo obtener la conexion a la base de datos")
        return jsonify({"error": "No se pudo obtener la conexion a la base de datos"}), 500

    try:
        with connection.cursor(DictCursor) as cursor:
            query = "SELECT * FROM puntos"
            cursor.execute(query)
            #result = cursor.fetchone()
            result = cursor.fetchall()
            
            if result:
                return jsonify({"Puntos": result}), 200
            else:
                return jsonify({"message": "No se encontraron puntos", "Puntos": []}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as ex:
        Logger.add_to_log("error", f"Error al obtener los puntos: {str(ex)}")
        return jsonify({"error": f"Error al obtener los puntos: {str(ex)}"}), 500
    finally:
        connection.close()

# TEST para ver si hay registros en la tabla 'rangos' - BORRAR O COMENTAR EN PRODUCCION
@fidelizacion_bp.route("/obtrng", methods=["GET"])
def obtrng():
    connection = get_connection()
    if not connection:
        Logger.add_to_log("error", "No se pudo obtener la conexion a la base de datos")
        return jsonify({"error": "No se pudo obtener la conexion a la base de datos"}), 500

    try:
        with connection.cursor(DictCursor) as cursor:
            query = "SELECT * FROM rangos"
            cursor.execute(query)
            #result = cursor.fetchone()
            result = cursor.fetchall()
            
            if result:
                return jsonify({"Rangos": result}), 200
            else:
                return jsonify({"message": "No se encontraron rangos", "Rangos": []}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as ex:
        Logger.add_to_log("error", f"Error al obtener los rangos: {str(ex)}")
        return jsonify({"error": f"Error al obtener los rangos: {str(ex)}"}), 500
    finally:
        connection.close()

# TEST para ver si hay registros en la tabla 'ventas' - BORRAR O COMENTAR EN PRODUCCION
@fidelizacion_bp.route("/obtvts", methods=["GET"])
def obtvts():
    connection = get_connection()
    if not connection:
        Logger.add_to_log("error", "No se pudo obtener la conexion a la base de datos")
        return jsonify({"error": "No se pudo obtener la conexion a la base de datos"}), 500

    try:
        with connection.cursor(DictCursor) as cursor:
            query = "SELECT * FROM ventas"
            cursor.execute(query)
            #result = cursor.fetchone()
            result = cursor.fetchall()
            
            if result:
                return jsonify({"Ventas": result}), 200
            else:
                return jsonify({"message": "No se encontraron ventas", "ventas": []}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as ex:
        Logger.add_to_log("error", f"Error al obtener las ventas: {str(ex)}")
        return jsonify({"error": f"Error al obtener las ventas: {str(ex)}"}), 500
    finally:
        connection.close()

# ---------------------------------------------------------------------------------------------------------------------------