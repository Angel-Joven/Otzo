from src.models.ventas.VentasModels import VentaModelo, DetalleVentaModelo
from src.services.fidelizacion.fidelizacionService import PuntosService, RangosService #Para calcular los puntos - FIDELIZACION

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

        #if self.totalVenta <= self.monto_recibido and self.posible:
            #connection = get_connection()

        #FIDELIZACION
        puntos_service = PuntosService()
        rangos_service = RangosService()

        #Pago con puntos - FIDELIZACION
        if self.metodo_pago.lower() == "puntos":
            resultado = puntos_service.descontar_puntos(self.id_cliente, self.totalVenta)
            if not resultado["exito"]:
                print(resultado["mensaje"])
                return {"exito": False, "mensaje": resultado["mensaje"]}
            print("Compra realizada con puntos.")
        
        #Pago con dinero
        elif self.totalVenta <= self.monto_recibido and self.posible:
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
                            producto["cantidad"],
                        ),
                    )
                for producto in self.productos:
                    cursor.execute(
                        "UPDATE inventario SET cantidad = cantidad - (%s) WHERE nombre_producto = (%s)",
                        (producto["cantidad"], producto["nombre_producto"]),
                    )
                connection.commit()
            connection.close()
        else:
            print("Monto recibido insuficiente.")
            return {"exito": False, "mensaje": "Monto insuficiente para completar la compra"}
        
        #ACTUALIZACION DEL RANGO DEL USUARIO - FIDELIZACION
        try:
            resultado_rango = rangos_service.actualizarRangoPorHistorialCompras(self.id_cliente)
            print(resultado_rango["mensaje"])
        except Exception as e:
            print("Error al actualizar el rango del cliente:", e)

        #OBTENCION Y ACTUALIZACION DE LOS PUNTOS DE UNA COMPRA - FIDELIZACION
        try:
            id_rango = rangos_service.obtener_rango_cliente(self.id_cliente)
            porcentaje_compra_puntos = rangos_service.obtener_porcentaje_compra(id_rango)
            puntos_obtenidos = puntos_service.calcular_puntos_compra(
                id_cliente=self.id_cliente,
                idrango=id_rango,
                precio_compra_total=self.totalVenta,
                porcentaje_compra_puntos=porcentaje_compra_puntos
            )
            puntos_service.añadir_puntos_compra(self.id_cliente, puntos_obtenidos)
            print("Puntos añadidos con éxito:", puntos_obtenidos)
        except Exception as e:
            print("Error al procesar los puntos de la compra:", e)
        
        print("Venta hecha correctamente")
        return {"exito": True, "mensaje": "Venta completada"}


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

    def devolverProducto(self, id_cliente, id_venta, precio_unitario):

        #OBTENCION Y ACTUALIZACION DE LOS PUNTOS DE UNA DEVOLUCION - FIDELIZACION
        puntos_service = PuntosService()
        rangos_service = RangosService()
        try:
            #Calculamos los puntos de una devolucion basados en el rango del cliente y el precio del producto
            puntos_devolucion = puntos_service.calcular_puntos_devolucion(
                id_cliente=id_cliente,
                idrango=rangos_service.obtener_rango_cliente(id_cliente),
                precio_producto=self.precio_unitario,
                porcentaje_devolucion_puntos=rangos_service.obtener_porcentaje_devolucion(rangos_service.obtener_rango_cliente(id_cliente))
            )
            puntos_service.añadir_puntos_devolucion(id_cliente, puntos_devolucion)
        except Exception as e:
            print("Error al procesar los puntos de la devolucion:", e)
