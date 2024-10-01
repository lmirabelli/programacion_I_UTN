


# 
# 
# 
# # Ejemplo [2,5,5,3,1] -> Retorna el índice [1,2]
# # 7. Escribir una función que reciba como parámetros una lista de enteros y muestre la posición del valor máximo encontrado. Reutilizar la función anterior.
# # Ejemplo [2,5,5,3,1] -> Muestra tanto el índice 1 como el 2 y sus valores
# # 8. Definir y cargar una lista con 10 sueldos enteros aleatorios (utilizar random), entre ARS 350.000 y ARS 1.250.000. Calcular el porcentaje de personas que superan el salario promedio de estos mismos.

# # 1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
# def promediando(lista):
#     suma_total = 0
#     for i in lista:
#         suma_total += i
    
#     promedio = suma_total / len(lista)

#     return promedio


# lista_numero = []
# cantidad_a_ingresar = int(input("Escriba la cantidad de numeros que va a ingresar: "))

# for i in range(cantidad_a_ingresar):
#     lista_numero.append(int(input("escriba un numero: ")))


# promedio = promediando(lista_numero)
# print(f"el promedio de los numeros ingresados es {promedio}")


# # 2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos. En caso de no haber números positivos validar división por cero

# def promedio_positivos(lista):
#     suma_total = 0
#     contador_positivos = 0

#     for i in lista:
#         if i > 0:
#             suma_total += i
#             contador_positivos += 1
    
#     if contador_positivos == 0:
#         return "No hay números positivos, no se puede calcular el promedio."
    
#     promedio = suma_total / contador_positivos
#     return promedio


# lista_numero = []
# cantidad_a_ingresar = int(input("Escriba la cantidad de números que va a ingresar: "))

# for i in range(cantidad_a_ingresar):
#     lista_numero.append(int(input("Escriba un número: ")))

# promedio = promedio_positivos(lista_numero)
# print(f"El promedio de los números positivos ingresados es: {promedio}")


# 3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro

def multiplicar_lista(lista):
    '''Multiplica los numeros de la lista'''
    producto_total = 1 
    
    for i in lista:
        producto_total *= i  
    
    return producto_total


lista_numero = []
cantidad_a_ingresar = int(input("Escriba la cantidad de números que va a ingresar: "))

for i in range(cantidad_a_ingresar):
    lista_numero.append(int(input("Escriba un número: ")))

producto = multiplicar_lista(lista_numero)
print(f"El producto de los números ingresados es: {producto}")

# 4.Escribir una función que reciba como parámetros una lista de enteros y retorne el índice del valor máximo encontrado (retornar un sólo índice, en caso de que haya más de un máximo el primero)

def buscar_maximo(lista: list) -> int:
    '''Busca el numero maximo de la lista recibida'''
    numero_maximo = ''
    indice = 0

    for i in range(len(lista)):

        if numero_maximo == '':
            numero_maximo = lista[i]

        elif numero_maximo < lista[i]:
            numero_maximo = lista[i]
            indice = i

    return indice

lista_numero = []
cantidad_a_ingresar = int(input("Escriba la cantidad de números que va a ingresar: "))

for i in range(cantidad_a_ingresar):
    lista_numero.append(int(input("Escriba un número: ")))


indice = buscar_maximo(lista_numero)
print(f"el indice del numero maximo es {indice}")


# 5. Escribir una función que reciba como parámetros una lista de enteros y muestre el índice del valor máximo encontrado (no se tienen en cuenta si hay más de un máximo) Reutilizar la función anterior.

lista_numero_dos = []
cantidad_a_ingresar = int(input("Escriba la cantidad de números que va a ingresar: "))

for i in range(cantidad_a_ingresar):
    lista_numero_dos.append(int(input("Escriba un número: ")))


numero_maximo_dos = buscar_maximo(lista_numero_dos)
print(f"el maximo número en la lista es {numero_maximo_dos}")

# Ejemplo [2,5,5,3,1] -> Imprime el índice  1 y su valor