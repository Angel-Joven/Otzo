from flask import request, jsonify, Response
from . import atencion_bp  # Importa el Blueprint de atencion
from src.services.atencion.AtencionService import QuejasService, SugerenciasService
from src.db import get_connection
import json
from datetime import datetime

# Conversor para serializar datetimes
def custom_json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convierte datetimes a ISO 8601
    return str(obj)  # Convierte otros tipos problemáticos a cadena

@atencion_bp.route("/quejas", methods=["GET"])
def get_complaints():
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM quejas",
        )
        resultado = cursor.fetchall()
        print(resultado)
        connection.close()

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        {"Quejas": resultado}, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")

@atencion_bp.route("/quejas", methods=["POST"])
def add_complaint():
    # Lógica para agregar una nueva queja
    data = request.json
    queja = QuejasService(
        data["id_cliente"],
        data["id_trabajador"],
        data["descripcion"],
    )
    queja.crearQueja()
    return jsonify({"message": "Queja registrada con éxito"})

@atencion_bp.route("/quejas/<int:id_queja>", methods=["PUT"])
def resolve_complaint(id_queja):
    # Lógica para actualizar una queja
    queja = QuejasService(None, None, None)
    queja.actualizarEstado(id_queja)
    return jsonify({"message": "Queja resuelta con éxito"})

@atencion_bp.route("/sugerencias", methods=["GET"])
def get_suggestions():
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM sugerencias",
        )
        resultado = cursor.fetchall()
        print(resultado)
        connection.close()

    # Convierte el resultado a JSON usando el conversor personalizado
    json_data = json.dumps(
        {"Sugerencias": resultado}, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")

@atencion_bp.route("/sugerencias", methods=["POST"])
def add_suggestion():
    # Lógica para agregar una nueva sugerencia
    data = request.json
    sugerencia = SugerenciasService(
        data["id_cliente"],
        data["id_trabajador"],
        data["descripcion"],
    )
    sugerencia.crearSugerencia()
    return jsonify({"message": "Sugerencia registrada con éxito"})

@atencion_bp.route("/sugerencias/<int:id_sugerencia>", methods=["PUT"])
def resolve_suggestion(id_sugerencia):
    # Lógica para actualizar una sugerencia
    sugerencia = SugerenciasService(None, None, None)
    sugerencia.actualizarEstado(id_sugerencia)
    return jsonify({"message": "Sugerencia resuelta con éxito"})