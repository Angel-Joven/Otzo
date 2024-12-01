from flask import request, jsonify, Response
from pymysql.cursors import DictCursor
from src.db import get_connection
from datetime import datetime
from decimal import Decimal
from . import ventas_bp  # Importa el Blueprint de ventas
import json
from flask_cors import cross_origin

from src.models.ventas.VentasDTOs import VentaDTO, DetalleVentaDTO

from src.services.ventas.VentaServicio import VentaServicio
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

    detalles_venta = []

    inventario_servicio = InventarioServicio()
    detalle_inventario_servicio = DetalleInventarioServicio()

    codigos = []

    for producto in data["productos"]:
        cantidad_suficiente = inventario_servicio.comprobarStock(
            producto["id_inventario"], producto["cantidad"]
        )

        if not cantidad_suficiente:
            return (
                jsonify(
                    {
                        "Mensaje": f"No hay stock suficiente del producto: {producto["nombre_producto"]}"
                    }
                ),
                404,
            )

        datos_tipo_producto = inventario_servicio.retornar_tipo_producto(
            producto["id_inventario"]
        )

        codigo_producto = detalle_inventario_servicio.obtenerProductos(
            producto["id_inventario"], codigos
        )

        codigos.append(codigo_producto["codigo_producto"])

        detalle_venta = DetalleVentaDTO(
            datos_tipo_producto["nombre_producto"],
            codigo_producto["codigo_producto"],
            datos_tipo_producto["categoria_producto"],
            datos_tipo_producto["id_inventario"],
            datos_tipo_producto["precio_unitario"],
            False,
            None,
            None,
        )

        detalles_venta.append(detalle_venta)

    venta = VentaDTO(
        float(data["monto_recibido"]),
        datetime.now(),
        data["metodo_pago"],
        1,
        7,
        detalles_venta,
        data["total"],
    )

    venta_servicio = VentaServicio()

    venta_servicio.agregarVenta(venta)

    return jsonify({"Mensaje": "Venta agregada correctamente"}), 200
