from src.models.ventas.VentasModelos import VentaModelo, DetalleVentaModelo
from src.models.ventas.VentasDTOs import VentaDTO, DetalleVentasDTO
from pymysql.cursors import DictCursor
from dataclasses import dataclass
from src.db import get_connection
from decimal import Decimal


@dataclass
class VentaServicio(VentaModelo):

    def calcularTotalVenta(self, venta: VentaDTO) -> float:

        totalVenta = 0

        for producto in venta.detalles_venta:
            totalVenta += producto.precio_unitario

        return totalVenta

    def agregarVenta(self, venta: VentaDTO):
        connection = get_connection()
        cursor = connection.cursor(DictCursor)

        # Insertar la venta
        cursor.execute(
            "INSERT INTO ventas (total_venta, fecha_venta, metodo_pago, id_cliente, id_empleado) VALUES (%s, %s, %s, %s, %s)",
            (
                venta.total_venta,
                venta.fecha_venta,
                venta.metodo_pago,
                venta.id_cliente,
                venta.id_empleado,
            ),
        )

        # Obtener el id de la venta recién insertada
        venta_id = cursor.lastrowid

        # Insertar los detalles de la venta
        for detalle in venta.detalles_venta:
            cursor.execute(
                "INSERT INTO detalles_venta (id_venta, nombre_producto, codigo_producto, precio_unitario, categoria_producto) "
                "VALUES (%s, %s, %s, %s, %s)",
                (
                    venta_id,
                    detalle.nombre_producto,
                    detalle.codigo_producto,
                    detalle.precio_unitario,
                    detalle.categoria_producto,
                ),
            )

        connection.commit()
        connection.close()
