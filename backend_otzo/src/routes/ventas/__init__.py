from flask import Blueprint

# Define el Blueprint para ventas
ventas_bp = Blueprint("ventas", __name__)

# Importa las rutas de ventas
from . import routes
