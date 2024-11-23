from . import inventario_bp  # Importa el Blueprint de ventas
from flask import request, jsonify, Response
from pymysql.cursors import DictCursor
from src.db import get_connection
from datetime import datetime
from decimal import Decimal
from . import inventario_bp  # Importa el Blueprint de ventas
import json
from flask_cors import cross_origin

from src.services.inventario.InventarioServicio import InventarioServicio
from src.models.inventario.InventarioDTOs import InventarioDTO


# Conversor para serializar Decimals y datetimes
def custom_json_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # Convierte Decimals a float
    elif isinstance(obj, datetime):
        return obj.isoformat()  # Convierte datetimes a ISO 8601
    return str(obj)  # Convierte otros tipos problemáticos a cadena


@inventario_bp.route("/", methods=["GET"])
def index():

    inventario_servicio = InventarioServicio()

    tipos_productos = inventario_servicio.listarTipoProductos()

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        {"inventario": tipos_productos},
        ensure_ascii=False,
        default=custom_json_serializer,
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@inventario_bp.route("/agregar_tipo_producto", methods=["POST"])
@cross_origin()
def agregar_tipo_producto():

    data = request.json

    inventario_servicio = InventarioServicio()

    nuevo_tipo_producto = InventarioDTO(
        data["nombre_tipo_producto"],
        data["imagen_tipo_producto"],
        data["categoria_tipo_producto"],
        data["descripcion_tipo_producto"],
    )

    resultado = inventario_servicio.agregarTipoProducto(nuevo_tipo_producto)

    if resultado:
        return jsonify({"mensaje": "Tipo de producto agregado correctamente"}), 200
    else:
        return jsonify({"error": "No se pudo agregar el tipo de producto"}), 500
