from abc import ABC, abstractmethod


class Venta(ABC):
    @abstractmethod
    def agregarVenta(self):
        pass

    @abstractmethod
    def calcularTotal(self):
        pass


class VentaProductos(Venta):
    def __init__(self, productos):
        self.productos = productos

    def agregarVenta(self):
        print("Agregando venta de productos")

    def calcularTotal(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total


venta_producto = VentaProductos()
venta_producto.agregarVenta()  # 3 productos a $10 cada uno
venta_producto.agregarVenta()  # 5 productos a $15 cada uno
print("Total de venta de productos:", venta_producto.calcularTotal())
