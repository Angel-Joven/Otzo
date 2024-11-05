from flask import Blueprint

# Define el Blueprint para atención al cliente
atencion_bp = Blueprint("atencion", __name__)

# Importa las rutas de atención al cliente
from . import routes