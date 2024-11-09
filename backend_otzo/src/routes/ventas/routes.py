from flask import request, jsonify, Response
from pymysql.cursors import DictCursor
from src.db import get_connection
from datetime import datetime
from decimal import Decimal
from . import ventas_bp  # Importa el Blueprint de ventas
import json

from src.models.ventas.VentasDTOs import VentaDTO, DetalleVentaDTO

from src.services.ventas.VentaServicio import VentaServicio


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

    # Crear los objetos DetalleVentasDTO
    detalles_venta = []

    conexion = get_connection()
    cursor = conexion.cursor(DictCursor)

    for producto in data["detalles_venta"]:
        cursor.execute(
            "select * from inventario where codigo_producto = (%s)",
            producto["codigo_producto"],
        )

        producto_db = cursor.fetchone()

        if not producto_db:
            return (
                jsonify(
                    {
                        "error": f"Producto con código {producto["codigo_producto"]} no encontrado"
                    }
                ),
                404,
            )

        detalle = DetalleVentaDTO(
            producto_db["id_inventario"],
            producto["codigo_producto"],
            producto_db["nombre_producto"],
            producto_db["categoria"],
            float(producto_db["precio_unitario"]),
        )

        detalles_venta.append(detalle)

    conexion.close()

    # Crear el objeto VentaDTO
    venta = VentaDTO(
        data["monto_recibido"],
        datetime.now(),
        data["metodo_pago"],
        data["id_cliente"],
        data["id_empleado"],
        detalles_venta,
    )

    venta_servicio = VentaServicio()
    venta.total_venta = venta_servicio.calcularTotalVenta(venta)

    if venta.monto_recibido >= venta.total_venta:
        venta_servicio.agregarVenta(venta)

    # Calcular el total de la venta
    # venta.total_venta = VentaService().calcularTotalVenta(venta)

    # Agregar la venta a la base de datos
    # VentaService().agregarVenta(venta)

    return jsonify({"Mensaje": "Venta agregada correctamente"}), 201
