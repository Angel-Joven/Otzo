# Rutas para el Modulo de Clientes
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from flask import request, jsonify, Response
from . import clientes_bp # Importar el Blueprint de Clientes
from src.services.clientes.clientesService import *
from src.db import get_connection

from src.utils.Logger import Logger
from pymysql.cursors import DictCursor

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para saber si esta funcionando nuestra api
@clientes_bp.route("/", methods=["GET"])
def index():
    try:
        return jsonify({"mensaje": "Hola - Clientes"}), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para realizar un login al cliente
@clientes_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nombre = data.get('nombre')
    contraseña = data.get('contraseña')

    if not nombre or not contraseña:
        return jsonify({"error": "Faltan datos de inicio de sesion"}), 400

    try:
        connection = get_connection()
        with connection.cursor(DictCursor) as cursor:
            cursor.execute(
                "SELECT idCliente, nombre, contraseña FROM clientes WHERE nombre = %s",
                (nombre,)
            )
            cliente = cursor.fetchone()

        if not cliente:
            return jsonify({"error": "La cuenta no existe"}), 404

        if cliente['contraseña'] != contraseña:
            return jsonify({"error": "La contraseña es incorrecta"}), 401

        return jsonify({
            "mensaje": "Inicio de sesion exitoso",
            "cliente": {
                "idCliente": cliente['idCliente'],
                "nombre": cliente['nombre']
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
    
# ---------------------------------------------------------------------------------------------------------------------------
