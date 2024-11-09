from abc import ABC, abstractmethod


class VentaModelo(ABC):
    @abstractmethod
    def agregarVenta(self):
        """Funcion para agregar una venta"""
        pass

    @abstractmethod
    def calcularTotalVenta(self):
        """Funcion para calcular el precio total de una venta"""
        pass

    @abstractmethod
    def calcularCantidadVenta(self):
        """Funcion para poder calcular la cantidad de producto unico en una venta"""
        pass

    @abstractmethod
    def obtenerDatosProductos(self):
        """Funcion para obtener los datos de los productos en una venta"""
        pass


class DetalleVentaModelo(ABC):
    @abstractmethod
    def devolverProducto(self):
        """Funcion para devolver un producto al inventario"""
        pass
