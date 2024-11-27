import json
from dataclasses import dataclass

class ReporteDTO:
    """DTO para los reportes diarios de puntos."""
    def __init__(self, fecha_generacion=None, clientes=None):
        self._fecha_generacion = fecha_generacion
        self._clientes = clientes or []

    # Getters
    @property
    def fecha_generacion(self):
        return self._fecha_generacion

    @property
    def clientes(self):
        return self._clientes

    # Setters
    @fecha_generacion.setter
    def fecha_generacion(self, value):
        self._fecha_generacion = value

    @clientes.setter
    def clientes(self, value):
        self._clientes = value

    def to_dict(self):
        return {
            "fecha_generacion": self._fecha_generacion,
            "clientes": self._clientes
        }

    def to_json(self):
        return json.dumps(self.to_dict())
    
    import json

class VentaDTO:
    """DTO para los reportes diarios de ventas."""
    def __init__(self, id_venta=None, total_venta=0, fecha_venta=None, cliente=None, empleado=None, detalles=None):
        self._id_venta = id_venta
        self._total_venta = total_venta
        self._fecha_venta = fecha_venta
        self._cliente = cliente
        self._empleado = empleado
        self._detalles = detalles or []

    @property
    def id_venta(self):
        return self._id_venta

    @id_venta.setter
    def id_venta(self, value):
        self._id_venta = value

    @property
    def total_venta(self):
        return self._total_venta

    @total_venta.setter
    def total_venta(self, value):
        self._total_venta = value

    @property
    def fecha_venta(self):
        return self._fecha_venta

    @fecha_venta.setter
    def fecha_venta(self, value):
        self._fecha_venta = value

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, value):
        self._cliente = value

    @property
    def empleado(self):
        return self._empleado

    @empleado.setter
    def empleado(self, value):
        self._empleado = value

    @property
    def detalles(self):
        return self._detalles

    @detalles.setter
    def detalles(self, value):
        self._detalles = value

    def to_dict(self):
        return {
            "id_venta": self._id_venta,
            "total_venta": self._total_venta,
            "fecha_venta": self._fecha_venta,
            "cliente": self._cliente,
            "empleado": self._empleado,
            "detalles": self._detalles,
        }

    def to_json(self):
        return json.dumps(self.to_dict())

class QuejasReporteDTO:
    """DTO para el reporte de quejas."""
    def __init__(self, categoria=None, cantidad=0, ids_quejas=None):
        self._categoria = categoria
        self._cantidad = cantidad
        self._ids_quejas = ids_quejas or []

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

    @property
    def ids_quejas(self):
        return self._ids_quejas

    @ids_quejas.setter
    def ids_quejas(self, value):
        self._ids_quejas = value

    def to_dict(self):
        return {
            "categoria": self._categoria,
            "cantidad": self._cantidad,
            "ids_quejas": self._ids_quejas,
        }

@dataclass
class InventarioReporteDTO:
    id_inventario: int
    nombre_producto: str
    cantidad_producto: int
    categoria: str  # Campo añadido para mostrar la categoría del producto.

    def to_dict(self):
        return {
            "id_inventario": self.id_inventario,
            "nombre_producto": self.nombre_producto,
            "cantidad_producto": self.cantidad_producto,
            "categoria": self.categoria,  # Ajuste para incluir nuevos campos.
        }