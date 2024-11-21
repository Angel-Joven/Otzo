# Rutas para el Modulo de Clientes
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from flask import request, jsonify, Response
from . import clientes_bp  # Importar el Blueprint de Clientes
from src.services.clientes.clientesService import ClientesService
from src.db import get_connection

from src.utils.Logger import Logger
from pymysql.cursors import DictCursor

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para saber si está funcionando nuestra API
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
            "mensaje": "Inicio de sesión exitoso",
            "idCliente": cliente['idCliente']
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para obtener el cliente que ha iniciado sesion actualmente
@clientes_bp.route('/sesionactualcliente/<int:id_cliente>', methods=['GET'])
def cliente_sesion_actual(id_cliente):
    try:
        cliente = ClientesService.devolverClienteSesionActual(id_cliente)
        return jsonify(cliente), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para crear un cliente (dar de alta)
@clientes_bp.route('/crearcliente', methods=['POST'])
def crear_cliente():
    try:
        data = request.get_json()
        resultado = ClientesService.altaCliente(data)
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para dar de baja un cliente (dar de baja)
@clientes_bp.route('/darbajacliente/<int:id_cliente>', methods=['DELETE'])
def baja_cliente(id_cliente):
    try:
        resultado = ClientesService.bajaCliente(id_cliente)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para suspender un cliente
@clientes_bp.route('/suspendercliente/<int:id_cliente>', methods=['POST'])
def suspender_cliente(id_cliente):
    try:
        resultado = ClientesService.suspenderCliente(id_cliente)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

# Ruta para modificar la información de un cliente
@clientes_bp.route('/modificarcliente/<int:id_cliente>', methods=['PUT'])
def modificar_cliente(id_cliente):
    try:
        data = request.get_json()
        resultado = ClientesService.modificarCliente(id_cliente, data)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta que devuelve todos los clientes que existen en la BD
@clientes_bp.route('/clientes', methods=['GET'])
def devolver_lista_clientes():
    try:
        clientes = ClientesService.devolverListaClientes()
        return jsonify(clientes), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta que devuelve a 1 cliente en concreto en base al id_cliente
@clientes_bp.route('/clientes/<int:id_cliente>', methods=['GET'])
def devolver_cliente(id_cliente):
    try:
        cliente = ClientesService.devolverCliente(id_cliente)
        return jsonify(cliente), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------
