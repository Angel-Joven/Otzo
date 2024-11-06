from flask import request, jsonify, Response
from . import ventas_bp  # Importa el Blueprint de ventas
from src.services.ventas.VentaService import VentaService
from src.db import get_connection
from pymysql.cursors import DictCursor
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

    with connection.cursor(DictCursor) as cursor:
        cursor.execute(
            "SELECT * FROM ventas",
        )
        resultado = cursor.fetchall()
        print(resultado)
        connection.close()

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        {"ventas": resultado}, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@ventas_bp.route("/<int:id>", methods=["GET"])
def obtenerVenta(id):
    connection = get_connection()

    with connection.cursor(DictCursor) as cursor:
        cursor.execute("SELECT * FROM ventas where id_venta = (%s)", id)
        resultado = cursor.fetchone()
        print(resultado)
        connection.close()

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        {"venta": resultado}, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@ventas_bp.route("/agregar", methods=["POST"])
def agregar_venta():
    data = request.json

    venta = VentaService(
        data["metodo_pago"],
        data["monto_recibido"],
        data["productos"],
        data["id_cliente"],
        data["id_trabajador"],
    )

    venta.agregarVenta()

    return jsonify({"message": "xd"})


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

    venta.agregarVenta()

    return jsonify({"message": "xd"})

    """ venta = VentaService(
        data["metodo_pago"],
        data["monto_recibido"],
        data["productos"],
        data["id_cliente"],
        data["id_trabajador"],
    )
    total_venta = venta.calcularTotal()
    print(total_venta)
    return jsonify({"total": total_venta}) """
