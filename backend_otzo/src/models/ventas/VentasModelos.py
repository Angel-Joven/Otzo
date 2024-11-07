from abc import ABC, abstractmethod


class VentaModelo(ABC):
    @abstractmethod
    def agregarVenta(self):
        pass

    @abstractmethod
    def calcularTotalVenta(self):
        pass


class DetalleVentaModelo(ABC):
    @abstractmethod
    def devolverProducto(self):
        pass
