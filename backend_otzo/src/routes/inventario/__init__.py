from flask import Blueprint

# Define el Blueprint para inventario
inventario_bp = Blueprint("inventario", __name__)

# Importa la ruta de inventario
from . import routes
