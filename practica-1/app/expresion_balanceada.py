# Importamos las funciones necesarias para
# generar aleatoriamente valores
from random import randint, choice

def isBalanceada(cadena):
    """ 
        Funcion que comprueba si una cadena de [ y ] 
        está balanceada. Comprobamos si la expresion está balanceada 
        sumando por cada [ y restando por cada ], y si el resultado
        es 0, está balanceada. Si en algún momento el valor acumulado
        es menor que 0, deja de ser balanceada.
    """

    balanceada = True
    balanceo = 0
    
    for caracter in cadena:
        if balanceada:
            if caracter == '[':
                balanceo += 1
            else:
                balanceo -= 1

            if balanceo < 0:
                balanceada = False
        else:
            return balanceada 

    return balanceo == 0

# Inicializamos variables a usar 
# como el tamaño del string
tamanio = randint(2, 16)
cadena = ''

# Generamos una cadena de [ o ] en funcion
# del tamaño escogido por randint
for i in range(0, tamanio + 1):
    cadena += choice(['[', ']'])

if isBalanceada(cadena):
    print(f"{cadena} -> Correcto")
else:
    print(f"{cadena} -> Incorrecto")