from src.services.fidelizacion.fidelizacionService import ObtenerInfoClientesPuntosService
from datetime import datetime
from src.models.reportes.reportesModels import obtener_datos_puntos, guardar_reporte_diario
from src.models.reportes.reportesDTO import ReporteDTO

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

def crear_reporte_puntos(fecha_dia):
    datos_puntos=ObtenerInfoClientesPuntosService().obtener_info_clientes_puntos()
    clientes=datos_puntos[0]
    puntos=datos_puntos[2]
    ultima_fecha_actualizacion_puntos=datos_puntos[3]
    print("prueba 1")
    print(clientes)

crear_reporte_puntos(fecha_dia="1")
print("hola")