# Blueprint para el Modulo de Clientes
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from flask import Blueprint

#Definimos el Blueprint para clientes
clientes_bp = Blueprint("clientes", __name__)

#Importamos las rutas de clientes
from . import routes
