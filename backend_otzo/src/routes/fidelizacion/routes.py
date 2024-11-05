from flask import request, jsonify
from . import fidelizacion_bp  # Importar el Blueprint de ventas

from src.db import get_connection
from src.utils.Logger import Logger

from pymysql.cursors import DictCursor

@fidelizacion_bp.route("/", methods=["GET"])
def index():
    return jsonify({"mensaje": "Hola - Fidelizacion"})

@fidelizacion_bp.route("/calcularptscompra", methods=["POST"])
def calcularPuntosCompra():
    # Lógica para calcular los puntos de una compra
    data = request.json

    id_cliente = data['id_cliente']
    idrango = data['idrango']
    precio_compra_total = data['precioCompraTotal']
    porcentaje_compra_puntos = data['porcentajeCompraPuntos']
    puntos_obtenidos = int(precio_compra_total * (porcentaje_compra_puntos / 100))

    # Procesa los puntos usando `data` y devuelve una respuesta
    return jsonify({"message": "Puntos de una compra calculados con éxito"},{'Puntos obtenidos': puntos_obtenidos})

@fidelizacion_bp.route("/calcularptsdevolucion", methods=["POST"])
def calcularPuntosDevolucion():
    # Lógica para calcular los puntos de una devolucion
    data = request.json

    id_cliente = data['id_cliente']
    idrango = data['idrango']
    precio_producto = data['precioProducto']
    porcentaje_devolucion_puntos = data['porcentajeDevolucionPuntos']
    puntos_obtenidos = int(precio_producto * (porcentaje_devolucion_puntos / 100))

    # Procesa los puntos usando `data` y devuelve una respuesta
    return jsonify({"message": "Puntos de una devolucion calculados con éxito"},{'puntos_obtenidos': puntos_obtenidos})

@fidelizacion_bp.route("/addptscompra", methods=["POST"])
def añadirPuntosCompra():
    # Lógica para añadir los puntos de una compra al cliente
    data = request.json

    id_cliente = data['id_cliente']
    puntos_compra = data['puntosCompra']
    
    # Lógica para insertar o actualizar en la tabla 'puntos'
    # Actualiza total_puntos en la tabla 'puntos' del cliente

    # Procesa los puntos usando `data` y devuelve una respuesta
    return jsonify({"message": "Puntos de una compra añadidos con éxito"})

@fidelizacion_bp.route("/addptsdevolucion", methods=["POST"])
def añadirPuntosDevolucion():
    # Lógica para añadir los puntos de una devolucion al cliente
    data = request.json

    id_cliente = data['id_cliente']
    puntos_devolucion = data['puntosDevolucion']

    # Lógica de actualización en la tabla 'puntos' para la devolución
    # Actualiza total_puntos en la tabla 'puntos' del cliente

    # Procesa los puntos usando `data` y devuelve una respuesta
    return jsonify({"message": "Puntos de una devolucion añadidos con éxito"})

@fidelizacion_bp.route("/descontarpuntos", methods=["POST"])
def descontarPuntos():
    # Lógica para calcular los puntos que se descontaran de una compra
    data = request.json

    id_cliente = data['id_cliente']
    precio_compra_total = data['precioCompraTotal']
    
    # Consulta para obtener los puntos del cliente
    puntos_totales = obtenerPuntos(id_cliente)
    
    if puntos_totales >= precio_compra_total:
        # Resta puntos y procede con la transacción
        return jsonify({'status': 'success', 'mensaje': 'Transacción completada con puntos'})
    else:
        # Notifica al usuario sobre puntos insuficientes
        return jsonify({'status': 'failed', 'mensaje': f'Puntos Insuficientes. Actualmente tienes {puntos_totales} puntos.'})

    # Procesa los puntos usando `data` y devuelve una respuesta
    #return jsonify({"message": "Puntos descontados de una compra con éxito"})

id_cliente = 1 # test id

@fidelizacion_bp.route("/obtenerpuntos", methods=["GET"])
def obtenerPuntos(id_cliente=1):
    connection = get_connection()
    if not connection:
        Logger.add_to_log("error", "No se pudo obtener la conexión a la base de datos.")
        return 0

    try:
        with connection.cursor(DictCursor) as cursor:
            query = "SELECT total_puntos FROM puntos WHERE idclientes_puntos = %s"
            cursor.execute(query, (id_cliente,))
            result = cursor.fetchone()
            return result['total_puntos'] if result else jsonify({"message": "Puntos obtenidos correctamente del usuario"},{'Puntos del usuario': result})
    except Exception as ex:
        Logger.add_to_log("error", f"Error al obtener puntos para cliente {id_cliente}: {str(ex)}")
        return 0
    finally:
        connection.close()

# ---------------------------------------------------------------------------------------------------------------------------

# Test para ver si hay registros en la tabla 'clientes' - BORRAR O COMENTAR EN PRODUCCION
@fidelizacion_bp.route("/obtcli", methods=["GET"])
def obtcli():
    connection = get_connection()
    if not connection:
        Logger.add_to_log("error", "No se pudo obtener la conexión a la base de datos.")
        return jsonify({"error": "No se pudo obtener la conexión a la base de datos."}), 500

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

# Test para ver si hay registros en la tabla 'puntos' - BORRAR O COMENTAR EN PRODUCCION
@fidelizacion_bp.route("/obtpts", methods=["GET"])
def obtpts():
    connection = get_connection()
    if not connection:
        Logger.add_to_log("error", "No se pudo obtener la conexión a la base de datos.")
        return jsonify({"error": "No se pudo obtener la conexión a la base de datos."}), 500

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

# Test para ver si hay registros en la tabla 'rangos' - BORRAR O COMENTAR EN PRODUCCION
@fidelizacion_bp.route("/obtrng", methods=["GET"])
def obtrng():
    connection = get_connection()
    if not connection:
        Logger.add_to_log("error", "No se pudo obtener la conexión a la base de datos.")
        return jsonify({"error": "No se pudo obtener la conexión a la base de datos."}), 500

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