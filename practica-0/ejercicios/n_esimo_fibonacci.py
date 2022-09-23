fichero_lectura = open("posicion.txt", "r")

posicion = int(fichero_lectura.read())

# Creamos una lista con los dos primeros números de la sucesión
fibonacci = [0, 1]

# Recorremos la lista hasta la posición indicada
for i in range(2, posicion + 1):
    # Calculamos el siguiente número de la sucesión
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

# Escribimos el valor en el fichero de salida
fichero_escritura = open("valor.txt", "w")
fichero_escritura.write(str(fibonacci[posicion]))