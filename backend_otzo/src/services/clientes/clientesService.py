# Servicios para el Modulo de Clientes
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from src.models.clientes.clientesModels import *
from src.db import get_connection
from pymysql import DatabaseError

# ---------------------------------------------------------------------------------------------------------------------------

class ClientesService(ClientesModelo):
    def altaCliente(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, direccion_calle, direccion_colonia, direccion_codigopostal, direccion_estado, direccion_municipio, contacto_correo, contraseña, contacto_telefono):
        """Generamos el poder de crear una cuenta para algun cliente"""
        pass

    def bajaCliente(self, id_cliente):
        """Generamos el poder de dar de baja a un cliente"""
        pass

    def modificarCliente(self, id_cliente, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, direccion_calle, direccion_colonia, direccion_codigopostal, direccion_estado, direccion_municipio, contacto_correo, contraseña, contacto_telefono):
        """Generamos el poder de modificar la informacion de un cliente"""
        pass

    def devolverClienteSesionActual(self, id_cliente):
        """Devolvemos la informacion de un cliente que ha iniciado sesion"""
        pass
    
    def devolverCliente(self, id_cliente):
        """Devolvemos la informacion de un cliente cualquiera"""
        pass
