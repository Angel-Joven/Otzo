# Modulo de Fidelizacion y Marketing

import json

# ---------------------------------------------------------------------------------------------------------------------------

class Serializable:
    def to_dict(self):
        """Convertimos el objeto en un diccionario"""
        return self.__dict__


    def to_json(self):
        """Convertimos el objeto a formato JSON""" 
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data):
        """Creamos un objeto desde un diccionario, asimismo, eliminamos los guiones bajos de las claves"""
        cleaned_data = {k.lstrip('_'): v for k, v in data.items()}
        return cls(**cleaned_data)

    @classmethod
    def from_json(cls, json_data):
        """Creamos un objeto desde una cadena JSON"""
        return cls.from_dict(json.loads(json_data))

# ---------------------------------------------------------------------------------------------------------------------------

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
        if value is not None and value < 0:
            raise ValueError("El ID del cliente no puede ser negativo")
        self._idclientes_puntos = value

    @idrango.setter
    def idrango(self, value):
        if value is not None and value < 0:
            raise ValueError("El ID del rango no puede ser negativo")
        self._idrango = value

    @total_puntos.setter
    def total_puntos(self, value):
        if value < 0:
            raise ValueError("Los puntos no pueden ser negativos")
        self._total_puntos = value

# ---------------------------------------------------------------------------------------------------------------------------

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
        if value is not None and value < 0:
            raise ValueError("El ID del rango no puede ser negativo")
        self._idrango = value

    @nombre_rango.setter
    def nombre_rango(self, value):
        if not value:
            raise ValueError("El nombre del rango no puede estar vacio")
        self._nombre_rango = value

    @porcentaje_puntos.setter
    def porcentaje_puntos(self, value):
        if not (0 <= value <= 100):
            raise ValueError("El porcentaje de puntos de una compra debe estar entre 0 y 100")
        self._porcentaje_puntos = value

    @porcentaje_devolucionPuntos.setter
    def porcentaje_devolucionPuntos(self, value):
        if not (0 <= value <= 100):
            raise ValueError("El porcentaje de devolucion de puntos debe estar entre 0 y 100")
        self._porcentaje_devolucionPuntos = value

# ---------------------------------------------------------------------------------------------------------------------------

print("---------------------------------------------------------------------------------------------------------------------------")
print("PUNTOS DTO")

#PuntosDTO - EJEMPLO TEST
puntos_dto = PuntosDTO(idclientes_puntos=1, idrango=5, total_puntos=100)

#Convertimos a JSON - EJEMPLO TEST
json_data = puntos_dto.to_json()
print("JSON:", json_data)
#JSON: {"_idclientes_puntos": 1, "_idrango": 5, "_total_puntos": 100}

#Reconstruimos desde un JSON - EJEMPLO TEST
nuevo_puntos_dto = PuntosDTO.from_json(json_data)
print("Nuevo DTO:", nuevo_puntos_dto.to_dict())
#Nuevo DTO: {'_idclientes_puntos': 1, '_idrango': 5, '_total_puntos': 100}

print("ID del cliente:", puntos_dto.idclientes_puntos)
print("Rango del cliente:", puntos_dto.idrango)
print("Total de puntos del cliente:", puntos_dto.total_puntos)

print("---------------------------------------------------------------------------------------------------------------------------")

# ---------------------------------------------------------------------------------------------------------------------------

print("RANGOS DTO")

#PuntosDTO - EJEMPLO TEST
rangos_dto = RangosDTO(idrango=1, nombre_rango='INVITADO', porcentaje_puntos=0, porcentaje_devolucionPuntos=0)

#Convertimos a JSON - EJEMPLO TEST
json_data = rangos_dto.to_json()
print("JSON:", json_data)
#JSON: {"_idrango": 1, "_nombre_rango": "INVITADO", "_porcentaje_puntos": 0, "_porcentaje_devolucionPuntos": 0}

#Reconstruimos desde un JSON - EJEMPLO TEST
nuevo_rangos_dto = RangosDTO.from_json(json_data)
print("Nuevo DTO:", nuevo_rangos_dto.to_dict())
#Nuevo DTO: {'_idrango': 1, '_nombre_rango': 'INVITADO', '_porcentaje_puntos': 0, '_porcentaje_devolucionPuntos': 0}

print("ID del rango:", rangos_dto.idrango)
print("Nombre del rango:", rangos_dto.nombre_rango)
print("Porcentaje de puntos de compras para ese rango:", rangos_dto.porcentaje_puntos)
print("Porcentaje de puntos de devoluciones para ese rango:", rangos_dto.porcentaje_devolucionPuntos)

print("---------------------------------------------------------------------------------------------------------------------------")

# ---------------------------------------------------------------------------------------------------------------------------