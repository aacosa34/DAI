#./app/app.py
from flask import Flask, render_template
import re
from random import randint
app = Flask(__name__)
          
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
  encontrado = re.search(r'^((([0-9]{4}\s){3})|(([0-9]{4}-){3}))[0-9]{4}$', cadena)

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