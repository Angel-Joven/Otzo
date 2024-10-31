# Modulo de Fidelizacion y Marketing

import json

class Serializable:
    def to_dict(self):
        """Convierte el objeto en un diccionario."""
        return self.__dict__


    def to_json(self):
        """Convierte el objeto a formato JSON.""" 
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data):
        """Crea un objeto desde un diccionario."""
        return cls(**data)

    @classmethod
    def from_json(cls, json_data):
        """Crea un objeto desde una cadena JSON."""
        return cls.from_dict(json.loads(json_data))

class PuntosDTO(Serializable):
    def __init__(self, idclientes_puntos=None, idrango=None, total_puntos=0):
        self._idclientes_puntos = idclientes_puntos
        self._idrango = idrango
        self._total_puntos = total_puntos

    # Getters
    @property
    def idclientes_puntos(self):
        return self._idclientes_puntos

    @property
    def idrango(self):
        return self._idrango

    @property
    def total_puntos(self):
        return self._total_puntos

    # Setters
    @idclientes_puntos.setter
    def idclientes_puntos(self, value):
        self._idclientes_puntos = value

    @idrango.setter
    def idrango(self, value):
        self._idrango = value

    @total_puntos.setter
    def total_puntos(self, value):
        self._total_puntos = value

class RangosDTO(Serializable):
    def __init__(self, idrango=None, nombre_rango="", porcentaje_puntos=0, porcentaje_devolucionPuntos=0):
        self._idrango = idrango
        self._nombre_rango = nombre_rango
        self._porcentaje_puntos = porcentaje_puntos
        self._porcentaje_devolucionPuntos = porcentaje_devolucionPuntos

    # Getters
    @property
    def idrango(self):
        return self._idrango

    @property
    def nombre_rango(self):
        return self._nombre_rango

    @property
    def porcentaje_puntos(self):
        return self._porcentaje_puntos

    @property
    def porcentaje_devolucionPuntos(self):
        return self._porcentaje_devolucionPuntos

    # Setters
    @idrango.setter
    def idrango(self, value):
        self._idrango = value

    @nombre_rango.setter
    def nombre_rango(self, value):
        self._nombre_rango = value

    @porcentaje_puntos.setter
    def porcentaje_puntos(self, value):
        self._porcentaje_puntos = value

    @porcentaje_devolucionPuntos.setter
    def porcentaje_devolucionPuntos(self, value):
        self._porcentaje_devolucionPuntos = value
