from abc import ABC, abstractmethod


class QuejasModelo(ABC):
    @abstractmethod
    def crearQueja(self):
        pass

    @abstractmethod
    def actualizarEstado(self):
        pass


class SugerenciasModelo(ABC):
    @abstractmethod
    def crearSugerencia(self):
        pass
    
    @abstractmethod
    def actualizarEstado(self):
        pass