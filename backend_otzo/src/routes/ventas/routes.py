from flask import request, jsonify, Response
from pymysql.cursors import DictCursor
from src.db import get_connection
from datetime import datetime
from decimal import Decimal
from . import ventas_bp  # Importa el Blueprint de ventas
import json
from flask_cors import cross_origin

from src.models.ventas.VentasDTOs import VentaDTO

from src.services.ventas.VentaServicio import VentaServicio, DetalleVentaServicio
from src.services.inventario.InventarioServicio import (
    InventarioServicio,
    DetalleInventarioServicio,
)

# Servicios de fidelizacion:
from src.services.fidelizacion.fidelizacionService import (
    CalcularAgregarPuntosCompraActualizarRangoService,
    CalcularAgregarPuntosDevolucionActualizarRangoService,
    PagarPuntosCompraActualizarRangoService,
)

from src.services.fidelizacion.fidelizacionService import PuntosService


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

    # Servicios de fidelizacion:
    calcular_agregar_puntos_compra_rango_service = (
        CalcularAgregarPuntosCompraActualizarRangoService()
    )
    calcular_agregar_puntos_devolucion_rango_service = (
        CalcularAgregarPuntosDevolucionActualizarRangoService()
    )
    pagar_puntos_compra_rango_service = PagarPuntosCompraActualizarRangoService()

    puntos_service = PuntosService()

    productos = data["productos"]

    # Validar que el inventario tenga los productos necesarios

    stock = inventario_servicio.validarInventario(productos)

    if not stock:
        return jsonify({"Error": "No hay stock suficiente para realizar la venta"}), 400

    # Validar el total de la venta
    total_venta = venta_servicio.calcularTotalVenta(productos)
    metodo_pago = str(data["metodo_pago"])
    monto_recibido = float(data["monto_recibido"])
    id_cliente = int(data["id_cliente"])
    id_empleado = int(data["id_empleado"])

    detalles_venta = detalle_venta_servicio.llenarDatos(productos)

    print("DETALLES VENTA: ", detalles_venta)

    if data["metodo_pago"] == "efectivo":
        print("METODO PAGO EFECTIVO")

        venta = VentaDTO(
            monto_recibido,
            datetime.now(),
            metodo_pago,
            id_cliente,
            id_empleado,
            total_venta,
            detalles_venta,
        )

        venta_hecha = venta_servicio.agregarVenta(venta)

        if not venta_hecha:
            return jsonify({"Error": "No se pudo agregar la venta"}), 400

        calcular_agregar_puntos_compra_rango_service.obtener_y_asignar_nuevo_Rango(
            id_cliente
        )
        calcular_agregar_puntos_compra_rango_service.calcular_y_agregar_puntos_compra(
            id_cliente, total_venta
        )

    elif data["metodo_pago"] == "tarjeta":
        print("METODO PAGO TARJETA")

        venta = VentaDTO(
            total_venta,
            datetime.now(),
            metodo_pago,
            id_cliente,
            id_empleado,
            total_venta,
            detalles_venta,
        )

        venta_hecha = venta_servicio.agregarVenta(venta)

        if not venta_hecha:
            return jsonify({"Error": "No se pudo agregar la venta"}), 400

        calcular_agregar_puntos_compra_rango_service.obtener_y_asignar_nuevo_Rango(
            id_cliente
        )
        calcular_agregar_puntos_compra_rango_service.calcular_y_agregar_puntos_compra(
            id_cliente, total_venta
        )

    elif data["metodo_pago"] == "puntos":
        print("METODO PAGO PUNTOS")

        venta = VentaDTO(
            total_venta,
            datetime.now(),
            metodo_pago,
            id_cliente,
            id_empleado,
            total_venta,
            detalles_venta,
        )

        puntos_suficientes = puntos_service.comprobar_puntos(id_cliente, total_venta)

        if not puntos_suficientes:
            return (
                jsonify({"Error": "No hay suficientes puntos para realizar la compra"}),
                400,
            )

        venta_hecha = venta_servicio.agregarVenta(venta)

        if not venta_hecha:
            return jsonify({"Error": "No se pudo agregar la venta"}), 400

        pagar_puntos_compra_rango_service.obtener_y_asignar_nuevo_Rango(id_cliente)
        pagar_puntos_compra_rango_service.pagar_con_puntos_compra(
            id_cliente, total_venta
        )

    return jsonify({"Mensaje": "Venta agregada correctamente"}), 200


@ventas_bp.route("/ver_historial", methods=["POST"])
def ver_historial():
    data = request.json

    id_cliente = int(data["id_cliente"])

    venta_servicio = VentaServicio()

    historial = venta_servicio.listarVentasDeUsuario(id_cliente)

    if not historial:
        return jsonify({"Error": "No hay historial de ventas para este cliente"}), 404

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        historial, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@ventas_bp.route("/ver_historial/detalles_ventas", methods=["POST"])
def ver_historial_detalles_ventas():
    data = request.json

    ids_ventas = data["ids_ventas"]

    detalle_venta_servicio = DetalleVentaServicio()

    historial = detalle_venta_servicio.listarVariosDetallesDeVentas(ids_ventas)

    if not historial:
        return (
            jsonify(
                {
                    "Error": "No hay historial de detalles ventas para este cliente o fallo 1"
                }
            ),
            404,
        )

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        historial, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")
