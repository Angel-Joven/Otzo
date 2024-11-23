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

#Ruta para crear un cliente desde el login (dar de alta)
@clientes_bp.route('/crearclientelogin', methods=['POST'])
def crear_cliente_login():
    try:
        data = request.get_json()
        resultado = ClientesService.altaClienteLogin(data)
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para verificar si un cliente ya existe en la BD en base al correo, nombre, apellido paterno y materno proporcionados
@clientes_bp.route('/verificarcliente', methods=['POST'])
def verificar_cliente():
    try:
        data = request.get_json()
        correo = data.get('contacto_correo')
        nombre = data.get('nombre')
        apellido_paterno = data.get('apellido_paterno')
        apellido_materno = data.get('apellido_materno')

        if not correo or not nombre or not apellido_paterno or not apellido_materno:
            return jsonify({"error": "Faltan datos para la verificacion"}), 400

        connection = get_connection()
        with connection.cursor(DictCursor) as cursor:
            cursor.execute(
                "SELECT COUNT(*) as cuenta FROM clientes WHERE contacto_correo = %s AND nombre = %s AND apellido_paterno = %s AND apellido_materno = %s",
                (correo, nombre, apellido_paterno, apellido_materno)
            )
            resultado = cursor.fetchone()

        if resultado['cuenta'] > 0:
            return jsonify({"existe": True, "mensaje": "El cliente ya existe"}), 200
        else:
            return jsonify({"existe": False}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para resetear la contraseña de un cliente
@clientes_bp.route('/resetearcontraseña', methods=['POST'])
def resetear_contraseña():
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        apellido_paterno = data.get('apellido_paterno')
        apellido_materno = data.get('apellido_materno')
        nueva_contraseña = data.get('nueva_contraseña')

        if not nombre or not apellido_paterno or not apellido_materno or not nueva_contraseña:
            return jsonify({"error": "Faltan datos para resetear la contraseña"}), 400

        connection = get_connection()
        with connection.cursor(DictCursor) as cursor:
            cursor.execute(
                "SELECT idCliente FROM clientes WHERE nombre = %s AND apellido_paterno = %s AND apellido_materno = %s",
                (nombre, apellido_paterno, apellido_materno)
            )
            cliente = cursor.fetchone()

        if not cliente:
            return jsonify({"error": "Cliente no encontrado"}), 404

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE clientes SET contraseña = %s WHERE idCliente = %s",
                (nueva_contraseña, cliente['idCliente'])
            )
            connection.commit()

        return jsonify({"mensaje": "Contraseña actualizada con exito"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para dar de alta a un cliente (dar de alta estatus)
@clientes_bp.route('/daraltacliente/<int:id_cliente>', methods=['POST'])
def alta_cliente(id_cliente):
    try:
        resultado = ClientesService.altaClienteBoton(id_cliente)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para dar de baja un cliente (dar de baja)
@clientes_bp.route('/darbajacliente/<int:id_cliente>', methods=['POST'])
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
