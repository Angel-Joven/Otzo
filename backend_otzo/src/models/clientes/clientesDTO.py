# DTO para el Modulo de Clientes
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

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

class ClientesDTO(Serializable):
    def __init__(self, idCliente=None, nombre=None, apellido_paterno=None, apellido_materno=None, fecha_nacimiento=None, genero=None, direccion_calle=None, direccion_colonia=None, direccion_codigopostal=0, direccion_estado=None, direccion_municipio=None, contacto_correo=None, contraseña=None, contacto_telefono=None, fechaDe_Alta=None, ultimo_acceso=None, estado_cuenta=None):
        self._idCliente = idCliente
        self._nombre = nombre
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._fecha_nacimiento = fecha_nacimiento
        self._genero = genero
        self._direccion_calle = direccion_calle
        self._direccion_colonia = direccion_colonia
        self._direccion_codigopostal = direccion_codigopostal
        self._direccion_estado = direccion_estado
        self._direccion_municipio = direccion_municipio
        self._contacto_correo = contacto_correo
        self._contraseña = contraseña
        self._contacto_telefono = contacto_telefono
        self._fechaDe_Alta = fechaDe_Alta
        self._ultimo_acceso = ultimo_acceso
        self._estado_cuenta = estado_cuenta
    
    # Getters
    @property
    def idCliente(self):
        return self._idCliente
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido_paterno(self):
        return self._apellido_paterno
    
    @property
    def apellido_materno(self):
        return self._apellido_materno

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @property
    def genero(self):
        return self._genero
    
    @property
    def direccion_calle(self):
        return self._direccion_calle
    
    @property
    def direccion_colonia(self):
        return self._direccion_colonia
    
    @property
    def direccion_codigopostal(self):
        return self._direccion_codigopostal
    
    @property
    def direccion_municipio(self):
        return self._direccion_municipio
    
    @property
    def contacto_correo(self):
        return self._contacto_correo
    
    @property
    def contraseña(self):
        return self._contraseña
    
    @property
    def contacto_telefono(self):
        return self._contacto_telefono
    
    @property
    def fechaDe_Alta(self):
        return self._fechaDe_Alta
    
    @property
    def ultimo_acceso(self):
        return self._ultimo_acceso
    
    @property
    def estado_cuenta(self):
        return self._estado_cuenta

    # Setters
    @idCliente.setter
    def idCliente(self, value):
        if value is not None and value < 0:
            raise ValueError("El ID del cliente no puede ser negativo")
        self._idCliente = value
    
    @nombre.setter
    def nombre(self, value):
        if not value:
            raise ValueError("Este nombre no puede ser vacio")
        self._nombre = value
    
    @apellido_paterno.setter
    def apellido_paterno(self, value):
        if not value:
            raise ValueError("Este apellido paterno no puede ser vacio")
        self._apellido_paterno = value
    
    @apellido_materno.setter
    def apellido_materno(self, value):
        if not value:
            raise ValueError("Este apellido materno no puede ser vacio")
        self._apellido_materno = value
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        if not value:
            raise ValueError("Esta fecha de nacimiento no puede ser vacia")
        self._fecha_nacimiento = value
    
    @genero.setter
    def genero(self, value):
        if not value:
            raise ValueError("Este genero no puede ser vacio")
        self._genero = value
    
    @direccion_calle.setter
    def direccion_calle(self, value):
        if not value:
            raise ValueError("Esta direccion calle no puede ser vacio")
        self._direccion_calle = value
    
    @direccion_colonia.setter
    def direccion_colonia(self, value):
        if not value:
            raise ValueError("Esta direccion colonia no puede ser vacio")
        self._direccion_colonia = value
    
    @direccion_codigopostal.setter
    def direccion_codigopostal(self, value):
        if value is not None and value < 0:
            raise ValueError("Esta direccion codigo postal no puede ser vacio")
        self._direccion_codigopostal = value
    
    @direccion_municipio.setter
    def direccion_municipio(self, value):
        if not value:
            raise ValueError("Esta direccion municipio no puede ser vacio")
        self._direccion_municipio = value
    
    @contacto_correo.setter
    def contacto_correo(self, value):
        if not value:
            raise ValueError("Este contacto correo no puede ser vacio")
        self._contacto_correo = value
    
    @contraseña.setter
    def contraseña(self, value):
        if not value:
            raise ValueError("Esta contraseña no puede ser vacia")
        self._contraseña = value
    
    @contacto_telefono.setter
    def contacto_telefono(self, value):
        if not value:
            raise ValueError("Este contacto telefono no puede ser vacio")
        self._contacto_telefono = value
    
    @fechaDe_Alta.setter
    def fechaDe_Alta(self, value):
        if not value:
            raise ValueError("Esta fecha de alta no puede ser vacia")
        self._fechaDe_Alta = value
    
    @ultimo_acceso.setter
    def ultimo_acceso(self, value):
        if not value:
            raise ValueError("Esta fecha de ultimo acceso no puede ser vacia")
        self._ultimo_acceso = value
    
    @estado_cuenta.setter
    def estado_cuenta(self, value):
        if not value:
            raise ValueError("Este estado cuenta no puede ser vacio")
        self._estado_cuenta = value 

# ---------------------------------------------------------------------------------------------------------------------------

print("---------------------------------------------------------------------------------------------------------------------------")
print("CLIENTES DTO")

# ClientesDTO - EJEMPLO TEST
cliente_dto = ClientesDTO(
    idCliente=1,
    nombre="Juan",
    apellido_paterno="Perez",
    apellido_materno="Lopez",
    fecha_nacimiento="1985-05-10",
    genero="Masculino",
    direccion_calle="Calle Falsa 123",
    direccion_colonia="Centro",
    direccion_codigopostal=12345,
    direccion_estado="Ciudad de México",
    direccion_municipio="Cuauhtémoc",
    contacto_correo="juan.perez@example.com",
    contraseña="pass1234",
    contacto_telefono="5551234567",
    fechaDe_Alta="2024-11-20 08:00:00",
    ultimo_acceso="2024-11-20 10:00:00",
    estado_cuenta="Activo"
)

# ---------------------------------------------------------------------------------------------------------------------------

print("---------------------------------------------------------------------------------------------------------------------------")

#Convertimos a JSON - EJEMPLO TEST
json_data = cliente_dto.to_json()
print("JSON:", json_data)
#JSON: {"_idCliente": 1, "_nombre": "Juan", "_apellido_paterno": "Perez", "_apellido_materno": "Lopez", "_fecha_nacimiento": "1985-05-10", "_genero": "Masculino", "_direccion_calle": "Calle Falsa 123", "_direccion_colonia": "Centro", "_direccion_codigopostal": 12345, "_direccion_estado": "Ciudad de M\u00e9xico", "_direccion_municipio": "Cuauht\u00e9moc", "_contacto_correo": "juan.perez@example.com", "_contrase\u00f1a": "pass1234", "_contacto_telefono": "5551234567", "_fechaDe_Alta": "2024-11-20 08:00:00", "_ultimo_acceso": "2024-11-20 10:00:00", "_estado_cuenta": "Activo"}

#Reconstruimos desde un JSON - EJEMPLO TEST
nuevo_cliente_dto = ClientesDTO.from_json(json_data)
print("Nuevo DTO:", nuevo_cliente_dto.to_dict())
#Nuevo DTO: {'_idCliente': 1, '_nombre': 'Juan', '_apellido_paterno': 'Perez', '_apellido_materno': 'Lopez', '_fecha_nacimiento': '1985-05-10', '_genero': 'Masculino', '_direccion_calle': 'Calle Falsa 123', '_direccion_colonia': 'Centro', '_direccion_codigopostal': 12345, '_direccion_estado': 'Ciudad de México', '_direccion_municipio': 'Cuauhtémoc', '_contacto_correo': 'juan.perez@example.com', '_contraseña': 'pass1234', '_contacto_telefono': '5551234567', '_fechaDe_Alta': '2024-11-20 08:00:00', '_ultimo_acceso': '2024-11-20 10:00:00', '_estado_cuenta': 'Activo'}
print("ID del cliente:", cliente_dto.idCliente)
print("Nombre del cliente:", cliente_dto.nombre)
print("Correo del cliente:", cliente_dto.contacto_correo)

print("---------------------------------------------------------------------------------------------------------------------------")

# ---------------------------------------------------------------------------------------------------------------------------