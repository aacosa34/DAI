numero = int(input('Introduce un número natural: '))

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
print(f'Los números primos entre 2 y {numero} son:')

for primo in primos:
    print(primo, end=' ')
