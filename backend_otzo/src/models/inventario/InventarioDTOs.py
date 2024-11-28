from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class InventarioDTO:
    _nombre_producto: str
    _imagen_producto: str
    _categoria_producto: str
    _descripcion_producto: str
    _precio_unitario: Decimal
    _cantidad_producto: int = 0
    _descontinuado: bool = False
    _cantidad_maxima_producto: int = 50
    _id_inventario: int = None

    @property
    def nombre_producto(self) -> str:
        return self._nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
        self._nombre_producto = nombre_producto

    @property
    def imagen_producto(self) -> str:
        return self._imagen_producto

    @imagen_producto.setter
    def imagen_producto(self, imagen_producto: str):
        self._imagen_producto = imagen_producto

    @property
    def categoria_producto(self) -> str:
        return self._categoria_producto

    @categoria_producto.setter
    def categoria_producto(self, categoria_producto: str):
        self._categoria_producto = categoria_producto

    @property
    def cantidad_producto(self) -> int:
        return self._cantidad_producto

    @cantidad_producto.setter
    def cantidad_producto(self, cantidad_producto: int):
        self._cantidad_producto = cantidad_producto

    @property
    def descripcion_producto(self) -> str:
        return self._descripcion_producto

    @descripcion_producto.setter
    def descripcion_producto(self, descripcion_producto: str):
        self._descripcion_producto = descripcion_producto

    @property
    def precio_unitario(self) -> Decimal:
        return self._precio_unitario

    @precio_unitario.setter
    def precio_unitario(self, precio_unitario: Decimal):
        self.precio_unitario = precio_unitario

    @property
    def id_inventario(self) -> int:
        return self._id_inventario

    @id_inventario.setter
    def id_inventario(self, id_inventario: int):
        self._id_inventario = id_inventario

    @property
    def descontinuado(self) -> bool:
        return self._descontinuado

    @descontinuado.setter
    def descontinuado(self, descontinuado: bool):
        self._descontinuado = descontinuado

    @property
    def cantidad_maxima_producto(self) -> int:
        return self._cantidad_maxima_producto

    @cantidad_maxima_producto.setter
    def cantidad_maxima_producto(self, cantidad_maxima_producto: int):
        self._cantidad_maxima_producto = cantidad_maxima_producto


@dataclass
class DetalleInventarioDTO:
    _id_inventario: int
    _codigo_producto: str
    _fecha_producto: datetime
    _caducidad_producto: datetime
    _costo_unitario: Decimal
    _vendido: bool = False
    _devuelto: bool = False

    @property
    def id_inventario(self) -> int:
        return self._id_inventario

    @id_inventario.setter
    def id_inventario(self, id_inventario: int):
        self.id_inventario = id_inventario

    @property
    def codigo_producto(self) -> str:
        return self._codigo_producto

    @codigo_producto.setter
    def codigo_producto(self, codigo_producto: str):
        self.codigo_producto = codigo_producto

    @property
    def fecha_producto(self) -> datetime:
        return self._fecha_producto

    @fecha_producto.setter
    def fecha_producto(self, fecha_producto: datetime):
        self.fecha_producto = fecha_producto

    @property
    def caducidad_producto(self) -> datetime:
        return self._caducidad_producto

    @caducidad_producto.setter
    def caducidad_producto(self, caducidad_producto: datetime):
        self.caducidad_producto = caducidad_producto

    @property
    def costo_unitario(self) -> Decimal:
        return self._costo_unitario

    @costo_unitario.setter
    def costo_unitario(self, costo_unitario: Decimal):
        self.costo_unitario = costo_unitario

    @property
    def vendido(self) -> bool:
        return self._vendido

    @vendido.setter
    def vendido(self, vendido: bool):
        self._vendido = vendido

    @property
    def devuelto(self) -> bool:
        return self._devuelto

    @devuelto.setter
    def devuelto(self, devuelto: bool):
        self._devuelto = devuelto
