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
from src.models.reportes.reportesDTO import QuejasReporteDTO
from src.models.reportes.reportesDTO import InventarioReporteDTO

class ReportesService(ReportesModelo):
    @staticmethod
    def crear_reporte_puntos():
        """
        Genera un reporte de puntos para todos los clientes.
        """
        datos_puntos = ObtenerInfoClientesPuntosService().obtener_info_clientes_puntos()

        if isinstance(datos_puntos, list):
            reporte = []
            for dato in datos_puntos:
                # Convertir la fecha al formato YYYY-MM-DD
                ultima_actualizacion = dato.get("ultima_actualizacionPuntos")
                if ultima_actualizacion:
                    try:
                        # Asegurarse de que sea un objeto datetime antes de convertir
                        fecha_iso = datetime.fromisoformat(ultima_actualizacion).date().isoformat()
                    except ValueError:
                        fecha_iso = ultima_actualizacion.split("T")[0]  # Fallback si no es válida

                reporte.append({
                    "idcliente_puntos": dato["idcliente_puntos"],
                    "total_puntos": dato["total_puntos"],
                    "ultima_actualizacionPuntos": fecha_iso,
                })

            return reporte
        else:
            return {"error": datos_puntos}

    @staticmethod
    def generar_reporte_ventas():
        """
        Genera un reporte de todas las ventas registradas, incluyendo sus detalles.
        """
        try:
            # Conexión a la base de datos
            conexion = get_connection()
            cursor = conexion.cursor()

            # Consultar todas las ventas con datos relacionados
            cursor.execute("""
                SELECT v.id_venta, v.total_venta, v.fecha_venta, c.nombre AS cliente, e.nombre AS empleado
                FROM ventas v
                LEFT JOIN clientes c ON v.id_cliente = c.id_cliente
                LEFT JOIN empleados e ON v.id_empleado = e.id_empleado
            """)
            ventas = cursor.fetchall()

            # Verificar si hay ventas registradas
            if not ventas:
                return {"mensaje": "No se encontraron ventas registradas."}

            # Generar el reporte con los detalles de cada venta
            reporte = []
            for venta in ventas:
                cursor.execute("""
                    SELECT nombre_producto, precio_unitario, cantidad
                    FROM detalle_ventas
                    WHERE id_venta = %s
                """, (venta[0],))
                detalles = cursor.fetchall()

                reporte.append({
                    "id_venta": venta[0],
                    "total_venta": venta[1],
                    "fecha_venta": venta[2],
                    "cliente": venta[3] or "Sin asignar",
                    "empleado": venta[4] or "Sin asignar",
                    "detalles": [
                        {
                            "nombre_producto": detalle[0],
                            "precio_unitario": detalle[1],
                            "cantidad": detalle[2]
                        }
                        for detalle in detalles
                    ]
                })

            # Retornar el reporte como lista de diccionarios
            return reporte
        except Exception as e:
            raise Exception(f"Error al generar el reporte de ventas: {str(e)}")
        finally:
            # Asegurar que la conexión se cierre
            if 'conexion' in locals():
                conexion.close()

    @staticmethod
    def crear_reporte_inventario():
        """
        Genera un reporte de inventario con los campos:
        id_producto, id_inventario, nombre_producto, cantidad_producto y categoría.
        """
        conexion = get_connection()
        try:
            with conexion.cursor(DictCursor) as cursor:
                query = """
                    SELECT 
                        i.id_inventario,
                        i.nombre_producto,
                        i.cantidad_producto,
                        i.categoria_producto AS categoria
                    FROM inventario i
                """
                cursor.execute(query)
                resultados = cursor.fetchall()

                # Transformar resultados al formato DTO
                reporte = [
                    InventarioReporteDTO(
                        id_inventario=row["id_inventario"],
                        nombre_producto=row["nombre_producto"],
                        cantidad_producto=row["cantidad_producto"],
                        categoria=row["categoria"]  # Ajuste para mapear la categoría.
                    ).to_dict()
                    for row in resultados
                ]

                return reporte
        except Exception as e:
            return {"error": f"Error al generar el reporte de inventario: {str(e)}"}
        finally:
            conexion.close()

    @staticmethod
    def crear_reporte_quejas():
        """
        Genera un reporte de quejas con los campos: categoría, estado, fechaHora, idQueja.
        """
        conexion = get_connection()
        try:
            with conexion.cursor(DictCursor) as cursor:
                query = """
                    SELECT 
                        idQueja AS id_queja,
                        categoria,
                        estado,
                        fechaHora
                    FROM quejas
                """
                cursor.execute(query)
                resultados = cursor.fetchall()

                # Formatear el reporte
                reporte = [
                    {
                        "idQueja": row["id_queja"],
                        "categoria": row["categoria"],
                        "estado": row["estado"],
                        "fechaHora": row["fechaHora"].isoformat()  # Convertir a formato ISO
                    }
                    for row in resultados
                ]

                return reporte
        except Exception as e:
            return {"error": f"Error al generar el reporte de quejas: {str(e)}"}
        finally:
            conexion.close()

# prueba de funcionalidad fecha del reporte
# print("Prueba con fecha específica")
# fecha_prueba = "2024-11-21"  # Cambia esta fecha para tus pruebas
# reporte = ReportesService.crear_reporte_puntos(fecha_prueba)
# print(reporte)