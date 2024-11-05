from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para obtener todos los proveedores
@app.route('/proveedores', methods=['GET'])
def obtener_proveedores():
    # Código para obtener la lista de proveedores
    return jsonify({"message": "Lista de proveedores"})

# Ruta para obtener un proveedor por su ID
@app.route('/proveedores/<int:id_proveedor>', methods=['GET'])
def obtener_proveedor(id_proveedor):
    # Código para obtener un proveedor específico
    return jsonify({"message": f"Proveedor con ID {id_proveedor}"})

# Ruta para crear un nuevo proveedor
@app.route('/proveedores', methods=['POST'])
def crear_proveedor():
    data = request.get_json()
    # Código para crear un proveedor usando data
    return jsonify({"message": "Proveedor creado"}), 201

# Ruta para actualizar un proveedor por su ID
@app.route('/proveedores/<int:id_proveedor>', methods=['PUT'])
def actualizar_proveedor(id_proveedor):
    data = request.get_json()
    # Código para actualizar el proveedor usando data
    return jsonify({"message": f"Proveedor con ID {id_proveedor} actualizado"})

# Ruta para eliminar un proveedor por su ID
@app.route('/proveedores/<int:id_proveedor>', methods=['DELETE'])
def eliminar_proveedor(id_proveedor):
    # Código para eliminar el proveedor
    return jsonify({"message": f"Proveedor con ID {id_proveedor} eliminado"})

# Ruta para obtener todos los reabastecimientos
@app.route('/reabastecimientos', methods=['GET'])
def obtener_reabastecimientos():
    # Código para obtener la lista de reabastecimientos
    return jsonify({"message": "Lista de reabastecimientos"})

# Ruta para obtener un reabastecimiento por su ID
@app.route('/reabastecimientos/<int:id_reabastecimiento>', methods=['GET'])
def obtener_reabastecimiento(id_reabastecimiento):
    # Código para obtener un reabastecimiento específico
    return jsonify({"message": f"Reabastecimiento con ID {id_reabastecimiento}"})

# Ruta para crear un nuevo reabastecimiento
@app.route('/reabastecimientos', methods=['POST'])
def crear_reabastecimiento():
    data = request.get_json()
    # Código para crear un reabastecimiento usando data
    return jsonify({"message": "Reabastecimiento creado"}), 201

# Ruta para actualizar un reabastecimiento por su ID
@app.route('/reabastecimientos/<int:id_reabastecimiento>', methods=['PUT'])
def actualizar_reabastecimiento(id_reabastecimiento):
    data = request.get_json()
    # Código para actualizar el reabastecimiento usando data
    return jsonify({"message": f"Reabastecimiento con ID {id_reabastecimiento} actualizado"})

# Ruta para eliminar un reabastecimiento por su ID
@app.route('/reabastecimientos/<int:id_reabastecimiento>', methods=['DELETE'])
def eliminar_reabastecimiento(id_reabastecimiento):
    # Código para eliminar el reabastecimiento
    return jsonify({"message": f"Reabastecimiento con ID {id_reabastecimiento} eliminado"})

if __name__ == '__main__':
    app.run(debug=True)
