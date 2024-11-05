from flask import request, jsonify, Response
from . import ventas_bp  # Importa el Blueprint de ventas
from src.services.ventas.VentaService import VentaService
from src.db import get_connection
import json
from decimal import Decimal
from datetime import datetime


# Conversor para serializar Decimals y datetimes
def custom_json_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # Convierte Decimals a float
    elif isinstance(obj, datetime):
        return obj.isoformat()  # Convierte datetimes a ISO 8601
    return str(obj)  # Convierte otros tipos problemáticos a cadena


@ventas_bp.route("/", methods=["GET"])
def index():
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM ventas",
        )
        resultado = cursor.fetchall()
        print(resultado)
        connection.close()

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        {"Ventas": resultado}, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


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
