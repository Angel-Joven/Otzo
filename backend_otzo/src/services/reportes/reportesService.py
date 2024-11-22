from src.models.reportes.reportesModels import *
from src.services.fidelizacion.fidelizacionService import ObtenerInfoClientesPuntosService
from datetime import datetime
from src.db import get_connection
import json

class ReportesService(ReportesModelo):
    @staticmethod
    def crear_reporte_puntos():
        datos_puntos = ObtenerInfoClientesPuntosService().obtener_info_clientes_puntos()

        if isinstance(datos_puntos, list):
            datos_filtrados = [
                {
                    "idcliente_puntos": dato["idcliente_puntos"],
                    "total_puntos": dato["total_puntos"],
                    "ultima_actualizacionPuntos": dato["ultima_actualizacionPuntos"].split("T")[0],
                }
                for dato in datos_puntos
            ]
            print(json.dumps(datos_filtrados, indent=4, ensure_ascii=False))
        else:
            return {"error": datos_puntos}

print("prueba 1")
ReportesService.crear_reporte_puntos()
