# ./app/app.py
from bson.json_util import dumps
from bson import ObjectId
from flask import Flask, render_template, Response, request, jsonify
from pymongo import MongoClient
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

# Inicializar el API
api = Api(app)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles

# Crear el modelo para la coleccion que vamos a devolver
class Recipes(Resource):
    def get(self, id=None):
        if id is None:
            if request.args.get('con'):
                ingrediente = request.args.get('con')
                recetas = db.recipes.find(
                    {"ingredients": {"$elemMatch": {"name": {"$regex": ingrediente, "$options": 'i'}}}})
                lista_recetas = []
                for receta in recetas:
                    app.logger.debug(receta)
                    lista_recetas.append(receta)

                if lista_recetas:
                    response = {
                        "len": len(lista_recetas),
                        "recetas": lista_recetas
                    }

                    resJson = dumps(response)

                    return Response(resJson, mimetype='application/json')
                else:
                    return jsonify({'error': 'No hay recetas'}), 404
            else:
                lista = []
                buscados = db.recipes.find().sort('name')
                if buscados:
                    for recipe in buscados:
                        recipe['_id'] = str(recipe['_id'])  # paso a string
                        lista.append(recipe)
                    return jsonify(lista)
                else:
                    return jsonify({'error': 'No hay recetas'}), 404
        else:
            buscado = db.recipes.find_one({'_id': ObjectId(id)})
            if buscado:
                resJson = dumps(buscado)
                return Response(resJson, mimetype='application/json')
            else:
                return jsonify({'error': 'Not found'}), 404

    def post(self):
        recipe = db.recipes.insert_one(request.json).inserted_id
        response = request.json
        response['_id'] = str(recipe)
        
        return jsonify(response), 201

    def put(self):
        json = request.json
        db.recipes.update_one({'_id': ObjectId(id)}, {'$set': json})
        json['_id'] = id
        resJson = dumps(json)
        return Response(resJson, mimetype="application/json"), 202

    def delete(self, id):
        db.recipes.delete_one({'_id': ObjectId(id)})
        return jsonify({'deleted_id': id}), 202
    
api.add_resource(Recipes, '/api2/recipes', '/api2/recipes/<string:id>')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# para devolver una lista (GET), o añadir (POST)
@app.route('/api1/recipes', methods=['GET', 'POST'])
def api1_1():
    if request.method == 'GET' and not request.args.get('con'):
        lista = []
        buscados = db.recipes.find().sort('name')
        if buscados:
            for recipe in buscados:
                recipe['_id'] = str(recipe['_id'])  # paso a string
                lista.append(recipe)
            return jsonify(lista)
        else:
            return jsonify({'error': 'No hay recetas'}), 404
    elif request.method == 'GET' and request.args.get('con'):
        ingrediente = request.args.get('con')
        recetas = db.recipes.find(
            {"ingredients": {"$elemMatch": {"name": {"$regex": ingrediente, "$options": 'i'}}}})
        lista_recetas = []
        for receta in recetas:
            app.logger.debug(receta)
            lista_recetas.append(receta)

        if lista_recetas:
            response = {
                "len": len(lista_recetas),
                "recetas": lista_recetas
            }

            resJson = dumps(response)

            return Response(resJson, mimetype='application/json')
        
        else:
            return jsonify({'error': 'No hay recetas'}), 404

    if request.method == 'POST':
        recipe = db.recipes.insert_one(request.json).inserted_id
        response = request.json
        response['_id'] = str(recipe)
        
        return jsonify(response), 201

# para devolver una, modificar o borrar
@app.route('/api1/recipes/<id>', methods=['GET', 'PUT', 'DELETE'])
def api1_2(id):
    if request.method == 'GET':
        buscado = db.recipes.find_one({'_id': ObjectId(id)})
        if buscado:
            resJson = dumps(buscado)
            return Response(resJson, mimetype='application/json')
        else:
            return jsonify({'error': 'Not found'}), 404

    if request.method == 'PUT':
        json = request.json
        db.recipes.update_one({'_id': ObjectId(id)}, {'$set': json})
        json['_id'] = id
        resJson = dumps(json)
        return Response(resJson, mimetype="application/json"), 202

    if request.method == 'DELETE':
        db.recipes.delete_one({'_id': ObjectId(id)})
        return jsonify({'deleted_id': id}), 202