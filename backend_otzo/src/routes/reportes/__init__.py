from flask import Blueprint

#Definimos el Blueprint para fidelizacion
reportes_bp = Blueprint("reportes", __name__)

#Importamos las rutas de fidelizacion
from . import routes
