from src.models.reportes.reportesModels import obtener_reporte_mas_reciente
from src.models.reportes.reportesDTO import ReporteDTO
from flask import request,jsonify 
from . import reportes_bp
import json

@reportes_bp.route('/reporte_diario', methods=['GET'])
def obtener_reporte_diario():
    """Devuelve el último reporte generado."""
    reporte_db = obtener_reporte_mas_reciente()
    
    if not reporte_db:
        return jsonify({"mensaje": "No hay reportes disponibles"}), 404

    reporte = ReporteDTO(
        fecha_generacion=reporte_db["fecha_generacion"],
        clientes=json.loads(reporte_db["reporte"])
    )
    return jsonify(reporte.to_dict())