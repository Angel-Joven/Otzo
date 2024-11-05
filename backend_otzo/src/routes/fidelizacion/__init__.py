from flask import Blueprint

#Definimos el Blueprint para fidelizacion
fidelizacion_bp = Blueprint("fidelizacion", __name__)

#Importamos las rutas de fidelizacion
from . import routes
