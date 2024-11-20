# Servicios para el Modulo de Clientes
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from src.models.administracion.administracionModels import *
from src.db import get_connection
from pymysql import DatabaseError

# ---------------------------------------------------------------------------------------------------------------------------

class AdministracionService(AdministracionModelo):
    def altaAdministrador(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, direccion_calle, direccion_colonia, direccion_codigopostal, direccion_estado, direccion_municipio, contacto_correo, contraseña, contacto_telefono, area_Trabajo):
        """Generamos el poder de crear una cuenta para algun Administrador"""
        pass

    def bajaAdministrador(self, id_empleado):
        """Generamos el poder de dar de baja a un Administrador"""
        pass

    def modificarAdministrador(self, id_empleado, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, direccion_calle, direccion_colonia, direccion_codigopostal, direccion_estado, direccion_municipio, contacto_correo, contraseña, contacto_telefono, area_Trabajo):
        """Generamos el poder de modificar la informacion de un Administrador"""
        pass

    def devolverAdministradorSesionActual(self, id_empleado):
        """Devolvemos la informacion de un Administrador que ha iniciado sesion"""
        pass
    
    def devolverAdministrador(self, id_empleado):
        """Devolvemos la informacion de un Administrador cualquiera"""
        pass