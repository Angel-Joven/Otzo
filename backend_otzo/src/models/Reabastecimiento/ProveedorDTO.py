class ProveedorDTO:
    def __init__(self, nombre: str, tipo_producto: str, contacto: str, tiempo_entrega: int, direccion: str, email: str):
        self._nombre = nombre
        self._tipo_producto = tipo_producto
        self._contacto = contacto
        self._tiempo_entrega = tiempo_entrega
        self._direccion = direccion
        self._email = email


    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        if not value:
            raise ValueError("El nombre no puede sin nada.")
        self._nombre = value

    # tipo_producto
    @property
    def tipo_producto(self) -> str:
        return self._tipo_producto

    @tipo_producto.setter
    def tipo_producto(self, value: str):
        if not value:
            raise ValueError("El tipo de producto no puede estar en 0.")
        self._tipo_producto = value

    # contacto
    @property
    def contacto(self) -> str:
        return self._contacto

    @contacto.setter
    def contacto(self, value: str):
        if not value:
            raise ValueError("El contacto debe tener 10 caracteres.")
        self._contacto = value

    # tiempo_entrega
    @property
    def tiempo_entrega(self) -> int:
        return self._tiempo_entrega

    @tiempo_entrega.setter
    def tiempo_entrega(self, value: int):
        if value < 0:
            raise ValueError("El tiempo de entrega no puede ser negativo.")
        self._tiempo_entrega = value

    # direccion
    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, value: str):
        if not value:
            raise ValueError("La dirección no puede estar vacía.")
        self._direccion = value

    # email
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if "@" not in value:
            raise ValueError("El correo debe ser válido.")
        self._email = value

    def __str__(self):
        return f"Proveedor(nombre={self.nombre}, tipo_producto={self.tipo_producto}, contacto={self.contacto}, " \
               f"tiempo_entrega={self.tiempo_entrega}, direccion={self.direccion}, email={self.email})"