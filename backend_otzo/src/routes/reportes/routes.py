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

@reportes_bp.route("/reporte-puntos", methods=["GET"])
def generar_reporte_puntos():
    try:
        fecha_reporte = request.args.get("fecha")  # Obtener fecha desde los parámetros de consulta
        if not fecha_reporte:
            return jsonify({"error": "La fecha es obligatoria"}), 400
        
        reporte = ReportesService.crear_reporte_puntos(fecha_reporte)
        return jsonify(reporte), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

@reportes_bp.route("/reporte-ventas", methods=["GET"])
def generar_reporte_ventas():
    try:
        fecha_reporte = request.args.get("fecha")  # Obtener fecha desde los parámetros de consulta
        if not fecha_reporte:
            return jsonify({"error": "La fecha es obligatoria"}), 400

        reporte = ReportesService.crear_reporte_ventas(fecha_reporte)
        return jsonify(reporte), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
