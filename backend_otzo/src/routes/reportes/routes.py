from flask import request, jsonify, Response
from . import reportes_bp
from src.services.reportes.reportesService import *
from src.db import get_connection
from src.utils.Logger import Logger
from pymysql.cursors import DictCursor
from datetime import datetime

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
    """
    Genera un reporte de ventas sin necesidad de filtrar por fecha.
    """
    try:
        # Conexión a la base de datos
        conexion = get_connection()
        cursor = conexion.cursor(DictCursor)

        # Consultar todas las ventas
        cursor.execute("""
            SELECT v.id_venta, v.total_venta, v.fecha_venta, c.nombre AS cliente, e.nombre AS empleado
            FROM ventas v
            JOIN clientes c ON v.id_cliente = c.id_cliente
            JOIN empleados e ON v.id_empleado = e.id_empleado
        """)
        ventas = cursor.fetchall()

        if not ventas:
            return jsonify({"mensaje": "No se encontraron ventas registradas."}), 200

        # Procesar cada venta y obtener detalles
        reporte = []
        for venta in ventas:
            cursor.execute("""
                SELECT nombre_producto, precio_unitario, cantidad
                FROM detalle_ventas
                WHERE id_venta = %s
            """, (venta["id_venta"],))
            detalles = cursor.fetchall()

            reporte.append({
                "id_venta": venta["id_venta"],
                "total_venta": venta["total_venta"],
                "fecha_venta": venta["fecha_venta"],
                "cliente": venta["cliente"],
                "empleado": venta["empleado"],
                "detalles": detalles,
            })

        return jsonify(reporte), 200
    except Exception as e:
        return jsonify({"error": f"Error al generar el reporte de ventas: {str(e)}"}), 500
    finally:
        if 'conexion' in locals():
            conexion.close()

# ---------------------------------------------------------------------------------------------------------------------------

@reportes_bp.route("/reporte-rangos", methods=["GET"])
def generar_reporte_rangos():
    """
    Genera un reporte con los rangos y la cantidad de clientes en cada uno.
    """
    conexion = get_connection()
    try:
        with conexion.cursor(DictCursor) as cursor:
            query = """
                SELECT r.nombre_rango, COUNT(p.idclientes_puntos) AS total_personas
                FROM puntos p
                JOIN rangos r WHERE p.idrango = r.idrango                              
                GROUP BY r.nombre_rango
                ORDER BY total_personas DESC
            """
            cursor.execute(query)
            resultado = cursor.fetchall()
            return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": f"Error al generar el reporte: {str(e)}"}), 500
    finally:
        conexion.close()
# linea 65 where > on 
# ---------------------------------------------------------------------------------------------------------------------------

@reportes_bp.route("/reporte-administracion", methods=["GET"])
def generar_reporte_administracion():
    """
    Genera un reporte con las áreas de trabajo, el número de empleados en cada una,
    y los ID de los empleados.
    """
    conexion = get_connection()
    try:
        with conexion.cursor(DictCursor) as cursor:
            query = """
                SELECT 
                    area_Trabajo AS area,
                    COUNT(id_empleado) AS total_empleados,
                    GROUP_CONCAT(id_empleado) AS empleados
                FROM administracion
                GROUP BY area_Trabajo
                ORDER BY total_empleados DESC
            """
            cursor.execute(query)
            resultado = cursor.fetchall()
            return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": f"Error al generar el reporte: {str(e)}"}), 500
    finally:
        conexion.close()

# ---------------------------------------------------------------------------------------------------------------------------

@reportes_bp.route("/reporte-quejas", methods=["GET"])
def generar_reporte_quejas():
    """
    Genera un reporte de quejas agrupadas por categoría.
    """
    try:
        reporte = ReportesService.crear_reporte_quejas()
        return jsonify(reporte), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

@reportes_bp.route("/reporte-inventario", methods=["GET"])
def generar_reporte_inventario():
    """
    Genera un reporte del inventario.
    """
    try:
        reporte = ReportesService.crear_reporte_inventario()
        return jsonify(reporte), 200
    except Exception as e:
        return jsonify({"error": f"Error al generar el reporte de inventario: {str(e)}"}), 500
