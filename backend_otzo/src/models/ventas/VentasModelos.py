from abc import ABC, abstractmethod


class VentaModelo(ABC):
    @abstractmethod
    def agregarVenta(self):
        """Funcion para agregar una venta en efectivo"""
        pass

    @abstractmethod
    def calcularTotalVenta(self):
        """Funcion para calcular el precio total de una venta"""
        pass

    @abstractmethod
    def listarVentasDeUsuario(self):
        """Funcion para listar las ventas de un usuario"""
        pass


class DetalleVentaModelo(ABC):
    @abstractmethod
    def devolverProducto(self):
        """Funcion para devolver un producto al inventario"""
        pass

    @abstractmethod
    def llenarDatos(self):
        """Funcion para llenar los datos de los detalles de venta"""
        pass

    @abstractmethod
    def listarDetallesDeVenta(self):
        """Funcion para listar los detalles de una venta"""
        pass

    @abstractmethod
    def listarVariosDetallesDeVentas(self):
        """Funcion para listar varios detalles de varias ventas"""
        pass
