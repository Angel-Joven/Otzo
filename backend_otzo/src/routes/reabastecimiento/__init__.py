from flask import Blueprint

# Define el Blueprint para reabastecimiento
reabastecimiento_bp = Blueprint("reabastecimiento", __name__)

# Importa las rutas de reabastecimiento
from . import routes