import re

def palabraEspacioMayuscula(cadena):
    """ Ejemplo: Apellido N """
    encontrado = re.search(r'^[a-zA-Z]+ [A-Z]$', cadena)

    if encontrado:
        print(encontrado.group())
    else:
        print('No encontrado')

palabraEspacioMayuscula('holacaracola H')


def correoElectronico(cadena):
    encontrado = re.search(r'[\w+.-]+@[\w+.-]+', cadena)

    if encontrado:
        print(encontrado.group())
    else:
        print('No encontrado')

correoElectronico('adri.acosa@gmail.com')


def tarjetasCredito(cadena):
    encontrado = re.search(r'^((([0-9]{4}\s){3})|(([0-9]{4}-){3}))[0-9]{4}$', cadena)

    if encontrado:
        print(encontrado.group())
    else:
        print('No encontrado')

tarjetasCredito('1234 1234 1234 1234')

