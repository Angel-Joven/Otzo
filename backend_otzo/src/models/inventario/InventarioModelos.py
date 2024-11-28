from abc import ABC, abstractmethod


class InventarioModelo(ABC):
    @abstractmethod
    def agregarTipoProducto(self):
        """Función para agregar un nuevo tipo de producto al inventario"""
        pass

    @abstractmethod
    def actualizarTipoProducto(self):
        """Función para actualizar un tipo de producto en el inventario"""
        pass

    @abstractmethod
    def eliminarTipoProducto(self):
        """Funcion para eliminar un tipo producto en el inventario"""
        pass

    @abstractmethod
    def listarTipoProductos(self):
        """Función para listar los tipos de productos en el inventario"""
        pass

    @abstractmethod
    def listarTipoProductosDescontinuados(self):
        """Función para listar los tipos de productos descontinuados en el inventario"""
        pass

    @abstractmethod
    def listarCategoriasTiposProductos(self):
        """Función para listar las categorías de tipos de productos en el inventario"""
        pass

    @abstractmethod
    def obtenerTipoProducto(self):
        """Función para obtener un tipo producto en el inventario"""
        pass


class DetalleInventarioModelo(ABC):
    @abstractmethod
    def agregarProducto(self):
        """Función para agregar un nuevo producto al detalle de inventario"""
        pass

    @abstractmethod
    def actualizarProducto(self):
        """ "Funcion para actualizar un producto del detalle de inventario"""
        pass

    @abstractmethod
    def devolverProducto(self):
        """Funcion para devolver un producto al detalle de inventario"""
        pass

    @abstractmethod
    def generarCodigoProducto(self):
        """Función para generar un código de producto único"""
        pass

    @abstractmethod
    def generarPrecioProducto(self):
        """Función para generar el precio de un producto"""
        pass
