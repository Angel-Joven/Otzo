# Modelos para el Modulo de Fidelizacion y Marketing
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from abc import ABC, abstractmethod

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para los puntos
class PuntosModelo(ABC):
    @abstractmethod
    def calcular_puntos_compra(self, precio_compra_total, porcentaje_compra_puntos):
        """Calculamos los puntos basados en el total de la compra"""
        pass

    @abstractmethod
    def calcular_puntos_devolucion(self, precio_producto, porcentaje_devolucion_puntos):
        """Calculamos los puntos basados en una devolucion"""
        pass

    @abstractmethod
    def añadir_puntos_compra(self, id_cliente, puntos_compra):
        """Añadimos los puntos obtenidos de una compra a la tabla de puntos"""
        pass

    @abstractmethod
    def añadir_puntos_devolucion(self, id_cliente, puntos_devolucion):
        """Añadimos los puntos obtenidos de una devolucion a la tabla de puntos"""
        pass

    @abstractmethod
    def descontar_puntos(self, id_cliente, precio_compra_total):
        """Descontamos los puntos si la compra se realiza con el metodo de pago: puntos"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para los rangos
class RangosModelo(ABC):
    @abstractmethod
    def asignarRangoInicialAuto(self):
        """Asignamos el rango inicial a todos los usuarios sin rango y despues verificamos que cuentas estan activas y cuales no"""
        pass

    @abstractmethod
    def actualizarRangoPorHistorialCompras(self, id_cliente):
        """Actualizamos el rango de un cliente en base al historial de compras"""
        pass

    @abstractmethod
    def obtener_rango_cliente_y_porcentajeCompras(self, id_cliente):
        """Obtenemos el rango y el porcentaje de puntos de una compra para un cliente especifico"""
        pass

    @abstractmethod
    def obtener_rango_cliente_y_porcentajeDevolucion(self, id_cliente):
        """Obtenemos el rango y el porcentaje de puntos de una devolucion para un cliente especifico"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para la funcionalidad de calculo y agregar los puntos de una compra y actualizacion de rango a la cuenta del cliente
class PuntosCompraActualizarRangoModelo(ABC):
    @abstractmethod
    def obtener_y_asignar_nuevo_Rango(self, id_cliente):
        """Actualizamos el rango de un cliente en funcion de su historial de compras"""
        pass

    @abstractmethod
    def calcular_y_agregar_puntos_compra(self, id_cliente, precio_compra_total):
        """Calculamos y agregamos los puntos obtenidos de una compra a la cuenta del cliente"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para la funcionalidad de calculo y agregar los puntos de una devolucion y actualizacion de rango a la cuenta del cliente
class PuntosDevolucionActualizarRangoModelo(ABC):
    @abstractmethod
    def obtener_y_asignar_nuevo_Rango(self, id_cliente):
        """Actualizamos el rango de un cliente en funcion de su historial de compras"""
        pass

    @abstractmethod
    def calcular_y_agregar_puntos_devolucion(self, id_cliente, precio_producto):
        """Calculamos y agregamos los puntos obtenidos de una devolucion a la cuenta del cliente"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para la funcionalidad de pagar con puntos y actualizacion de rango a la cuenta del cliente
class PagarPuntosActualizarRangoModelo(ABC):
    @abstractmethod
    def obtener_y_asignar_nuevo_Rango(self, id_cliente):
        """Actualizamos el rango de un cliente en funcion de su historial de compras"""
        pass

    @abstractmethod
    def pagar_con_puntos_compra(self, id_cliente, precio_compra_total):
        """Realizamos una compra descontando puntos de la cuenta del cliente"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para la funcionalidad de obtencion del idrango y nombre_rango - ATENCION
class ObtenerRangoModelo(ABC):
    @abstractmethod
    def obtener_rango_cliente_atencion(self, id_cliente):
        """Obtenemos el idrango y el nombre_rango de un cliente especifico"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para la funcionalidad de obtencion de toda la informacion de la tabla puntos
class ObtenerInfoClientesPuntosModelo(ABC):
    @abstractmethod
    def obtener_info_clientes_puntos(self, id_cliente):
        """Obtenemos toda la informacion de un cliente especifico"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para la funcionalidad de obtencion del idrango y nombre_rango - REPORTES
class ObtenerRangoClientesModelo(ABC):
    @abstractmethod
    def obtener_rango_cliente_reportes(self, id_cliente):
        """Obtenemos el idrango y el nombre_rango de todos los clientes"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------