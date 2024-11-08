# Blueprint para el Modulo de Fidelizacion y Marketing
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from flask import Blueprint

#Definimos el Blueprint para fidelizacion
fidelizacion_bp = Blueprint("fidelizacion", __name__)

#Importamos las rutas de fidelizacion
from . import routes
