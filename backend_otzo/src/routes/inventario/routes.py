from flask import request, jsonify, Response
from pymysql.cursors import DictCursor
from src.db import get_connection
from datetime import datetime
from decimal import Decimal
from . import ventas_bp  # Importa el Blueprint de inventario
import json
from flask_cors import cross_origin

from src.models.inventario.inventarioDTO import inventarioDTO

