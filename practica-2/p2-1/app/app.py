# ./app/app.py
from unicodedata import name
from urllib import response
from flask import Flask, render_template, jsonify, json
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


@app.route('/fibonacci/<posicion>')
def n_esimo_fibonacci(posicion):
    posicion = int(posicion)
    # Creamos una lista con los dos primeros números de la sucesión
    fibonacci = [0, 1]

    # Recorremos la lista hasta la posición indicada
    for i in range(2, posicion + 1):
        # Calculamos el siguiente número de la sucesión
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    return str(fibonacci[posicion])


@app.route('/eratostenes/<numero>')
def criba_eratostenes(numero):
    numero = int(numero)

    # Creamos una lista con todos los números naturales
    # desde 2 hasta el número introducido
    primos = list(range(2, numero + 1))

    # Recorremos la lista de números buscando los primos
    for n in primos:
        # Cogemos el siguiente múltiplo que exista en la
        # lista de valores y lo eliminamos
        for j in range(n * n, numero + 1, n):
            if j in primos:
                primos.remove(j)

    # Mostramos los números primos
    resultado = f'Los números primos entre 2 y {numero} son:\n\n'

    for primo in primos:
        resultado += str(primo) + ' '

    return resultado


@app.route('/balanceada/<cadena>')
def is_balanceada(cadena):
    """
        Funcion que comprueba si una cadena de [ y ]
        está balanceada. Comprobamos si la expresion está balanceada
        sumando por cada [ y restando por cada ], y si el resultado
        es 0, está balanceada. Si en algún momento el valor acumulado
        es menor que 0, deja de ser balanceada.
    """

    balanceada = 'La cadena está balanceada'
    balanceo = 0

    for caracter in cadena:
        if balanceada:
            if caracter == '[':
                balanceo += 1
            else:
                balanceo -= 1

            if balanceo < 0:
                balanceada = 'La cadena está desbalanceada'
        else:
            return balanceada

    return balanceada if balanceo == 0 else 'La cadena está desbalanceada'


@app.route('/palabras/<cadena>')
def palabraEspacioMayuscula(cadena):
    """ Ejemplo: Apellido N """
    encontrado = re.search(r'^[a-zA-Z]+ [A-Z]$', cadena)

    if encontrado:
        return encontrado.group()
    else:
        return 'No encontrado'


@app.route('/email/<cadena>')
def correoElectronico(cadena):
    encontrado = re.search(r'[\w+.-]+@[\w+.-]+', cadena)

    if encontrado:
        return encontrado.group()
    else:
        return 'No encontrado'


@app.route('/tarjeta/<cadena>')
def tarjetasCredito(cadena):
    encontrado = re.search(
        r'^((([0-9]{4}\s){3})|(([0-9]{4}-){3}))[0-9]{4}$', cadena)

    if encontrado:
        return encontrado.group()
    else:
        return 'No encontrado'


@app.route('/imagen')
def imagen(name=None):
    return render_template('image.html', name=name)


@app.route('/svg')
def svg(grafico=0):
    grafico = randint(1, 4)
    return render_template('svg.html', grafico=randint(1, 4))


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
        parsed_receta = {
            '_id': str(receta['_id']),
            'name': receta['name'],
            'ingredients': receta['ingredients'],
            'instructions': receta['instructions'],
            'slug': receta['slug']
        }
        lista_recetas.append(parsed_receta)

    response = {
        "len": len(lista_recetas),
        "recetas": lista_recetas
    }

    # Devolver en JSON al cliente
    return jsonify(response)


@app.route('/receta_de/<nombre>')
def receta_de(nombre):
    recetas = db.recipes.find({'slug': nombre})

    lista_recetas = []
    for receta in recetas:
        app.logger.debug(receta)  # salida consola
        parsed_receta = {
            '_id': str(receta['_id']),
            'name': receta['name'],
            'ingredients': receta['ingredients'],
            'instructions': receta['instructions'],
            'slug': receta['slug']
        }
        lista_recetas.append(parsed_receta)

    response = {
        "len": len(lista_recetas),
        "recetas": lista_recetas
    }

    return jsonify(response)


@app.route('/recetas_con/<ingrediente>')
def recetas_con(ingrediente):
    recetas = db.recipes.find(
        {"ingredients": {"$elemMatch": {"name": ingrediente}}})

    lista_recetas = []
    for receta in recetas:
        app.logger.debug(receta)
        parsed_receta = {
            '_id': str(receta['_id']),
            'name': receta['name'],
            'ingredients': receta['ingredients'],
            'instructions': receta['instructions']
        }
        lista_recetas.append(parsed_receta)

    response = {
        "len": len(lista_recetas),
        "recetas": lista_recetas
    }

    return jsonify(response)


@app.route('/recetas_compuestas_de/<cantidad>/ingredientes')
def recetas_compuestas_de(cantidad):
    recetas = db.recipes.find(
        {"ingredients": {"$size": int(cantidad)}})

    lista_recetas = []
    for receta in recetas:
        app.logger.debug(receta)
        parsed_receta = {
            '_id': str(receta['_id']),
            'name': receta['name'],
            'ingredients': receta['ingredients'],
            'instructions': receta['instructions']
        }
        lista_recetas.append(parsed_receta)

    response = {
        "len": len(lista_recetas),
        "recetas": lista_recetas
    }

    return jsonify(response)
