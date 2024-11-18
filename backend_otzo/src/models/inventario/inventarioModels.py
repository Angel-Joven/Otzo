from abc import ABC, abstractmethod


class InventarioModelo(ABC):
    @abstractmethod
    def agregarProducto(self):
        """Función para agregar un producto al inventario"""
        pass

    @abstractmethod
    def bajaProducto(self):
         """Función para dar de baja un producto del inventario"""
        pass

    @abstractmethod
    def ModificarProducto(self):
        """Función para modificar la información de un producto"""
        pass




