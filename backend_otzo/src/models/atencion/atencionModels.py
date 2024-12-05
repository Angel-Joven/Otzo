from abc import ABC, abstractmethod


class QuejasModelo(ABC):
    @abstractmethod
    def crearQueja(self):
        pass

    @abstractmethod
    def actualizarQueja(self):
        pass

    @abstractmethod
    def listarQuejasCliente(self):
        pass

    @abstractmethod
    def listarQuejasPendientes(self):
        pass


class SugerenciasModelo(ABC):
    @abstractmethod
    def crearSugerencia(self):
        pass

    @abstractmethod
    def actualizarSugerencia(self):
        pass
    
    @abstractmethod
    def listarSugerenciasPendientes(self):
        pass
