from datetime import datetime

class ReabastecimientoDTO:
    def __init__(self, id_reabastecimiento: int, id_producto: int, cantidad: int, fecha_reabastecimiento: datetime, proveedor: str):
        self._id_reabastecimiento = id_reabastecimiento
        self._id_producto = id_producto
        self._cantidad = cantidad
        self._fecha_reabastecimiento = fecha_reabastecimiento
        self._proveedor = proveedor


    @property
    def id_reabastecimiento(self) -> int:
        return self._id_reabastecimiento

    @id_reabastecimiento.setter
    def id_reabastecimiento(self, value: int):
        if value <= 0:
            raise ValueError("El ID de reabastecimiento debe ser positivo.")
        self._id_reabastecimiento = value

    # id_producto
    @property
    def id_producto(self) -> int:
        return self._id_producto

    @id_producto.setter
    def id_producto(self, value: int):
        if value <= 0:
            raise ValueError("El ID de producto debe ser positivo.")
        self._id_producto = value

    # cantidad
    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value: int):
        if value <= 0:
            raise ValueError("La cantidad debe ser mas que 0.")
        self._cantidad = value

    # fecha_reabastecimiento
    @property
    def fecha_reabastecimiento(self) -> datetime:
        return self._fecha_reabastecimiento

    @fecha_reabastecimiento.setter
    def fecha_reabastecimiento(self, value: datetime):
        if value > datetime.now():
            raise ValueError("La fecha de reabastecimiento es incorrecta.")
        self._fecha_reabastecimiento = value

    # proveedor
    @property
    def proveedor(self) -> str:
        return self._proveedor

    @proveedor.setter
    def proveedor(self, value: str):
        if not value:
            raise ValueError("falta el nombre.")
        self._proveedor = value

    def __str__(self):
        return f"Reabastecimiento(id_reabastecimiento={self.id_reabastecimiento}, id_producto={self.id_producto}, " \
               f"cantidad={self.cantidad}, fecha_reabastecimiento={self.fecha_reabastecimiento}, proveedor={self.proveedor})"
