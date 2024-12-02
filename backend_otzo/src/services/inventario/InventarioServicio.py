from src.models.inventario.InventarioModelos import (
    InventarioModelo,
    DetalleInventarioModelo,
)
from src.models.inventario.InventarioDTOs import InventarioDTO, DetalleInventarioDTO

from dataclasses import dataclass
from src.db import get_connection
from pymysql.cursors import DictCursor
import string
import random
from datetime import datetime, timedelta


@dataclass
class InventarioServicio(InventarioModelo):
    def agregarTipoProducto(self, tipo_producto: InventarioDTO) -> bool:
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute(
                "SELECT 1 FROM inventario WHERE nombre_producto = %s OR descripcion_producto = %s",
                (tipo_producto.nombre_producto, tipo_producto.descripcion_producto),
            )

            resultado = cursor.fetchone()

            if resultado:
                raise Exception("No se puede agregar un producto que ya existe")

            cursor.execute(
                "INSERT INTO inventario (nombre_producto, imagen_producto, categoria_producto, cantidad_producto, descripcion_producto, precio_unitario, descontinuado, cantidad_maxima_producto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    tipo_producto.nombre_producto,
                    tipo_producto.imagen_producto,
                    tipo_producto.categoria_producto,
                    tipo_producto.cantidad_producto,
                    tipo_producto.descripcion_producto,
                    tipo_producto.precio_unitario,
                    tipo_producto.descontinuado,
                    tipo_producto.cantidad_maxima_producto,
                ),
            )

            conexion.commit()

            return True

        except Exception as e:
            print("No se pudo agregar un nuevo tipo de producto, error:", e)
            conexion.rollback()
            return False
        finally:
            conexion.close()

    def actualizarTipoProducto(self, datos_producto: InventarioDTO):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute(
                "UPDATE inventario SET nombre_producto = %s, imagen_producto = %s, categoria_producto = %s, cantidad_producto = %s, descripcion_producto = %s, precio_unitario = %s, descontinuado = %s, cantidad_maxima_producto = %s WHERE id_inventario = %s",
                (
                    datos_producto.nombre_producto,
                    datos_producto.imagen_producto,
                    datos_producto.categoria_producto,
                    datos_producto.cantidad_producto,
                    datos_producto.descripcion_producto,
                    datos_producto.precio_unitario,
                    datos_producto.descontinuado,
                    datos_producto.cantidad_maxima_producto,  # La cantidad máxima del producto
                    datos_producto.id_inventario,  # El identificador del producto
                ),
            )

            conexion.commit()

            return True

        except Exception as e:
            print("No se pudo actualizar el tipo de producto, error:", e)
            conexion.rollback()
            return False
        finally:
            conexion.close()

    def eliminarTipoProducto(self, tipo_producto: InventarioDTO):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute(
                "UPDATE inventario SET descontinuado = %s WHERE id_inventario = %s",
                (tipo_producto.descontinuado, tipo_producto.id_inventario),
            )

            resultado = cursor.fetchone()
            print(resultado)

            conexion.commit()

            return True

        except Exception as e:
            print("No se pudo conectar a la base de datos, error:", e)
            conexion.rollback()
            return None
        finally:
            conexion.close()

    def listarTipoProductos(self) -> dict:
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            cursor.execute("SELECT * FROM inventario where descontinuado = 0")

            return cursor.fetchall()

        except Exception as e:
            print("No se pudo conectar a la base de datos, error:", e)
            conexion.rollback()
            return None
        finally:
            conexion.close()

    def listarTipoProductosALaVenta(self) -> dict:
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            cursor.execute(
                "SELECT * FROM inventario where descontinuado = 0 and cantidad_producto > 0"
            )

            return cursor.fetchall()

        except Exception as e:
            print("No se pudo conectar a la base de datos, error:", e)
            conexion.rollback()
            return None
        finally:
            conexion.close()

    def listarTipoProductosDescontinuados(self) -> dict:
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            cursor.execute("SELECT * FROM inventario where descontinuado = 1")

            return cursor.fetchall()

        except Exception as e:
            print("No se pudo conectar a la base de datos, error:", e)
            conexion.rollback()
            return None
        finally:
            conexion.close()

    def listarCategoriasTiposProductos(self) -> dict:
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            cursor.execute(
                "SELECT DISTINCT categoria_producto FROM inventario where descontinuado = 0"
            )

            return cursor.fetchall()

        except Exception as e:
            print("No se pudo conectar a la base de datos, error:", e)
            conexion.rollback()
            return None
        finally:
            conexion.close()


@dataclass
class DetalleInventarioServicio(DetalleInventarioModelo):

    def generarCodigoProducto(self):
        letras_numeros = string.ascii_uppercase + string.digits
        codigo_producto = "".join(random.choices(letras_numeros, k=8))
        return codigo_producto

    def generarPrecioProducto(self, precio_maximo: float):
        precio_unitario = round(random.uniform(1, precio_maximo), 2)
        return precio_unitario

    def agregarProducto(self, id_tipo_producto: int, cantidad: int):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute(
                "SELECT precio_unitario FROM inventario WHERE id_inventario = %s",
                id_tipo_producto,
            )

            precio_producto = float(cursor.fetchone()["precio_unitario"])
            fecha_actual = datetime.now()
            fecha_caducidad = datetime.now() + timedelta(days=30)
            costo_unitario = self.generarPrecioProducto(precio_producto)

            cursor.execute(
                "SELECT cantidad_maxima_producto FROM inventario where id_inventario = %s",
                id_tipo_producto,
            )

            cantidad_maxima_producto = int(
                cursor.fetchone()["cantidad_maxima_producto"]
            )

            cursor.execute(
                "SELECT cantidad_producto FROM inventario WHERE id_inventario = %s",
                id_tipo_producto,
            )

            cantidad_actual = int(cursor.fetchone()["cantidad_producto"])

            print(cantidad_maxima_producto, cantidad_actual, cantidad)
            nueva_cantidad = cantidad_maxima_producto - cantidad_actual

            if cantidad_actual == cantidad_maxima_producto:
                raise Exception("Ya hay el stock maximo")

            if int(cantidad) <= nueva_cantidad:
                for i in range(int(cantidad)):
                    cursor.execute(
                        "INSERT INTO detalle_inventario (id_inventario, codigo_producto, fecha_producto, caducidad_producto, costo_unitario, vendido, devuelto) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (
                            id_tipo_producto,
                            self.generarCodigoProducto(),
                            fecha_actual,
                            fecha_caducidad,
                            costo_unitario,
                            False,
                            False,
                        ),
                    )

                cursor.execute(
                    "SELECT cantidad_producto FROM inventario WHERE id_inventario = %s",
                    id_tipo_producto,
                )

                cursor.execute(
                    "UPDATE inventario SET cantidad_producto = %s WHERE id_inventario = %s",
                    (
                        cantidad_actual + int(cantidad),
                        id_tipo_producto,
                    ),
                )
            else:
                for i in range(nueva_cantidad):
                    cursor.execute(
                        "INSERT INTO detalle_inventario (id_inventario, codigo_producto, fecha_producto, caducidad_producto, costo_unitario, vendido, devuelto) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (
                            id_tipo_producto,
                            self.generarCodigoProducto(),
                            fecha_actual,
                            fecha_caducidad,
                            costo_unitario,
                            False,
                            False,
                        ),
                    )

                cursor.execute(
                    "UPDATE inventario SET cantidad_producto = %s WHERE id_inventario = %s",
                    (
                        cantidad_maxima_producto,
                        id_tipo_producto,
                    ),
                )
            conexion.commit()

            return True

        except Exception as e:
            print("No se pudo agregar una nueva cantidad de productos, error:", e)
            conexion.rollback()
            return False
        finally:
            conexion.close()

    def actualizarProducto(self):
        pass

    def devolverProducto(self):
        pass

    def listarReabastecimientosPorDia(self):
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            cursor.execute(
                "SELECT fecha_producto AS dia_reabastecimiento, id_inventario, COUNT(*) AS cantidad_productos FROM detalle_inventario GROUP BY  dia_reabastecimiento, id_inventario ORDER BY dia_reabastecimiento, id_inventario;"
            )

            resultado = cursor.fetchall()

            return resultado

        except Exception as e:
            print("No se pudo conectar a la base de datos, error:", e)
            conexion.rollback()
            return None
        finally:
            conexion.close()
