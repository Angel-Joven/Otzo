from dataclasses import dataclass
from datetime import datetime

@dataclass
class QuejasDTO:
    _idQueja: int
    _idCliente: int
    _rangoUsuario: int
    _fechaHora: datetime
    _descripcion: str
    _categoria: str
    _estado: str
    _prioridad: int
    _comentarioSeguimiento: str
    
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
    def rangoUsuario(self) -> int:
        return self._rangoUsuario
    
    @rangoUsuario.setter
    def rangoUsuario(self, value: int):
        self._rangoUsuario = value
    
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
class Sugerencias:
    _idSugerencia: int
    _idCliente: int
    _fechaHora: datetime
    _descripcion: str
    _categoria: str
    _estado: str
    _comentarioSeguimiento: str
    
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

#Crear una queja
queja = QuejasDTO(
    _idQueja = 1,
    _idCliente = 1,
    _rangoUsuario = 1,
    _fechaHora = datetime.now(),
    _descripcion = "Mala atención del personal",
    _categoria = "Atención al cliente",
    _estado = "En espera",
    _prioridad = 1,
    _comentarioSeguimiento = ""
)

#Crear una sugerencia
sugerencia = Sugerencias(
    _idSugerencia = 1,
    _idCliente = 1,
    _fechaHora = datetime.now(),
    _descripcion = "Deberían tener más variedad de productos",
    _categoria = "Productos",
    _estado = "En espera",
    _comentarioSeguimiento = ""
)

#Imprimir los datos de la queja
print("ID de la queja:", queja.idQueja)
print("ID del cliente:", queja.idCliente)
print("Rango del usuario:", queja.rangoUsuario)
print("Fecha y hora:", queja.fechaHora)
print("Descripción:", queja.descripcion)
print("Categoría:", queja.categoria)
print("Estado:", queja.estado)
print("Prioridad:", queja.prioridad)
print("Comentario de seguimiento:", queja.comentarioSeguimiento)

#Imprimir los datos de la sugerencia
print("ID de la sugerencia:", sugerencia.idSugerencia)
print("ID del cliente:", sugerencia.idCliente)
print("Fecha y hora:", sugerencia.fechaHora)
print("Descripción:", sugerencia.descripcion)
print("Categoría:", sugerencia.categoria)
print("Estado:", sugerencia.estado)
print("Comentario de seguimiento:", sugerencia.comentarioSeguimiento)