from src.models.reportes.reportesModels import ReportesModelo
from src.services.fidelizacion.fidelizacionService import (
    ObtenerInfoClientesPuntosService,
)
from datetime import datetime
from src.db import get_connection
import json
from pymysql.cursors import DictCursor  # Importar DictCursor
from src.models.reportes.reportesDTO import VentaDTO  # Importar VentaDTO
from src.db import get_connection  # Importar la conexión a la base de datos 


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
                    "ultima_actualizacionPuntos": dato[
                        "ultima_actualizacionPuntos"
                    ].split("T")[0],
                }
                for dato in datos_puntos
                if dato["ultima_actualizacionPuntos"].split("T")[0] == fecha_reporte
            ]

            # Si no hay datos para la fecha proporcionada
            if not datos_filtrados:
                return {
                    "mensaje": f"No se encontraron puntos para la fecha {fecha_reporte}"
                }

            return datos_filtrados
        else:
            return {"error": datos_puntos}


    @staticmethod
    def crear_reporte_ventas(fecha_reporte):
        """
        Genera un reporte de ventas filtrado por una fecha específica.

        :param fecha_reporte: Fecha en formato 'YYYY-MM-DD' para filtrar las ventas.
        """
        conexion = get_connection()
        cursor = conexion.cursor(DictCursor)
        try:
            # Consultar las ventas del día
            cursor.execute("""
                SELECT v.id_venta, v.total_venta, v.fecha_venta, c.nombre AS cliente, e.nombre AS empleado
                FROM ventas v
                JOIN clientes c ON v.id_cliente = c.id_cliente
                JOIN empleados e ON v.id_empleado = e.id_empleado
                WHERE DATE(v.fecha_venta) = %s
            """, (fecha_reporte,))
            ventas = cursor.fetchall()

            if not ventas:
                return {"mensaje": f"No se encontraron ventas para la fecha {fecha_reporte}"}

            # Procesar cada venta y obtener detalles
            reporte = []
            for venta in ventas:
                cursor.execute("""
                    SELECT nombre_producto, precio_unitario, cantidad
                    FROM detalle_ventas
                    WHERE id_venta = %s
                """, (venta["id_venta"],))
                detalles = cursor.fetchall()

                venta_dto = VentaDTO(
                    id_venta=venta["id_venta"],
                    total_venta=venta["total_venta"],
                    fecha_venta=venta["fecha_venta"],
                    cliente=venta["cliente"],
                    empleado=venta["empleado"],
                    detalles=detalles,
                )
                reporte.append(venta_dto.to_dict())

            return reporte
        finally:
            conexion.close()

# prueba de funcionalidad fecha del reporte
# print("Prueba con fecha específica")
# fecha_prueba = "2024-11-21"  # Cambia esta fecha para tus pruebas
# reporte = ReportesService.crear_reporte_puntos(fecha_prueba)
# print(reporte)
