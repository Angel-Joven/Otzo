from flask import Blueprint

# Define el Blueprint para ventas
fidelizacion_bp = Blueprint("fidelizacion", __name__)

# Importa las rutas de ventas
from . import routes
