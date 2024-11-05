from flask import request, jsonify, Response
from . import fidelizacion_bp # Importar el Blueprint de fidelizacion
from src.services.fidelizacion.fidelizacionService import PuntosService, RangosService
from src.db import get_connection

from src.utils.Logger import Logger
from pymysql.cursors import DictCursor

# ---------------------------------------------------------------------------------------------------------------------------

@fidelizacion_bp.route("/", methods=["GET"])
def index():
    return jsonify({"mensaje": "Hola - Fidelizacion"})

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para calcular los puntos obtenidos de una compra
@fidelizacion_bp.route("/calcularptscompra", methods=["POST"])
def calcularPuntosCompra():
    data = request.json
    id_cliente = data["id_cliente"]
    id_rango = data["id_rango"]
    precio_compra_total = data["precioCompraTotal"]
    
    rangos_service = RangosService()
    porcentaje_compra_puntos = rangos_service.obtener_porcentaje_compra(id_rango)
    
    if porcentaje_compra_puntos is None:
        return jsonify({"error": "Rango no encontrado"}), 404

    puntos_service = PuntosService()
    puntos_obtenidos = puntos_service.calcular_puntos_compra(id_cliente, id_rango, precio_compra_total, porcentaje_compra_puntos)
    return jsonify({"message": "Puntos de una compra calculados con exito", 'Puntos obtenidos': puntos_obtenidos})

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para calcular los puntos obtenidos de una devolucion
@fidelizacion_bp.route("/calcularptsdevolucion", methods=["POST"])
def calcularPuntosDevolucion():
    data = request.json
    id_cliente = data["id_cliente"]
    id_rango = data["id_rango"]
    precio_producto = data["precioProducto"]

    rangos_service = RangosService()
    porcentaje_devolucion_puntos = rangos_service.obtener_porcentaje_devolucion(id_rango)
    
    if porcentaje_devolucion_puntos is None:
        return jsonify({"error": "Rango no encontrado"}), 404

    puntos_service = PuntosService()
    puntos_devolucion = puntos_service.calcular_puntos_devolucion(id_cliente, id_rango, precio_producto, porcentaje_devolucion_puntos)
    return jsonify({"message": "Puntos de una devolucion calculados con exito", 'Puntos devolucion': puntos_devolucion})

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para añadir los puntos obtenidos de una compra
@fidelizacion_bp.route("/addptscompra", methods=["POST"])
def añadirPuntosCompra():
    data = request.json
    id_cliente = data["id_cliente"]
    puntos_compra = data["puntosCompra"]

    puntos_service = PuntosService()
    puntos_service.añadir_puntos_compra(id_cliente, puntos_compra)
    return jsonify({"message": "Puntos de una compra añadidos con exito"})

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para añadir los puntos obtenidos de una devolucion
@fidelizacion_bp.route("/añadirPuntosDevolucion", methods=["POST"])
def añadirPuntosDevolucion():
    data = request.json
    id_cliente = data["id_cliente"]
    puntos_devolucion = data["puntosDevolucion"]

    puntos_service = PuntosService()
    puntos_service.añadir_puntos_devolucion(id_cliente, puntos_devolucion)
    return jsonify({"message": "Puntos de una devolucion añadidos con exito"})

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para descontar puntos de una compra
@fidelizacion_bp.route("/descontarpuntos", methods=["POST"])
def descontarPuntos():
    data = request.json
    id_cliente = data["id_cliente"]
    precio_compra_total = data["precioCompraTotal"]

    puntos_service = PuntosService()
    resultado = puntos_service.descontar_puntos(id_cliente, precio_compra_total)
    
    if resultado["exito"]:
        return jsonify({"message": "Puntos descontados con exito", "Puntos restantes": resultado["puntos_restantes"]})
    else:
        return jsonify({"message": resultado["mensaje"]}), 400

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
            result = cursor.fetchone()
            
            if result:
                return jsonify({"Clientes": result})
            else:
                return jsonify({"message": "No se encontraron clientes", "Clientes": []}), 200

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
            result = cursor.fetchone()
            
            if result:
                return jsonify({"Puntos": result})
            else:
                return jsonify({"message": "No se encontraron puntos", "Puntos": []}), 200

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
            result = cursor.fetchone()
            
            if result:
                return jsonify({"Rangos": result})
            else:
                return jsonify({"message": "No se encontraron rangos", "Rangos": []}), 200

    except Exception as ex:
        Logger.add_to_log("error", f"Error al obtener los rangos: {str(ex)}")
        return jsonify({"error": f"Error al obtener los rangos: {str(ex)}"}), 500

    finally:
        connection.close()

# ---------------------------------------------------------------------------------------------------------------------------