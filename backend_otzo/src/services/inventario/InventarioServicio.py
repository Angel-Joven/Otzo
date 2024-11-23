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

            cursor.execute(
                "INSERT INTO inventario (nombre_producto, imagen_producto, categoria_producto, cantidad_producto, descripcion_producto) VALUES (%s, %s, %s, %s, %s)",
                (
                    tipo_producto.nombre_producto,
                    tipo_producto.imagen_producto,
                    tipo_producto.categoria_producto,
                    tipo_producto.cantidad_producto,
                    tipo_producto.descripcion_producto,
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

    def actualizarTipoProducto(self):
        pass

    def eliminarTipoProducto(self):
        pass

    def listarTipoProductos(self) -> dict:
        try:
            conexion = get_connection()
            cursor = conexion.cursor(DictCursor)

            cursor.execute("SELECT * FROM inventario")

            return cursor.fetchall()

        except Exception as e:
            print("No se pudo conectar a la base de datos, error:", e)
            return None
        finally:
            conexion.close()
