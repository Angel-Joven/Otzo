from src.models.ventas.VentasModelos import VentaModelo, DetalleVentaModelo
from src.models.ventas.VentasDTOs import VentaDTO, DetalleVentaDTO
from pymysql.cursors import DictCursor
from dataclasses import dataclass
from src.db import get_connection


@dataclass
class VentaServicio(VentaModelo):
    def calcularTotalVenta(self, productos: list[dict]) -> float:
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            precio_total = 0

            conexion.begin()

            for producto in productos:

                print("PRODUCTO: ", producto)

                cursor.execute(
                    "SELECT precio_unitario from inventario where id_inventario = %s",
                    producto["id_inventario"],
                )

                precio_producto = int(producto["cantidad"]) * float(
                    cursor.fetchone()["precio_unitario"]
                )

                print("PRECIO PRODUCTO: ", precio_producto)

                precio_total += precio_producto

                print("PRECIO TOTAL:", precio_total)

            return precio_total

        except Exception as e:
            print("No se pudo calcular el precio total, error:", e)
            return None
        finally:
            conexion.close()

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

                cursor.execute(
                    "UPDATE detalle_inventario SET vendido = 1 WHERE codigo_producto = %s",
                    detalle_venta.codigo_producto,
                )

                # ACTUALIZAR STOCK

                cursor.execute(
                    "SELECT id_inventario FROM detalle_inventario WHERE codigo_producto = %s",
                    detalle_venta.codigo_producto,
                )

                id_inventario = cursor.fetchone()["id_inventario"]

                cursor.execute(
                    "UPDATE inventario SET cantidad_producto = cantidad_producto - 1 WHERE id_inventario = %s",
                    id_inventario,
                )

            conexion.commit()

            return True

        except Exception as e:
            print("No se pudo agregar la venta, error:", e)
            conexion.rollback()
            return False
        finally:
            conexion.close()

    def listarVentasDeUsuario(self, id_cliente: int):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            cursor.execute("SELECT * FROM ventas where id_cliente = %s", id_cliente)

            return cursor.fetchall()

        except Exception as e:
            print("No se pudo conectar a la base de datos, error:", e)
            conexion.rollback()
            return None
        finally:
            conexion.close()


@dataclass
class DetalleVentaServicio(DetalleVentaModelo):
    def devolverProducto(
        self, id_inventario: int, id_detalle: int, codigo_producto: str
    ):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute(
                "UPDATE detalle_inventario SET vendido = 0 WHERE codigo_producto = %s",
                codigo_producto,
            )

            cursor.execute(
                "UPDATE inventario SET cantidad_producto = cantidad_producto + 1 WHERE id_inventario = %s",
                id_inventario,
            )

            cursor.execute(
                "UPDATE detalle_ventas SET devuelto = 1 where id_detalle_venta = %s",
                id_detalle,
            )

            conexion.commit()

            return True

        except Exception as e:
            print("No se pudieron llenar los datos de detalles venta, error:", e)
            return False
        finally:
            conexion.close()

    def llenarDatos(self, productos: list[dict]) -> list[DetalleVentaDTO]:
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            detalles_venta = []

            conexion.begin()

            for producto in productos:

                id_inventario = int(producto["id_inventario"])
                cantidad = int(producto["cantidad"])

                cursor.execute(
                    "SELECT nombre_producto from inventario where id_inventario = %s",
                    id_inventario,
                )

                nombre_producto = str(cursor.fetchone()["nombre_producto"])

                cursor.execute(
                    "SELECT precio_unitario from inventario where id_inventario = %s",
                    id_inventario,
                )

                precio_unitario = float(cursor.fetchone()["precio_unitario"])

                cursor.execute(
                    "SELECT categoria_producto from inventario where id_inventario = %s",
                    id_inventario,
                )

                categoria_producto = str(cursor.fetchone()["categoria_producto"])

                cursor.execute(
                    "select codigo_producto from detalle_inventario where id_inventario = %s and vendido = 0",
                    id_inventario,
                )

                codigos_productos = [
                    row["codigo_producto"] for row in cursor.fetchall()[:cantidad]
                ]

                for i in range(cantidad):
                    detalle_venta = DetalleVentaDTO(
                        nombre_producto,
                        codigos_productos[i],
                        categoria_producto,
                        id_inventario,
                        precio_unitario,
                        False,
                    )

                    detalles_venta.append(detalle_venta)

            return detalles_venta

        except Exception as e:
            print("No se pudieron llenar los datos de detalles venta, error:", e)
            return None
        finally:
            conexion.close()

    def listarDetallesDeVenta(self, id_venta: int) -> dict:
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            cursor.execute(
                "SELECT * FROM detalle_ventas where id_venta = %s",
                id_venta,
            )

            return cursor.fetchall()

        except Exception as e:
            print("No se pudo conectar a la base de datos, error:", e)
            conexion.rollback()
            return None
        finally:
            conexion.close()

    def listarVariosDetallesDeVentas(self, ids_ventas: list[int]):

        # lista_detalles_ventas = [{"id_venta": 1, "detalles_venta": [{}]}]
        lista_detalles_ventas = []

        print(ids_ventas)

        for id_venta in ids_ventas:
            detalles_de_la_venta = self.listarDetallesDeVenta(id_venta)

            print(detalles_de_la_venta)

            if not detalles_de_la_venta:
                return None

            lista_detalles_ventas.append(
                {"id_venta": id_venta, "detalles_venta": detalles_de_la_venta}
            )

        print(lista_detalles_ventas)

        return lista_detalles_ventas
