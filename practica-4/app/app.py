# ./app/app.py
import mimetypes
from bson.json_util import dumps
from bson import ObjectId
from flask import Flask, render_template, Response, request
from pymongo import MongoClient
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

# Inicializar el API
api = Api(app)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles


recipes_put_args = reqparse.RequestParser()
recipes_put_args.add_argument("name", type=str, help="Name of the recipe is required", required=True)
recipes_put_args.add_argument("ingredients", type=list, help="Ingredients of the recipe is required", required=True)
recipes_put_args.add_argument("instructions", type=list, help="Instructions of the recipe is required", required=True)
recipes_put_args.add_argument("slug", type=str, help="Slug of the recipe is required", required=True)


# Crear el modelo para la coleccion que vamos a devolver
class Recipes(Resource):
    def get(self, id=None):
        if id is None:
            if request.args.get('con'):
                ingrediente = request.args.get('con')
                recetas = db.recipes.find(
                    {"ingredients": {"$elemMatch": {"name": {"$regex": ingrediente, "$options": 'i'}}}})
            else:
                recetas = db.recipes.find().sort('name')

            
            lista_recetas = []
            for receta in recetas:
                app.logger.debug(receta)
                lista_recetas.append(receta)

            if lista_recetas:            
                respuesta = {
                    "len": len(lista_recetas),
                    "recetas": lista_recetas
                }

                resJson = dumps(respuesta)

                return Response(resJson, mimetype='application/json')
            else:
                return {'error': 'No se encontraron recetas'}, 404


        else:
            buscado = db.recipes.find_one({'_id': ObjectId(id)})
            if buscado:
                resJson = dumps(buscado)
                return Response(resJson, mimetype='application/json')
            else:
                return {'error': 'Receta con id ' + str(id) + ' no entontrada'}, 404

    def post(self):
        recipe = db.recipes.insert_one(request.json).inserted_id
        response = request.json
        response['_id'] = str(recipe)
        
        return response, 201

    def put(self, id):
        args = recipes_put_args.parse_args()
        if db.recipes.find_one({'_id': ObjectId(id)}):
            json = request.json
            db.recipes.update_one({'_id': ObjectId(id)}, {'$set': args})    
            json['_id'] = id
            return json, 202
        else:
            return {'error': 'Receta con id ' + str(id) + ' no entontrada'}, 404

    def delete(self, id):
        if db.recipes.find_one({'_id': ObjectId(id)}):
            db.recipes.delete_one({'_id': ObjectId(id)})
            return {'message': 'Receta con id ' + str(id) + ' eliminada'}, 202
        else:
            return {'error': 'Receta con id ' + str(id) + ' no entontrada'}, 404
    
api.add_resource(Recipes, '/api/recipes', '/api/recipes/<string:id>')

@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
