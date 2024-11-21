import json

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
