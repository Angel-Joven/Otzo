from flask import request, jsonify, Response
from pymysql.cursors import DictCursor
from src.db import get_connection
from datetime import datetime
from decimal import Decimal
from . import ventas_bp  # Importa el Blueprint de ventas
import json
from flask_cors import cross_origin

from src.models.ventas.VentasDTOs import VentaDTO, DetalleVentaDTO

from src.services.ventas.VentaServicio import VentaServicio, DetalleVentaServicio
from src.services.inventario.InventarioServicio import (
    InventarioServicio,
    DetalleInventarioServicio,
)


# Conversor para serializar Decimals y datetimes
def custom_json_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # Convierte Decimals a float
    elif isinstance(obj, datetime):
        return obj.isoformat()  # Convierte datetimes a ISO 8601
    return str(obj)  # Convierte otros tipos problemáticos a cadena


@ventas_bp.route("/", methods=["GET"])
def index():
    conexion = get_connection()
    cursor = conexion.cursor(DictCursor)

    cursor.execute(
        "SELECT * FROM ventas",
    )

    resultado = cursor.fetchall()
    conexion.close()

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        {"ventas": resultado}, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@ventas_bp.route("/agregar", methods=["POST"])
def agregar():
    data = request.json

    inventario_servicio = InventarioServicio()
    detalle_inventario_servicio = DetalleInventarioServicio()
    venta_servicio = VentaServicio()
    detalle_venta_servicio = DetalleVentaServicio()

    productos = data["productos"]
    # Validar el total de la venta
    total_venta = venta_servicio.calcularTotalVenta(productos)
    metodo_pago = str(data["metodo_pago"])
    monto_recibido = float(data["monto_recibido"])

    detalles_venta = detalle_venta_servicio.llenarDatos(productos)

    print("DETALLES VENTA: ", detalles_venta)

    if data["metodo_pago"] == "efectivo":
        print("METODO PAGO EFECTIVO")

        # FUNCIONALIDAD A PROBAR

        # venta = VentaDTO(monto_recibido, datetime.now(), metodo_pago, 1, 7, total_venta, detalles_venta)
        # venta_servicio.agregarVentaEfectivo(venta)

    elif data["metodo_pago"] == "tarjeta":
        print("METODO PAGO TARJETA")
    elif data["metodo_pago"] == "puntos":
        print("METODO PAGO PUNTOS")

    return jsonify({"Mensaje": "Venta agregada correctamente"}), 200
