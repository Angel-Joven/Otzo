from flask import request, jsonify, Response
from . import reportes_bp
from src.services.reportes.reportesService import *
from src.db import get_connection

from src.utils.Logger import Logger
from pymysql.cursors import DictCursor

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para saber si está funcionando nuestra API
@reportes_bp.route("/", methods=["GET"])
def index():
    try:
        return jsonify({"mensaje": "Hola - Reportes"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------