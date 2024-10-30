from flask import request, jsonify
from . import ventas_bp  # Importa el Blueprint de ventas


@ventas_bp.route("/add", methods=["POST"])
def add_sale():
    # Lógica para agregar una nueva venta
    data = request.json
    # Procesa la venta usando `data` y devuelve una respuesta
    return jsonify({"message": "Venta agregada con éxito"})


@ventas_bp.route("/returns", methods=["POST"])
def handle_return():
    # Lógica para manejar devoluciones
    data = request.json
    # Procesa la devolución usando `data` y devuelve una respuesta
    return jsonify({"message": "Devolución procesada con éxito"})
