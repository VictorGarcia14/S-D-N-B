from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configuración de la conexión a MongoDB Atlas
app.config['MONGO_URI'] = 'mongodb+srv://<usuario>:<contraseña>@<cluster>.mongodb.net/<base_de_datos>?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/equipos', methods=['GET'])
def obtener_equipos():
    equipos = mongo.db.equipos.find()
    resultados = []
    for equipo in equipos:
        equipo_data = {'id': str(equipo['_id']), 'nombre': equipo['nombre']}
        resultados.append(equipo_data)
    return jsonify(resultados)


@app.route('/equipos', methods=['POST'])
def crear_equipo():
    datos = request.get_json()
    nombre = datos['nombre']
    nuevo_equipo = {'nombre': nombre}
    equipo_id = mongo.db.equipos.insert_one(nuevo_equipo).inserted_id
    return jsonify({'mensaje': 'Equipo creado exitosamente', 'id': str(equipo_id)})


@app.route('/equipos/<equipo_id>', methods=['GET'])
def obtener_equipo(equipo_id):
    equipo = mongo.db.equipos.find_one({'_id': ObjectId(equipo_id)})
    if equipo:
        equipo_data = {'id': str(equipo['_id']), 'nombre': equipo['nombre']}
        return jsonify(equipo_data)
    else:
        return jsonify({'mensaje': 'Equipo no encontrado'}), 404


@app.route('/equipos/<equipo_id>', methods=['PUT'])
def actualizar_equipo(equipo_id):
    equipo = mongo.db.equipos.find_one({'_id': ObjectId(equipo_id)})
    if equipo:
        datos = request.get_json()
        nombre = datos['nombre']
        mongo.db.equipos.update_one({'_id': ObjectId(equipo_id)}, {'$set': {'nombre': nombre}})
        return jsonify({'mensaje': 'Equipo actualizado exitosamente'})
    else:
        return jsonify({'mensaje': 'Equipo no encontrado'}), 404


@app.route('/equipos/<equipo_id>', methods=['DELETE'])
def eliminar_equipo(equipo_id):
    equipo = mongo.db.equipos.find_one({'_id': ObjectId(equipo_id)})
    if equipo:
        mongo.db.equipos.delete_one({'_id': ObjectId(equipo_id)})
        return jsonify({'mensaje': 'Equipo eliminado exitosamente'})
    else:
        return jsonify({'mensaje': 'Equipo no encontrado'}), 404


@app.route('/jugadores', methods=['GET'])
def obtener_jugadores():
    jugadores = mongo.db.jugadores.find()
    resultados = []
    for jugador in jugadores:
        jugador_data = {'id': str(jugador['_id']), 'nombre': jugador['nombre'], 'equipo_id': jugador['equipo_id']}
        resultados.append(jugador_data)
    return jsonify(resultados)


@app.route('/jugadores', methods=['POST'])
def crear_jugador():
    datos = request.get_json()
    nombre = datos['nombre']
    equipo_id = datos['equipo_id']
    nuevo_jugador = {'nombre': nombre, 'equipo_id': equipo_id}
    jugador_id = mongo.db.jugadores.insert_one(nuevo_jugador).inserted_id
    return jsonify({'mensaje': 'Jugador creado exitosamente', 'id': str(jugador_id)})


@app.route('/jugadores/<jugador_id>', methods=['GET'])
def obtener_jugador(jugador_id):
    jugador = mongo.db.jugadores.find_one({'_id': ObjectId(jugador_id)})
    if jugador:
        jugador_data = {'id': str(jugador['_id']), 'nombre': jugador['nombre'], 'equipo_id': jugador['equipo_id']}
        return jsonify(jugador_data)
    else:
        return jsonify({'mensaje': 'Jugador no encontrado'}), 404


@app.route('/jugadores/<jugador_id>', methods=['PUT'])
def actualizar_jugador(jugador_id):
    jugador = mongo.db.jugadores.find_one({'_id': ObjectId(jugador_id)})
    if jugador:
        datos = request.get_json()
        nombre = datos['nombre']
        equipo_id = datos['equipo_id']
        mongo.db.jugadores.update_one({'_id': ObjectId(jugador_id)}, {'$set': {'nombre': nombre, 'equipo_id': equipo_id}})
        return jsonify({'mensaje': 'Jugador actualizado exitosamente'})
    else:
        return jsonify({'mensaje': 'Jugador no encontrado'}), 404

@app.route('/jugadores/<jugador_id>', methods=['DELETE'])
def eliminar_jugador(jugador_id):
    jugador = mongo.db.jugadores.find_one({'_id': ObjectId(jugador_id)})
    if jugador:
        mongo.db.jugadores.delete_one({'_id': ObjectId(jugador_id)})
        return jsonify({'mensaje': 'Jugador eliminado exitosamente'})
    else:
        return jsonify({'mensaje': 'Jugador no encontrado'}), 404


@app.route('/nominas', methods=['GET'])
def obtener_nominas():
    nominas = mongo.db.nominas.find()
    resultados = []
    for nomina in nominas:
        nomina_data = {'id': str(nomina['_id']), 'nombre': nomina['nombre'], 'cantidad': nomina['cantidad']}
        resultados.append(nomina_data)
    return jsonify(resultados)


@app.route('/nominas', methods=['POST'])
def crear_nomina():
    datos = request.get_json()
    nombre = datos['nombre']
    cantidad = datos['cantidad']
    nueva_nomina = {'nombre': nombre, 'cantidad': cantidad}
    nomina_id = mongo.db.nominas.insert_one(nueva_nomina).inserted_id
    return jsonify({'mensaje': 'Nómina creada exitosamente', 'id': str(nomina_id)})


@app.route('/nominas/<nomina_id>', methods=['GET'])
def obtener_nomina(nomina_id):
    nomina = mongo.db.nominas.find_one({'_id': ObjectId(nomina_id)})
    if nomina:
        nomina_data = {'id': str(nomina['_id']), 'nombre': nomina['nombre'], 'cantidad': nomina['cantidad']}
        return jsonify(nomina_data)
    else:
        return jsonify({'mensaje': 'Nómina no encontrada'}), 404


@app.route('/nominas/<nomina_id>', methods=['PUT'])
def actualizar_nomina(nomina_id):
    nomina = mongo.db.nominas.find_one({'_id': ObjectId(nomina_id)})
    if nomina:
        datos = request.get_json()
        nombre = datos['nombre']
        cantidad = datos['cantidad']
        mongo.db.nominas.update_one({'_id': ObjectId(nomina_id)}, {'$set': {'nombre': nombre, 'cantidad': cantidad}})
        return jsonify({'mensaje': 'Nómina actualizada exitosamente'})
    else:
        return jsonify({'mensaje': 'Nómina no encontrada'}), 404


@app.route('/nominas/<nomina_id>', methods=['DELETE'])
def eliminar_nomina(nomina_id):
    nomina = mongo.db.nominas.find_one({'_id': ObjectId(nomina_id)})
    if nomina:
        mongo.db.nominas.delete_one({'_id': ObjectId(nomina_id)})
        return jsonify({'mensaje': 'Nómina eliminada exitosamente'})
    else:
        return jsonify({'mensaje': 'Nómina no encontrada'}), 404

if __name__ == "__main__":
    app.run()