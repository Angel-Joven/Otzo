# Rutas para el Modulo de Administracion
# Creado por: JOVEN JIMENEZ ANGEL CRISTIAN

# Temas Especiales de Programacion 2 | 1061

from flask import request, jsonify, Response
from . import administracion_bp # Importar el Blueprint de Administracion
from src.services.administracion.administracionService import *
from src.db import get_connection

from src.utils.Logger import Logger
from pymysql.cursors import DictCursor

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para saber si esta funcionando nuestra api
@administracion_bp.route("/", methods=["GET"])
def index():
    try:
        return jsonify({"mensaje": "Hola - Administracion"}), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para realizar un login al administrador
@administracion_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nombre = data.get('nombre')
    contraseña = data.get('contraseña')

    if not nombre or not contraseña:
        return jsonify({"error": "El nombre y la contraseña son obligatorios"}), 400

    try:
        conexion = get_connection()
        with conexion.cursor(DictCursor) as cursor:
            cursor.execute(
                "SELECT id_empleado, nombre, contraseña FROM administracion WHERE nombre = %s",
                (nombre,)
            )
            cliente = cursor.fetchone()

        if not cliente:
            return jsonify({"error": "La cuenta no existe"}), 404
        if cliente['contraseña'] != contraseña:
            return jsonify({"error": "La contraseña es incorrecta"}), 401
        return jsonify({
            "mensaje": "Inicio de sesion exitoso",
            "id_empleado": cliente['id_empleado']
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conexion.close()

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para obtener el id del empleado que ha iniciado sesion actualmente
@administracion_bp.route('/sesionactualadmin/<int:id_empleado>', methods=['GET'])
def administrador_sesionActual(id_empleado):
    try:
        administrador = AdministracionService.devolverAdministradorSesionActual(id_empleado)
        return jsonify(administrador), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para crear un administrador (dar de alta)
@administracion_bp.route('/crearadmin', methods=['POST'])
def crear_administrador():
    try:
        data = request.get_json()
        resultado = AdministracionService.altaAdministrador(data)
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para inactivar un administrador (dar de baja)
@administracion_bp.route('/darbajaadmin/<int:id_empleado>', methods=['DELETE'])
def baja_administrador(id_empleado):
    try:
        resultado = AdministracionService.bajaAdministrador(id_empleado)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para suspender un administrador
@administracion_bp.route('/suspenderadmin/<int:id_empleado>', methods=['POST'])
def suspender_administrador(id_empleado):
    try:
        resultado = AdministracionService.suspenderAdministrador(id_empleado)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para banear un administrador
@administracion_bp.route('/banearadmin/<int:id_empleado>', methods=['POST'])
def banear_administrador(id_empleado):
    try:
        resultado = AdministracionService.banearAdministrador(id_empleado)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta para modificar la informacion de un administrador (Modificacion)
@administracion_bp.route('/modificaradmin/<int:id_empleado>', methods=['PUT'])
def modificar_administrador(id_empleado):
    try:
        data = request.get_json()
        resultado = AdministracionService.modificarAdministrador(id_empleado, data)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta que devuelve todos los administradores que existen en la BD
@administracion_bp.route('/administradores', methods=['GET'])
def devolver_lista_administradores():
    try:
        administrador = AdministracionService.devolverListaAdministradores()
        return jsonify(administrador), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------

#Ruta que devuelve a 1 administrador en concreto en base al id_empleado
@administracion_bp.route('/administradores/<int:id_empleado>', methods=['GET'])
def devolver_administrador(id_empleado):
    try:
        administrador = AdministracionService.devolverAdministrador(id_empleado)
        return jsonify(administrador), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------------------------------------------------------------------------------------------------------