from src.models.ventas.VentasModelos import VentaModelo, DetalleVentaModelo
from src.models.ventas.VentasDTOs import VentaDTO, DetalleVentaDTO
from pymysql.cursors import DictCursor
from dataclasses import dataclass
from src.db import get_connection
from decimal import Decimal


@dataclass
class VentaServicio(VentaModelo):

    def obtenerDatosProductos(self, productos: dict):
        conexion = get_connection()
        cursor = conexion.cursor(DictCursor)

        # TODO: LOGICA PARA OBTENER LOS DATOS

        conexion.close()

    def calcularTotalVenta(self, venta: VentaDTO) -> float:

        totalVenta = 0

        for producto in venta.detalles_venta:
            totalVenta += producto.precio_unitario

        return totalVenta

    def calcularCantidadVenta(self, detallesVenta: list[DetalleVentaDTO]) -> dict:
        cantidad_por_producto = {}

        for producto in detallesVenta:
            if producto.nombre_producto not in cantidad_por_producto:
                cantidad_por_producto[producto.nombre_producto] = 1
            else:
                cantidad_por_producto[producto.nombre_producto] += 1

        return cantidad_por_producto

    def agregarVenta(self, venta: VentaDTO):
        pass
        # conexion = get_connection()
        # cursor = conexion.cursor(DictCursor)

        # PRODUCTOS_DISPONIBLES = {}
        # CANTIDAD_PRODUCTOS = {}

        # for producto in venta.detalles_venta:
        #     print(producto.nombre_producto)
        #     cursor.execute(
        #         "SELECT COUNT(nombre_producto) FROM inventario WHERE nombre_producto = (%s)",
        #         producto.nombre_producto,
        #     )

        #     resultado = cursor.fetchone()

        #     resultado = next(iter(resultado.items()))

        #     cantidad = resultado[1]

        #     # print(cantidad)

        #     if producto.nombre_producto not in PRODUCTOS_DISPONIBLES:
        #         PRODUCTOS_DISPONIBLES[producto.nombre_producto] = cantidad

        #     if producto.nombre_producto not in CANTIDAD_PRODUCTOS:
        #         CANTIDAD_PRODUCTOS[producto.nombre_producto] = 1
        #     else:
        #         CANTIDAD_PRODUCTOS[producto.nombre_producto] += 1

        #     print(CANTIDAD_PRODUCTOS)
        #     print(PRODUCTOS_DISPONIBLES)

        # conexion.close()
        # Insertar la venta
        # cursor.execute(
        #     "INSERT INTO ventas (total_venta, fecha_venta, metodo_pago, id_cliente, id_empleado) VALUES (%s, %s, %s, %s, %s)",
        #     (
        #         venta.total_venta,
        #         venta.fecha_venta,
        #         venta.metodo_pago,
        #         venta.id_cliente,
        #         venta.id_empleado,
        #     ),
        # )

        # Obtener el id de la venta recién insertada
        # venta_id = cursor.lastrowid

        # Insertar los detalles de la venta
        # for detalle in venta.detalles_venta:
        #     cursor.execute(
        #         "INSERT INTO detalles_venta (id_venta, nombre_producto, codigo_producto, precio_unitario, categoria_producto) "
        #         "VALUES (%s, %s, %s, %s, %s)",
        #         (
        #             venta_id,
        #             detalle.nombre_producto,
        #             detalle.codigo_producto,
        #             detalle.precio_unitario,
        #             detalle.categoria_producto,
        #         ),
        #     )

        # connection.commit()
        # connection.close()
