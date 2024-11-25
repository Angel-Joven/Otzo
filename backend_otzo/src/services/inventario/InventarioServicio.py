from src.models.inventario.InventarioModelos import (
    InventarioModelo,
    DetalleInventarioModelo,
)
from src.models.inventario.InventarioDTOs import InventarioDTO, DetalleInventarioDTO

from dataclasses import dataclass
from src.db import get_connection
from decimal import Decimal
from pymysql.cursors import DictCursor


@dataclass
class InventarioServicio(InventarioModelo):
    def agregarTipoProducto(self, tipo_producto: InventarioDTO) -> bool:
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            conexion.begin()

            cursor.execute(
                "SELECT 1 FROM inventario WHERE nombre_producto = %s",
                tipo_producto.nombre_producto,
            )

            resultado = cursor.fetchone()

            if resultado:
                raise Exception("No se puede agregar un producto que ya existe")

            cursor.execute(
                "INSERT INTO inventario (nombre_producto, imagen_producto, categoria_producto, cantidad_producto, descripcion_producto, precio_unitario, descontinuado) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    tipo_producto.nombre_producto,
                    tipo_producto.imagen_producto,
                    tipo_producto.categoria_producto,
                    tipo_producto.cantidad_producto,
                    tipo_producto.descripcion_producto,
                    tipo_producto.precio_unitario,
                    tipo_producto.descontinuado,
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
                "UPDATE inventario SET nombre_producto = %s, imagen_producto = %s, categoria_producto = %s, cantidad_producto = %s, descripcion_producto = %s, precio_unitario = %s, descontinuado = %s WHERE id_inventario = %s",
                (
                    datos_producto.nombre_producto,
                    datos_producto.imagen_producto,
                    datos_producto.categoria_producto,
                    datos_producto.cantidad_producto,
                    datos_producto.descripcion_producto,
                    datos_producto.precio_unitario,
                    datos_producto.descontinuado,
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
