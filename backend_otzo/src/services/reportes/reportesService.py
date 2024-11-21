from datetime import datetime
from reportesModels import obtener_datos_puntos, guardar_reporte_diario
from reportesDTO import ReporteDTO

def generar_reporte_diario():
    """Genera el reporte diario de puntos."""
    datos_puntos = obtener_datos_puntos()

    # Crear el DTO del reporte
    reporte = ReporteDTO(
        fecha_generacion=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        clientes=[punto.to_dict() for punto in datos_puntos]
    )

    # Guardar el reporte en la base de datos
    guardar_reporte_diario(reporte)
    return reporte
