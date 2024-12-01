from src.models.ventas.VentasModelos import VentaModelo, DetalleVentaModelo
from src.models.ventas.VentasDTOs import VentaDTO, DetalleVentaDTO
from pymysql.cursors import DictCursor
from dataclasses import dataclass
from src.db import get_connection


@dataclass
class VentaServicio(VentaModelo):
    def agregarVenta(self, venta: VentaDTO):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute(
                "INSERT INTO ventas (monto_recibido, total_venta, fecha_venta, metodo_pago, id_cliente, id_empleado) VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    venta.monto_recibido,
                    venta.total_venta,
                    venta.fecha_venta,
                    venta.metodo_pago,
                    venta.id_cliente,
                    venta.id_empleado,
                ),
            )

            id_venta = cursor.lastrowid

            for detalle_venta in venta.detalles_venta:
                cursor.execute(
                    "INSERT INTO detalle_ventas (id_venta, id_producto, nombre_producto, codigo_producto, precio_unitario, categoria_producto, devuelto) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        id_venta,
                        detalle_venta.id_producto,
                        detalle_venta.nombre_producto,
                        detalle_venta.codigo_producto,
                        detalle_venta.precio_unitario,
                        detalle_venta.categoria_producto,
                        detalle_venta.devuelto,
                    ),
                )

            conexion.commit()

            return True

        except Exception as e:
            print("No se pudo agregar la venta, error:", e)
            conexion.rollback()
            return False
        finally:
            conexion.close()
