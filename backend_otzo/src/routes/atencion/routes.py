from flask import request, jsonify, Response
from pymysql.cursors import DictCursor
from . import atencion_bp  # Importa el Blueprint de atencion
from src.services.atencion.AtencionService import QuejasService, SugerenciasService
from src.models.atencion.atencionDTO import QuejasDTO, SugerenciasDTO
from src.db import get_connection
import json
from datetime import datetime


# Conversor para serializar datetimes
def custom_json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convierte datetimes a ISO 8601
    return str(obj)  # Convierte otros tipos problemáticos a cadena


@atencion_bp.route("/quejas/<int:id>", methods=["GET"])
def obtener_quejas(id):

    quejas_servicio = QuejasService()

    quejas_cliente = quejas_servicio.listarQuejasCliente(id)

    json_data = json.dumps(
        quejas_cliente, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@atencion_bp.route("/quejas/pendientes", methods=["GET"])
def obtener_quejas_pendientes():

    quejas_servicio = QuejasService()

    quejas_cliente = quejas_servicio.listarQuejasPendientes()

    json_data = json.dumps(
        quejas_cliente, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")


@atencion_bp.route("/quejas/crear", methods=["POST"])
def agregar_queja():

    data = request.json

    quejas_servicio = QuejasService()

    queja = QuejasDTO(
        data["id_cliente"],
        data["id_empleado"],
        datetime.now(),
        data["descripcion"],
        data["categoria"],
        data["estado"],
        data["prioridad"],
        data["comentario_seguimiento"],
    )

    quejas_cliente = quejas_servicio.crearQueja(queja)

    if quejas_cliente:
        return jsonify({"message": "Queja registrada con éxito"})
    else:
        return jsonify({"message": "Error al registrar la queja"})

@atencion_bp.route("/quejas/responder", methods=["PATCH"])
def actualizar_queja():

    data = request.json

    quejas_servicio = QuejasService()

    queja = QuejasDTO(
        None,
        data["id_empleado"],
        None,
        None,
        None,
        data["estado"],
        None,
        data["comentarioSeguimiento"],
        data["id_queja"],
    )
    
    print(queja)

    quejas_cliente = quejas_servicio.actualizarQueja(queja)

    if quejas_cliente:
        return jsonify({"message": "Queja actualizada con éxito"})
    else:
        return jsonify({"message": "Error al actualizar la queja"})

@atencion_bp.route("/sugerencias/crear", methods=["POST"])
def agregar_sugerencia():

    data = request.json

    sugerencia_servicio = SugerenciasService()

    sugerencia = SugerenciasDTO(
        data["id_cliente"],
        data["id_empleado"],
        datetime.now(),
        data["descripcion"],
        data["categoria"],
        data["estado"],
        data["comentario_seguimiento"],
    )

    sugerencia_cliente = sugerencia_servicio.crearSugerencia(sugerencia)

    if sugerencia_cliente:
        return jsonify({"message": "Sugerencia registrada con éxito"})
    else:
        return jsonify({"message": "Error al registrar la sugerencia"})


# @atencion_bp.route("/qagregar", methods=["POST"])
# def add_complaint():
#     # Lógica para agregar una nueva queja
#     data = request.json

#     queja = QuejasService(
#         data["id_cliente"],
#         datetime.now(),
#         data["descripcion"],
#         data["categoria"],
#         data["estado"],
#     )
#     queja.crearQueja()
#     return jsonify({"message": "Queja registrada con éxito"})

# @atencion_bp.route("/qagregar/<int:id_queja>", methods=["PUT"])
# def resolve_complaint(id_queja):
#     # Lógica para actualizar una queja
#     queja = QuejasService(None, None, None)
#     queja.actualizarEstado(id_queja)
#     return jsonify({"message": "Queja resuelta con éxito"})

# @atencion_bp.route("/sugerencias", methods=["GET"])
# def get_suggestions():
#     connection = get_connection()

#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT * FROM sugerencias",
#         )
#         resultado = cursor.fetchall()
#         print(resultado)
#         connection.close()

#     # Convierte el resultado a JSON usando el conversor personalizado
#     json_data = json.dumps(
#         {"Sugerencias": resultado}, ensure_ascii=False, default=custom_json_serializer
#     )
#     return Response(json_data, content_type="application/json; charset=utf-8")

# @atencion_bp.route("/sagregar", methods=["POST"])
# def add_suggestion():
#     # Lógica para agregar una nueva sugerencia
#     data = request.json
#     sugerencia = SugerenciasService(
#         data["id_cliente"],
#         datetime.now(),
#         data["descripcion"],
#         data["categoria"],
#     )
#     sugerencia.crearSugerencia()
#     return jsonify({"message": "Sugerencia registrada con éxito"})

# @atencion_bp.route("/sagregar/<int:id_sugerencia>", methods=["PUT"])
# def resolve_suggestion(id_sugerencia):
#     # Lógica para actualizar una sugerencia
#     sugerencia = SugerenciasService(None, None, None)
#     sugerencia.actualizarEstado(id_sugerencia)
#     return jsonify({"message": "Sugerencia resuelta con éxito"})
