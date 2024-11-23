from abc import ABC, abstractmethod

class ReportesModelo(ABC):
    @abstractmethod
    def crear_reporte_puntos(self):
        """Info"""
        pass

    @abstractmethod
    def crear_reporte_ventas(self):
        """Info"""
        pass
