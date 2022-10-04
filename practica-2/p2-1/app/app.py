# ./app/app.py
from bson.json_util import dumps
from flask import Flask, render_template, Response
from pymongo import MongoClient
import re
from random import randint

app = Flask(__name__)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles


@app.route('/')
def hello_world():
    return 'Hello, World!'
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/todas_las_recetas')
def mongo():
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find()  # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')


@app.route('/receta_de/<nombre>')
def receta_de(nombre):
    recetas = db.recipes.find({'slug': nombre})

    lista_recetas = []
    for receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        "len": len(lista_recetas),
        "recetas": lista_recetas
    }

    resJson = dumps(response)

    return Response(resJson, mimetype='application/json')


@app.route('/recetas_con/<ingrediente>')
def recetas_con(ingrediente):
    # $elemMatch busca todas las coincidencias de lo que le pasemos
    # en la busqueda interna dentro de la lista de ingredientes
    recetas = db.recipes.find(
        {"ingredients": {"$elemMatch": {"name": ingrediente}}})

    lista_recetas = []
    for receta in recetas:
        app.logger.debug(receta)
        lista_recetas.append(receta)

    response = {
        "len": len(lista_recetas),
        "recetas": lista_recetas
    }

    resJson = dumps(response)

    return Response(resJson, mimetype='application/json')


@app.route('/recetas_compuestas_de/<cantidad>/ingredientes')
def recetas_compuestas_de(cantidad):
    recetas = db.recipes.find(
        {"ingredients": {"$size": int(cantidad)}})

    lista_recetas = []
    for receta in recetas:
        app.logger.debug(receta)
        lista_recetas.append(receta)

    response = {
        "len": len(lista_recetas),
        "recetas": lista_recetas
    }

    resJson = dumps(response)

    return Response(resJson, mimetype='application/json')
