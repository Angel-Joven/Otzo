from datetime import datetime
from src.models.fidelizacion.fidelizacionDTO import PuntosDTO, obtener_conexion

def obtener_datos_puntos():
    """Consulta los puntos de los clientes desde la base de datos y los convierte a DTOs."""
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
    SELECT 
        c.idclientes_puntos, 
        c.total_puntos, 
        c.ultima_actualizacionPuntos,
        r.nombre_rango,
        r.porcentaje_puntos
    FROM 
        clientes_puntos c
    JOIN 
        rangos r ON c.idrango = r.idrango
    WHERE 
        c.habilitado = 1;
    """
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()

    # Convertir resultados en DTOs
    datos_puntos = [
        PuntosDTO(
            idclientes_puntos=fila['idclientes_puntos'],
            idrango=fila['nombre_rango'],
            total_puntos=fila['total_puntos']
        )
        for fila in resultados
    ]
    return datos_puntos

def guardar_reporte_diario(reporte):
    """Guarda el reporte diario en la base de datos."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = """
    INSERT INTO ReportePuntos (fecha_generacion, reporte)
    VALUES (%s, %s)
    """
    data = (reporte.fecha_generacion, reporte.to_json())
    cursor.execute(query, data)
    conexion.commit()
    conexion.close()

def obtener_reporte_mas_reciente():
    """Obtiene el reporte más reciente de la base de datos."""
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ReportePuntos ORDER BY fecha_generacion DESC LIMIT 1")
    resultado = cursor.fetchone()
    conexion.close()
    return resultado