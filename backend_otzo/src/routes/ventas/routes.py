from flask import request, jsonify
from . import ventas_bp  # Importa el Blueprint de ventas
from src.services.ventas.VentaService import VentaService


@ventas_bp.route("/", methods=["GET"])
def index():
    return jsonify({"mensaje": "hola"})


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


@ventas_bp.route("/test", methods=["POST"])
def test():
    data = request.json
    venta = VentaService(
        data["metodo_pago"],
        data["monto_recibido"],
        data["productos"],
        data["id_cliente"],
        data["id_trabajador"],
    )
    total_venta = venta.calcularTotal()
    print(total_venta)
    return jsonify({"total": total_venta})
