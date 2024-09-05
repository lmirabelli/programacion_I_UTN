

def sumar (valor_uno, valor_dos):
    suma = valor_uno + valor_dos
    return suma

def restar (valor_uno, valor_dos):
    resta = valor_uno - valor_dos
    return resta

def multiplicar (valor_uno, valor_dos):
    multiplicacion = valor_uno * valor_dos
    return multiplicacion

def dividir (valor_uno, valor_dos):
    if valor_dos != 0:
        division = valor_uno / valor_dos
    else:
        division = "no se puede dividir por 0"
    return division

def potenciar (valor_uno, valor_dos):
    potencia = valor_uno ** valor_dos
    return potencia

def factorial(valor):
    factorizacion = 1
    for i in range(2, valor + 1):
        factorizacion *= i

    return factorizacion
