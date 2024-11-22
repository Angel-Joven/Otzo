from src.models.reportes.reportesModels import ReportesModelo
from src.services.fidelizacion.fidelizacionService import ObtenerInfoClientesPuntosService
from datetime import datetime
from src.db import get_connection
import json

class ReportesService(ReportesModelo):
    @staticmethod
    def crear_reporte_puntos(fecha_reporte):
        """
        Genera un reporte de puntos filtrado por una fecha específica.
        
        :param fecha_reporte: Fecha en formato 'YYYY-MM-DD' para filtrar los puntos.
        """
        datos_puntos = ObtenerInfoClientesPuntosService().obtener_info_clientes_puntos()

        if isinstance(datos_puntos, list):
            # Filtrar los datos por la fecha proporcionada
            datos_filtrados = [
                {
                    "idcliente_puntos": dato["idcliente_puntos"],
                    "total_puntos": dato["total_puntos"],
                    "ultima_actualizacionPuntos": dato["ultima_actualizacionPuntos"].split("T")[0],
                }
                for dato in datos_puntos
                if dato["ultima_actualizacionPuntos"].split("T")[0] == fecha_reporte
            ]

            # Si no hay datos para la fecha proporcionada
            if not datos_filtrados:
                return {"mensaje": f"No se encontraron puntos para la fecha {fecha_reporte}"}

            return datos_filtrados
        else:
            return {"error": datos_puntos}

#prueba de funcionalidad fecha del reporte 
print("Prueba con fecha específica")
fecha_prueba = "2024-11-21"  # Cambia esta fecha para tus pruebas
reporte = ReportesService.crear_reporte_puntos(fecha_prueba)
print(reporte)