from dataclasses import dataclass, field
from typing import List
from datetime import datetime


@dataclass
class DetalleVentasDTO:
    _id_detalle_venta: int
    _id_venta: int
    _nombre_producto: str
    _codigo_producto: str
    _precio_unitario: float
    _categoria_producto: str
    _devuelto: bool

    @property
    def id_detalle_venta(self) -> int:
        return self._id_detalle_venta

    @id_detalle_venta.setter
    def id_detalle_venta(self, value: int):
        self._id_detalle_venta = value

    @property
    def id_venta(self) -> int:
        return self._id_venta

    @id_venta.setter
    def id_venta(self, value: int):
        self._id_venta = value

    @property
    def nombre_producto(self) -> str:
        return self._nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, value: str):
        if len(value) < 3:
            raise ValueError("El nombre del producto debe tener al menos 3 caracteres")
        self._nombre_producto = value

    @property
    def codigo_producto(self) -> str:
        return self._codigo_producto

    @codigo_producto.setter
    def codigo_producto(self, value: str):
        if len(value) < 5:
            raise ValueError("El código del producto debe tener al menos 5 caracteres")
        self._codigo_producto = value

    @property
    def precio_unitario(self) -> float:
        return self._precio_unitario

    @precio_unitario.setter
    def precio_unitario(self, value: float):
        if value < 0:
            raise ValueError("El precio unitario no puede ser negativo")
        self._precio_unitario = value

    @property
    def categoria_producto(self) -> str:
        return self._categoria_producto

    @categoria_producto.setter
    def categoria_producto(self, value: str):
        if len(value) < 3:
            raise ValueError(
                "La categoría del producto debe tener al menos 3 caracteres"
            )
        self._categoria_producto = value

    @property
    def devuelto(self) -> bool:
        return self._devuelto

    @devuelto.setter
    def devuelto(self, value: bool):
        self._devuelto = value


@dataclass
class VentaDTO:
    _id_venta: int
    _total_venta: float
    _fecha_venta: datetime
    _metodo_pago: str
    _id_cliente: int
    _id_trabajador: int
    detalles_ventas: List[DetalleVentasDTO] = field(default_factory=list)

    @property
    def id_venta(self) -> int:
        return self._id_venta

    @id_venta.setter
    def id_venta(self, value: int):
        self._id_venta = value

    @property
    def total_venta(self) -> float:
        return self._total_venta

    @total_venta.setter
    def total_venta(self, value: float):
        if value < 0:
            raise ValueError("El total de la venta no puede ser negativo")
        self._total_venta = value

    @property
    def fecha_venta(self) -> datetime:
        return self._fecha_venta

    @fecha_venta.setter
    def fecha_venta(self, value: datetime):
        if value < datetime.now():
            raise ValueError("La fecha de venta no puede ser anterior a la actual")
        self._fecha_venta = value

    @property
    def metodo_pago(self) -> str:
        return self._metodo_pago

    @metodo_pago.setter
    def metodo_pago(self, value: str):
        if value not in ["efectivo", "t_debito", "t_credito"]:
            raise ValueError("Método de pago no válido")
        self._metodo_pago = value

    @property
    def id_cliente(self) -> int:
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, value: int):
        self._id_cliente = value

    @property
    def id_trabajador(self) -> int:
        return self._id_trabajador

    @id_trabajador.setter
    def id_trabajador(self, value: int):
        self._id_trabajador = value

    def agregar_detalle_venta(self, detalle_venta: DetalleVentasDTO):
        self.detalles_ventas.append(detalle_venta)


# Crear un detalle de venta
detalle_venta1 = DetalleVentasDTO(
    _id_detalle_venta=1,
    _id_venta=101,
    _nombre_producto="Laptop",
    _codigo_producto="ABC123",
    _precio_unitario=999.99,
    _categoria_producto="Electrónica",
    _devuelto=False,
)

# Crear una venta y añadir el detalle de venta
venta = VentaDTO(
    _id_venta=101,
    _total_venta=999.99,
    _fecha_venta=datetime.now(),
    _metodo_pago="t_debito",
    _id_cliente=1001,
    _id_trabajador=501,
)

# Añadir el detalle de venta a la venta
venta.agregar_detalle_venta(detalle_venta1)

# Imprimir detalles de la venta y sus detalles de venta
print(f"ID de Venta: {venta.id_venta}")
print(f"Total de Venta: {venta.total_venta}")
print(f"Fecha de Venta: {venta.fecha_venta}")
print(f"Método de Pago: {venta.metodo_pago}")
print(f"ID de Cliente: {venta.id_cliente}")
print(f"ID de Trabajador: {venta.id_trabajador}")

# Imprimir detalles de cada detalle de venta
for detalle in venta.detalles_ventas:
    print(f"\nID de Detalle de Venta: {detalle.id_detalle_venta}")
    print(f"ID de Venta: {detalle.id_venta}")
    print(f"Nombre del Producto: {detalle.nombre_producto}")
    print(f"Código del Producto: {detalle.codigo_producto}")
    print(f"Precio Unitario: {detalle.precio_unitario}")
    print(f"Categoría del Producto: {detalle.categoria_producto}")
    print(f"Devuelto: {detalle.devuelto}")
