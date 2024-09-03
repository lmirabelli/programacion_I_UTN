#LEONARDO MIRABELLI

# Una función sumar1 que reciba dos números y retorne el resultado

def sumar1(numero_uno: int, numero_dos: int) -> int:
    '''Suma 2 numeros ingresados por parametros y devuelve el resultado'''
    resultado = numero_uno + numero_dos

    return resultado

numero_a = int(input("ingrese un numero (1/2): "))
numero_b = int(input("ingrese un numero (2/2): "))

# Una función sumar2 que reciba dos números y no retorne nada (o sea que la función se encargue de mostrar el resultado)

def sumar2(numero_uno: int, numero_dos: int) -> int:
    '''Suma 2 numeros ingresados por parametros y no devuelve ni aka'''
    resultado = numero_uno + numero_dos
    print(f"sumar2: La suma de {numero_uno} y {numero_dos} da como resultado {resultado}")

# Una función sumar3 que no reciba nada y se encargue de pedir dos números y retornar el resultado

def sumar3():
    '''Suma 2 numeros ingresados dentro de la funcion y devuelve el resultado'''
    numero_uno = int(input("ingrese un numero (1/2): "))
    numero_dos = int(input("ingrese un numero (2/2): "))
    resultado = numero_uno + numero_dos

    return resultado

# Una función sumar4 que no reciba nada y no retorne nada, por ende se va encargar de pedir los numeros y de mostrar el resultado.

def sumar4():
    '''Suma 2 numeros ingresados dentro de la funcion y ni esperes la devolucion'''
    numero_uno = int(input("ingrese un numero (1/2): "))
    numero_dos = int(input("ingrese un numero (2/2): "))
    resultado = numero_uno + numero_dos
    print(f"sumar4: La suma de {numero_uno} y {numero_dos} da como resultado {resultado}")

suma1 = sumar1(numero_a,numero_b)
print(f"sumar1: La suma de {numero_a} y {numero_b} da como resultado {suma1}")
sumar2(numero_a,numero_b)
suma3 = sumar3()
print(f"sumar3: da como resultado {suma3}")
sumar4()