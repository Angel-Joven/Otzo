from abc import ABC, abstractmethod

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para los puntos
class PuntosModelo(ABC):
    @abstractmethod
    def calcular_puntos_compra(self, id_cliente, idrango, precio_compra_total, porcentaje_compra_puntos):
        """Calculamos los puntos basados en el total de la compra"""
        pass

    @abstractmethod
    def calcular_puntos_devolucion(self, id_cliente, idrango, precio_producto, porcentaje_devolucion_puntos):
        """Calculamos los puntos basados en una devolucion"""
        pass

    @abstractmethod
    def añadir_puntos_compra(self, puntos_compra):
        """Añadimos los puntos obtenidos de una compra a la tabla de puntos"""
        pass

    @abstractmethod
    def añadir_puntos_devolucion(self, puntos_devolucion):
        """Añadimos los puntos obtenidos de una devolucion a la tabla de puntos"""
        pass

    @abstractmethod
    def descontar_puntos(self, precio_compra_total, puntos_totales):
        """Descontamos los puntos si la compra se realiza con el metodo de pago: puntos"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para los rangos
class RangosModelo(ABC):
    
    @abstractmethod
    def obtener_porcentaje_compra(self, idrango):
        """Obtenemos el porcentaje de puntos de compra para un rango dado"""
        pass

    @abstractmethod
    def obtener_porcentaje_devolucion(self, idrango):
        """Obtenemos el porcentaje de puntos de devolucion para un rango dado"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------