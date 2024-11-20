# Rutas para el Modulo de Administracion
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from flask import request, jsonify, Response
from . import administracion_bp # Importar el Blueprint de Administracion
from src.services.administracion.administracionService import *
from src.db import get_connection

from src.utils.Logger import Logger
from pymysql.cursors import DictCursor

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para saber si esta funcionando nuestra api
@administracion_bp.route("/", methods=["GET"])
def index():
    try:
        return jsonify({"mensaje": "Hola - Administracion"}), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------
