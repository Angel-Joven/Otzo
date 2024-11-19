from flask import request, jsonify, Response
from pymysql.cursors import DictCursor
from src.db import get_connection
from datetime import datetime
from decimal import Decimal
from . import ventas_bp  # Importa el Blueprint de inventario
import json
from flask_cors import cross_origin

from src.models.inventario.inventarioDTO import inventarioDTO

def custom_json_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)  
    elif isinstance(obj, datetime):
        return obj.isoformat()  
    return str(obj)  


@inventario_bp.route("/", methods=["GET"])
def index():
    conexion = get_connection()
    cursor = conexion.cursor(DictCursor)

    cursor.execute(
        "SELECT * FROM inventario",
    )

    resultado = cursor.fetchall()
    conexion.close()

   json_data = json.dumps(
        {"inventario": resultado}, ensure_ascii=False, default=custom_json_serializer
    )
    return Response(json_data, content_type="application/json; charset=utf-8")

@inventario_bp.route("/test", methods=["POST", "OPTIONS"])
@cross_origin()
def test():
    data = request.json

    inventario = []

    for producto in data["inventario"]:

        # TODO: FUNCION QUE AL PASAR UN NOMBRE DE PRODUCTO Y LA CANTIDAD, RETORNE
        # UNA LISTA DE DICCIONARIOS CON TODOS LOS CAMPOS POR CADA PRODUCTO Y SI NO HAY SUFICIENTE CANTIDAD
        # QUE RETORNE NONE -----FUNCIONALIDAD DE INVENTARIO-----

        print(producto)
    

    return jsonify({"Mensaje": "producto agregado correctamente"}), 200



