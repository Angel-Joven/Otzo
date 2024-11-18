from src.models.inventario.inventarioModels import InventarioModelo
from src.models.inventario.inventarioDTO import inventarioDTO
from src.db import get_connection
from pymysql.cursors import DictCursor
from dataclasses import dataclass
from decimal import Decimal
    

@dataclass
class inventarioService(InventarioModelo):
    def agregarProducto(self, producto: inventarioDTO):
        pass

        conexion = get_connection()
        cursor = conexion.cursor(DictCursor)

        PRODUCTOS_DISPONIBLES = {}
        CANTIDAD_PRODUCTOS = {}

        for producto in inventario:
            print(producto.nombre_producto)
              cursor.execute(
                  "SELECT COUNT(nombre_producto) FROM inventario WHERE nombre_producto = (%s)",
                  producto.nombre_producto,
              )

              resultado = cursor.fetchone()

              resultado = next(iter(resultado.items()))

              cantidad = resultado[1]

                print(cantidad)

              if producto.nombre_producto not in PRODUCTOS_DISPONIBLES:
                  PRODUCTOS_DISPONIBLES[producto.nombre_producto] = cantidad

              if producto.nombre_producto not in CANTIDAD_PRODUCTOS:
                  CANTIDAD_PRODUCTOS[producto.nombre_producto] = 1
              else:
                  CANTIDAD_PRODUCTOS[producto.nombre_producto] += 1

              print(CANTIDAD_PRODUCTOS)
              print(PRODUCTOS_DISPONIBLES)

          conexion.close()


