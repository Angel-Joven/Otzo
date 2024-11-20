# Modelos para el Modulo de Administracion
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from abc import ABC, abstractmethod

# ---------------------------------------------------------------------------------------------------------------------------

#Clase abstracta para los administradores (Administracion)
class AdministracionModelo(ABC):
    @abstractmethod
    def altaAdministrador(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, direccion_calle, direccion_colonia, direccion_codigopostal, direccion_estado, direccion_municipio, contacto_correo, contraseña, contacto_telefono, area_Trabajo):
        """Generamos el poder de crear una cuenta para algun Administrador"""
        pass

    @abstractmethod
    def bajaAdministrador(self, id_empleado):
        """Generamos el poder de dar de baja a un Administrador"""
        pass

    @abstractmethod
    def modificarAdministrador(self, id_empleado, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, direccion_calle, direccion_colonia, direccion_codigopostal, direccion_estado, direccion_municipio, contacto_correo, contraseña, contacto_telefono, area_Trabajo):
        """Generamos el poder de modificar la informacion de un Administrador"""
        pass

    @abstractmethod
    def devolverAdministradorSesionActual(self, id_empleado):
        """Devolvemos la informacion de un Administrador que ha iniciado sesion"""
        pass
    
    @abstractmethod
    def devolverAdministrador(self, id_empleado):
        """Devolvemos la informacion de un Administrador cualquiera"""
        pass

# ---------------------------------------------------------------------------------------------------------------------------