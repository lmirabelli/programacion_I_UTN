# LEONARDO MIRABELLI
# D.114

# 1.Crear una función que reciba dos números (acumulador y contador) y calcule el promedio, en caso de que haya división por cero imprimir un mensaje de error.
def calcular_promedio(numero_uno : float, numero_dos : float) -> float:
    '''Segun los valores tomados en las varibales numero_a y numero_b calcula el promedio entre 2 numeros'''
    resultado = numero_uno / numero_dos

    return resultado

# 2.Crear una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.
def calcular_area(numero_uno : float, numero_dos : float) -> float:
    '''Segun los valores tomados en las varibales numero_a y numero_b calcula el area de un rectangulo, si algun numero es negativo se lo multiplicara por "-1" para que sea positivo'''

    if numero_uno < 0:
        numero_uno * -1
    if numero_dos < 0:
        numero_dos * -1

    resultado = numero_uno * numero_dos
    return resultado

# 3.Crear una función que verifique si un número es par o no, devuelve True si es par, y False si es impar
def calcular_si_par_o_impar(numero : float) -> bool:
    ''' Segun el dato ingresado en el parametro numero (que es tomado por la variable numero_a) verifica si es par o impar'''
    resultado = numero % 2
    if resultado == 0:
        es_par = True
    else:
        es_par = False
    
    return es_par

# 4.Crear una función que verifique si un primo o no, devuelve True si es primo, False si no lo es
def calcular_primo(numero : float) -> bool:
    '''Segun el parametro calcula si el numero es primo o no'''
    divisores = 0
    
    for i in range(2, int(numero) - 1):
        verificacion_primo = numero % i
        if verificacion_primo == 0:
            divisores = 1
            break

    es_primo = False
    if divisores == 0:
        es_primo = True
    
    return es_primo

# 5.Crear una función qué encuentre el máximo entre tres números. Debe aceptar tres argumentos y retornar el número más grande.
def calcular_maximo(numero_uno : int, numero_dos : int , numero_tres : int) -> int:
    '''Segun los numeros ingresados verificara cual es el mayor y lo retornara'''
    maximo = '?'

    if numero_uno >= numero_dos and numero_uno >= numero_tres:
        maximo = numero_uno
    elif numero_dos >= numero_tres:
        maximo = numero_dos
    else:
        maximo = numero_tres

    return maximo

# 6.Crear una función qué encuentre el mínimo entre tres números. Debe aceptar tres argumentos y retornar el número más chico.

def calcular_minimo(numero_uno : int, numero_dos : int , numero_tres : int) -> int:
    '''Segun los numeros ingresados verificara cual es el menor y lo retornara'''
    minimo = '?'

    if numero_uno <= numero_dos and numero_uno <= numero_tres:
        minimo = numero_uno
    elif numero_dos <= numero_tres:
        minimo = numero_dos
    else:
        minimo = numero_tres

    return minimo

# 7. Crear una función qué se encargue de dividir dos números, la misma debe recibir como parámetro dos números y retornar el resultado. Validar división por cero.

def calcular_division(numero_uno : float, numero_dos : float) -> float:

    resultado = numero_uno / numero_dos

    return resultado

# 8. Crear una función qué se encargue de multiplicar dos números, la misma debe recibir como parámetro dos números y retornar el resultado.

def calcular_multiplicacion(numero_uno : float, numero_dos : float) -> float:

    resultado = numero_uno * numero_dos

    return resultado

acumulador = 0
contador = 0
seguir = 'si'
while seguir == 'si':
    acumulador += float(input("elija un numero: "))
    contador += 1
    promedio = calcular_promedio(acumulador, contador)

    seguir = input('desea seguir introduciendo numeros? ')


print("--- EJERCICIO 1 ---")
print(f"el promedio de { acumulador } sobre { contador } es { promedio }")
print('el primer numero ingresado servira para calcular el area del rectangulo, para saber si es par o impar y si es primo, mientras que el tercero solo se tendra en cuenta para obtener maximo y minimo')

numero_a = float(input("---> elegi un numero: "))
numero_b = float(input("---> elegi otro numero: "))
numero_c = float(input("---> elegi otro numero mas: "))

area = calcular_area(numero_a, numero_b)
par = calcular_si_par_o_impar(numero_a)
primo = calcular_primo(numero_a)

print("--- EJERCICIO 2 ---")
print(f"el area del rectangulo es { area }")


print("--- EJERCICIO 3 ---")
if(par):
    print(f"el numero {numero_a} es par")
else:
    print(f"el numero {numero_a} es impar")


print("--- EJERCICIO 4 ---")
if(primo):
    print(f"{numero_a} es primo")
else:
    print(f"{numero_a} no es primo")


maximo = calcular_maximo(numero_a,numero_b,numero_c)
minimo = calcular_minimo(numero_a,numero_b,numero_c)


print("--- EJERCICIO 5 y 6 ---")
print(f"el maximo de los tres numeros es {maximo} y el minimo es {minimo}")


print("--- EJERCICIO 7 ---")
if numero_b == 0:
    print("no se puede dividir por 0")
else:
    division = calcular_division(numero_a,numero_b)
    print(f"la division entre { numero_a } y { numero_b } es {division}")

print("--- EJERCICIO 8 ---")
multiplicacion = calcular_multiplicacion(numero_a,numero_b)
print(f"la multiplicacion entre { numero_a } y { numero_b } es {multiplicacion}")




