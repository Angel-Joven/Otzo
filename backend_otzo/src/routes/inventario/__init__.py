from flask import Blueprint

# Define el Blueprint para ventas
inventario_bp = Blueprint("inventario", __name__)

# Importa las rutas de ventas
from . import routes
