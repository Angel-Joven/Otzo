# Blueprint para el Modulo de Administracion
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from flask import Blueprint

#Definimos el Blueprint para administracion
administracion_bp = Blueprint("administracion", __name__)

#Importamos las rutas de administracion
from . import routes
