from flask import request, jsonify
from . import fidelizacion_bp  # Importa el Blueprint de ventas

@fidelizacion_bp.route("/", methods=["GET"])
def index():
    return jsonify({"mensaje": "Hola - Fidelizacion"})

@fidelizacion_bp.route("/calcularptscompra", methods=["POST"])
def calcularPuntosCompra():
    # Lógica para calcular los puntos de una compra
    data = request.json
    # Procesa los puntos usando `data` y devuelve una respuesta
    return jsonify({"message": "Puntos de una compra calculados con éxito"})

@fidelizacion_bp.route("/calcularptsdevolucion", methods=["POST"])
def calcularPuntosDevolucion():
    # Lógica para calcular los puntos de una devolucion
    data = request.json
    # Procesa los puntos usando `data` y devuelve una respuesta
    return jsonify({"message": "Puntos de una devolucion calculados con éxito"})

@fidelizacion_bp.route("/addptscompra", methods=["POST"])
def añadirPuntosCompra():
    # Lógica para añadir los puntos de una compra al cliente
    data = request.json
    # Procesa los puntos usando `data` y devuelve una respuesta
    return jsonify({"message": "Puntos de una compra añadidos con éxito"})

@fidelizacion_bp.route("/addptsdevolucion", methods=["POST"])
def añadirPuntosDevolucion():
    # Lógica para añadir los puntos de una devolucion al cliente
    data = request.json
    # Procesa los puntos usando `data` y devuelve una respuesta
    return jsonify({"message": "Puntos de una devolucion añadidos con éxito"})

@fidelizacion_bp.route("/descontarpuntos", methods=["POST"])
def descontarPuntos():
    # Lógica para calcular los puntos que se descontaran de una compra
    data = request.json
    # Procesa los puntos usando `data` y devuelve una respuesta
    return jsonify({"message": "Puntos descontados de una compra con éxito"})
