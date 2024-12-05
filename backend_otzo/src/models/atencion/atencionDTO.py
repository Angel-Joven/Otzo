from dataclasses import dataclass
from datetime import datetime


@dataclass
class QuejasDTO:
    _idCliente: int
    _idEmpleado: int
    _fechaHora: datetime
    _descripcion: str
    _categoria: str
    _estado: str
    _prioridad: int
    _comentarioSeguimiento: str = ""
    _idQueja: int = None

    @property
    def idQueja(self) -> int:
        return self._idQueja

    @idQueja.setter
    def idQueja(self, value: int):
        self._idQueja = value

    @property
    def idCliente(self) -> int:
        return self._idCliente

    @idCliente.setter
    def idCliente(self, value: int):
        self._idCliente = value

    @property
    def idEmpleado(self) -> int:
        return self._idEmpleado

    @idEmpleado.setter
    def idEmpleado(self, value: int):
        self._idEmpleado = value

    @property
    def fechaHora(self) -> datetime:
        return self._fechaHora

    @fechaHora.setter
    def fechaHora(self, value: datetime):
        self._fechaHora = value

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: str):
        self._descripcion = value

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, value: str):
        self._categoria = value

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, value: str):
        self._estado = value

    @property
    def prioridad(self) -> int:
        return self._prioridad

    @prioridad.setter
    def prioridad(self, value: int):
        self._prioridad = value

    @property
    def comentarioSeguimiento(self) -> str:
        return self._comentarioSeguimiento

    @comentarioSeguimiento.setter
    def comentarioSeguimiento(self, value: str):
        self._comentarioSeguimiento = value


@dataclass
class SugerenciasDTO:
    _idCliente: int
    _idEmpleado: int
    _fechaHora: datetime
    _descripcion: str
    _categoria: str
    _estado: str
    _comentarioSeguimiento: str
    _idSugerencia: int = None

    @property
    def idSugerencia(self) -> int:
        return self._idSugerencia

    @idSugerencia.setter
    def idSugerencia(self, value: int):
        self._idSugerencia = value

    @property
    def idCliente(self) -> int:
        return self._idCliente

    @idCliente.setter
    def idCliente(self, value: int):
        self._idCliente = value

    @property
    def idEmpleado(self) -> int:
        return self._idEmpleado

    @idEmpleado.setter
    def idEmpleado(self, value: int):
        self._idEmpleado = value

    @property
    def fechaHora(self) -> datetime:
        return self._fechaHora

    @fechaHora.setter
    def fechaHora(self, value: datetime):
        self._fechaHora = value

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: str):
        self._descripcion = value

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, value: str):
        self._categoria = value

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, value: str):
        self._estado = value

    @property
    def comentarioSeguimiento(self) -> str:
        return self._comentarioSeguimiento

    @comentarioSeguimiento.setter
    def comentarioSeguimiento(self, value: str):
        self._comentarioSeguimiento = value
