from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class InventarioDTO:
    _nombre_producto: str
    _imagen_producto: str
    _categoria_producto: str
    _descripcion_producto: str
    _precio_unitario: float
    _cantidad_producto: int = 0
    _descontinuado: bool = False
    _cantidad_maxima_producto: int = 50
    _id_inventario: int = None

    @property
    def nombre_producto(self) -> str:
        return self._nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
        if not isinstance(nombre_producto, str):
            raise TypeError(
                "nombre_producto debe ser una cadena de texto. Error en DTO."
            )
        self._nombre_producto = nombre_producto

    @property
    def imagen_producto(self) -> str:
        return self._imagen_producto

    @imagen_producto.setter
    def imagen_producto(self, imagen_producto: str):
        if not isinstance(imagen_producto, str):
            raise TypeError(
                "imagen_producto debe ser una cadena de texto. Error en DTO."
            )
        self._imagen_producto = imagen_producto

    @property
    def categoria_producto(self) -> str:
        return self._categoria_producto

    @categoria_producto.setter
    def categoria_producto(self, categoria_producto: str):
        if not isinstance(categoria_producto, str):
            raise TypeError(
                "categoria_producto debe ser una cadena de texto. Error en DTO."
            )
        self._categoria_producto = categoria_producto

    @property
    def cantidad_producto(self) -> int:
        return self._cantidad_producto

    @cantidad_producto.setter
    def cantidad_producto(self, cantidad_producto: int):
        if not isinstance(cantidad_producto, int):
            raise TypeError("cantidad_producto debe ser un entero. Error en DTO.")
        self._cantidad_producto = cantidad_producto

    @property
    def descripcion_producto(self) -> str:
        return self._descripcion_producto

    @descripcion_producto.setter
    def descripcion_producto(self, descripcion_producto: str):
        if not isinstance(descripcion_producto, str):
            raise TypeError(
                "descripcion_producto debe ser una cadena de texto. Error en DTO."
            )
        self._descripcion_producto = descripcion_producto

    @property
    def precio_unitario(self) -> float:
        return self._precio_unitario

    @precio_unitario.setter
    def precio_unitario(self, precio_unitario: float):
        if not isinstance(precio_unitario, float):
            raise TypeError("precio_unitario debe ser un float. Error en DTO.")
        self.precio_unitario = precio_unitario

    @property
    def id_inventario(self) -> int:
        return self._id_inventario

    @id_inventario.setter
    def id_inventario(self, id_inventario: int):
        if not isinstance(id_inventario, int):
            raise TypeError("id_inventario debe ser un entero. Error en DTO.")
        self._id_inventario = id_inventario

    @property
    def descontinuado(self) -> bool:
        return self._descontinuado

    @descontinuado.setter
    def descontinuado(self, descontinuado: bool):
        if not isinstance(descontinuado, bool):
            raise TypeError("descontinuado debe ser un booleano. Error en DTO.")
        self._descontinuado = descontinuado

    @property
    def cantidad_maxima_producto(self) -> int:
        return self._cantidad_maxima_producto

    @cantidad_maxima_producto.setter
    def cantidad_maxima_producto(self, cantidad_maxima_producto: int):
        if not isinstance(cantidad_maxima_producto, int):
            raise TypeError(
                "cantidad_maxima_producto debe ser un entero. Error en DTO."
            )
        self._cantidad_maxima_producto = cantidad_maxima_producto


@dataclass
class DetalleInventarioDTO:
    _id_inventario: int
    _codigo_producto: str
    _fecha_producto: datetime
    _caducidad_producto: datetime
    _costo_unitario: float
    _vendido: bool = False
    _devuelto: bool = False

    @property
    def id_inventario(self) -> int:
        return self._id_inventario

    @id_inventario.setter
    def id_inventario(self, id_inventario: int):
        if not isinstance(id_inventario, int):
            raise TypeError("id_inventario debe ser un entero. Error en DTO.")
        self.id_inventario = id_inventario

    @property
    def codigo_producto(self) -> str:
        return self._codigo_producto

    @codigo_producto.setter
    def codigo_producto(self, codigo_producto: str):
        if not isinstance(codigo_producto, str):
            raise TypeError("codigo_producto debe ser una cadena. Error en DTO.")
        self.codigo_producto = codigo_producto

    @property
    def fecha_producto(self) -> datetime:
        return self._fecha_producto

    @fecha_producto.setter
    def fecha_producto(self, fecha_producto: datetime):
        if not isinstance(fecha_producto, datetime):
            raise TypeError("fecha_producto debe ser un datetime. Error en DTO.")
        self.fecha_producto = fecha_producto

    @property
    def caducidad_producto(self) -> datetime:
        return self._caducidad_producto

    @caducidad_producto.setter
    def caducidad_producto(self, caducidad_producto: datetime):
        if not isinstance(caducidad_producto, datetime):
            raise TypeError("caducidad_producto debe ser un datetime. Error en DTO.")
        self.caducidad_producto = caducidad_producto

    @property
    def costo_unitario(self) -> float:
        return self._costo_unitario

    @costo_unitario.setter
    def costo_unitario(self, costo_unitario: float):
        if not isinstance(costo_unitario, float):
            raise TypeError("costo_unitario debe ser un float. Error en DTO.")
        self.costo_unitario = costo_unitario

    @property
    def vendido(self) -> bool:
        return self._vendido

    @vendido.setter
    def vendido(self, vendido: bool):
        if not isinstance(vendido, bool):
            raise TypeError("vendido debe ser un boolean. Error en DTO.")
        self._vendido = vendido

    @property
    def devuelto(self) -> bool:
        return self._devuelto

    @devuelto.setter
    def devuelto(self, devuelto: bool):
        if not isinstance(devuelto, bool):
            raise TypeError("devuelto debe ser un boolean. Error en DTO.")
        self._devuelto = devuelto
