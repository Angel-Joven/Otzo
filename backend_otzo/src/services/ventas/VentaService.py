from src.models.ventas.VentasModels import VentaModelo, DetalleVentaModelo

from src.db import get_connection


class VentaService(VentaModelo):
    def __init__(
        self,
        metodo_pago: str,
        monto_recibido: float,
        productos: dict,
        id_cliente: int,
        id_trabajador: int,
    ):
        self.metodo_pago = metodo_pago
        self.monto_recibido = monto_recibido
        self.productos = productos
        self.id_cliente = id_cliente
        self.id_trabajador = id_trabajador

        self.totalVenta = 0

    def calcularTotal(self) -> float:

        connection = get_connection()

        for producto in self.productos:
            cantidad = self.productos[producto]
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT precio_unitario FROM inventario where nombre_producto = (%s)",
                    str(producto),
                )
                resultado = cursor.fetchone()

                if resultado is None:
                    print(f"El producto '{producto}' no existe en el inventario.")
                    connection.close()
                    return None

                precio_unitario = resultado[0]

                self.totalVenta += precio_unitario * cantidad
        connection.close()
        return self.totalVenta

    def agregarVenta(self):
        connection = get_connection()


class DetalleVentaService(DetalleVentaModelo):
    def __init__(
        self,
        id_producto: str,
        nombre_producto: str,
        codigo_producto: str,
        precio_unitario: float,
        categoria_producto: str,
    ):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.codigo_producto = codigo_producto
        self.precio_unitario = precio_unitario
        self.categoria_producto = categoria_producto

    def devolverProducto(self):
        pass
