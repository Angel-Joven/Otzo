from src.models.ventas.VentasModels import VentaModelo, DetalleVentaModelo

from src.db import get_connection

from datetime import datetime


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
        self.posible = True

    def calcularTotal(self) -> float:

        connection = get_connection()

        for producto in self.productos:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT precio_unitario FROM inventario where nombre_producto = (%s)",
                    str(producto["nombre_producto"]),
                )
                resultado = cursor.fetchone()

                if resultado is None:
                    print(
                        f"El producto '{producto["nombre_producto"]}' no existe en el inventario."
                    )
                    self.posible = False
                    connection.close()
                    return None

                precio_unitario = resultado[0]

                producto["precio_unitario"] = precio_unitario

                cursor.execute(
                    "SELECT cantidad FROM inventario where nombre_producto = (%s)",
                    str(producto["nombre_producto"]),
                )

                resultado = cursor.fetchone()

                cantidad_disponible = resultado[0]

                if cantidad_disponible < producto["cantidad"]:
                    self.posible = False
                    print(
                        "No hay cantidad suficiente para el producto: ",
                        producto["nombre_producto"],
                    )
                    connection.close()
                    return None

                self.totalVenta += precio_unitario * producto["cantidad"]

        connection.close()

        return self.totalVenta

    def agregarVenta(self):
        self.calcularTotal()

        if self.totalVenta <= self.monto_recibido and self.posible:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO ventas (total_venta, fecha_venta, metodo_pago, id_cliente, id_trabajador) VALUES (%s, %s, %s, %s, %s)",
                    (
                        self.totalVenta,
                        datetime.now(),
                        self.metodo_pago,
                        self.id_cliente,
                        self.id_trabajador,
                    ),
                )

                id_venta = cursor.lastrowid

                for producto in self.productos:
                    cursor.execute(
                        "INSERT INTO detalle_ventas (id_venta, nombre_producto, codigo_producto, precio_unitario, categoria_producto, cantidad) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (
                            id_venta,
                            producto["nombre_producto"],
                            producto["codigo_producto"],
                            producto["precio_unitario"],
                            producto["categoria_producto"],
                            producto["devuelto"],
                        ),
                    )

                for producto in self.productos:
                    cursor.execute(
                        "UPDATE inventario SET cantidad = cantidad - (%s) where nombre_producto = (%s)",
                        (producto["cantidad"], producto["nombre_producto"]),
                    )

                connection.commit()
                connection.close()

                print("Venta hecha correctamente")


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
