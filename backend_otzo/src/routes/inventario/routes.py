from . import inventario_bp  # Importa el Blueprint de ventas
from flask import request, jsonify, Response
from datetime import datetime
from decimal import Decimal
from . import inventario_bp  # Importa el Blueprint de ventas
import json
from flask_cors import cross_origin

from src.services.inventario.InventarioServicio import (
    InventarioServicio,
    DetalleInventarioServicio,
)
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
        tipos_productos,
        ensure_ascii=False,
        default=custom_json_serializer,
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@inventario_bp.route("/vender", methods=["GET"])
def productosVender():

    inventario_servicio = InventarioServicio()

    tipos_productos = inventario_servicio.listarTipoProductosALaVenta()

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        tipos_productos,
        ensure_ascii=False,
        default=custom_json_serializer,
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@inventario_bp.route("/<int:id>", methods=["GET"])
def obtener_producto(id):

    inventario_servicio = InventarioServicio()

    tipos_productos = inventario_servicio.obtenerTipoProducto(id)

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        tipos_productos,
        ensure_ascii=False,
        default=custom_json_serializer,
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@inventario_bp.route("/categorias", methods=["GET"])
def listar_categorias():

    inventario_servicio = InventarioServicio()

    tipos_productos = inventario_servicio.listarCategoriasTiposProductos()

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        tipos_productos,
        ensure_ascii=False,
        default=custom_json_serializer,
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@inventario_bp.route("/listar_descontinuados", methods=["GET"])
def listar_descontinuados():

    inventario_servicio = InventarioServicio()

    tipos_productos = inventario_servicio.listarTipoProductosDescontinuados()

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        tipos_productos,
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
        str(data["nombre_tipo_producto"]),
        str(data["imagen_tipo_producto"]),
        str(data["categoria_tipo_producto"]),
        str(data["descripcion_tipo_producto"]),
        float(data["precio_unitario"]),
        0,
        False,
        int(data["cantidad_maxima_producto"]),
    )

    resultado = inventario_servicio.agregarTipoProducto(nuevo_tipo_producto)

    if resultado:
        return jsonify({"mensaje": "Tipo de producto agregado correctamente"}), 200
    else:
        return jsonify({"error": "No se pudo agregar el tipo de producto"}), 500


@inventario_bp.route("/actualizar_tipo_producto", methods=["PUT"])
@cross_origin()
def actualizar_tipo_producto():

    data = request.json

    inventario_servicio = InventarioServicio()

    nuevo_tipo_producto = InventarioDTO(
        str(data["nombre_tipo_producto"]),
        str(data["imagen_tipo_producto"]),
        str(data["categoria_tipo_producto"]),
        str(data["descripcion_tipo_producto"]),
        float(data["precio_unitario"]),
        int(data["cantidad_tipo_producto"]),
        bool(data["descontinuado"]),
        int(data["cantidad_maxima_producto"]),
        int(data["id_inventario"]),
    )

    resultado = inventario_servicio.actualizarTipoProducto(nuevo_tipo_producto)

    if resultado:
        return jsonify({"mensaje": "Tipo de producto actualizado correctamente"}), 200
    else:
        return jsonify({"error": "No se pudo actualizar el tipo de producto"}), 500


@inventario_bp.route("/descontinuar_tipo_producto", methods=["PATCH"])
@cross_origin()
def descontinuar_tipo_producto():

    data = request.json

    inventario_servicio = InventarioServicio()

    producto_a_descontinuar = InventarioDTO(
        str(data["nombre_tipo_producto"]),
        str(data["imagen_tipo_producto"]),
        str(data["categoria_tipo_producto"]),
        str(data["descripcion_tipo_producto"]),
        float(data["precio_unitario"]),
        int(data["cantidad_tipo_producto"]),
        bool(data["descontinuado"]),
        int(data["cantidad_maxima_producto"]),
        int(data["id_inventario"]),
    )

    resultado = inventario_servicio.eliminarTipoProducto(producto_a_descontinuar)

    if resultado:
        return jsonify({"mensaje": "Tipo de producto descontinuado correctamente"}), 200
    else:
        return jsonify({"error": "No se pudo descontinuar el tipo de producto"}), 500


@inventario_bp.route("/reabastecer", methods=["POST"])
@cross_origin()
def reabastecer():

    data = request.json

    inventario_servicio = DetalleInventarioServicio()

    resultado = inventario_servicio.agregarProducto(
        int(data["id_inventario"]), int(data["cantidad"])
    )

    if resultado:
        return (
            jsonify({"mensaje": "Cantidad de productos agregados correctamente"}),
            200,
        )
    else:
        return jsonify({"error": "No se pudo agregar la cantidad de productos"}), 500


@inventario_bp.route("/historial_reabastecimiento", methods=["GET"])
@cross_origin()
def verHistorialReabastecimiento():
    detalleInventarioServicio = DetalleInventarioServicio()

    reabastecimientos = detalleInventarioServicio.listarReabastecimientosPorDia()

    if not reabastecimientos:
        return jsonify({"error": "No hay historial de reabastecimientos"}), 404
    else:
        return reabastecimientos
