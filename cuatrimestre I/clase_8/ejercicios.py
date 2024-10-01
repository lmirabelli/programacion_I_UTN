import random

# 1. Escribir una función que reciba como parámetro una lista de str y cuente la cantidad de elementos con más de cinco caracteres.
# Para contar los caracteres de un string también se usa la función len

lista_general = ['leonardo','diego','pablo','lalo','jose','luis','saracatuga']

def calcular_lista(lista: list) -> int:
    '''Calcula el largo de cada elemento y cuenta aquellos que tienen mas de 5 caracteres'''
    nombres_cinco_caracteres = 0
    for nombre in lista:
        if len(nombre) > 5:
            nombres_cinco_caracteres += 1
    
    return nombres_cinco_caracteres

print("EJERCICIO NUMERO 1")
nombres_cinco_caracteres = calcular_lista(lista_general)
print(nombres_cinco_caracteres)

# 2. Escribir una función que reciba como parámetro una lista de str y retorne una nueva lista con los elementos de más de cinco caracteres.

def listar_nombres(lista: list) -> list:
    '''Calcula el largo de cada elemento y agrega a una nueva lista aquellos que tienen mas de 5 caracteres'''
    lista_nombres_cinco_caracteres = []
    for nombre in lista:
        if len(nombre) > 5:
            lista_nombres_cinco_caracteres.append(nombre)
    
    return lista_nombres_cinco_caracteres

print("EJERCICIO NUMERO 2")
lista_cinco_caracteres = listar_nombres(lista_general)
print("Lista de nombres con mas de 5 caracteres:")
for nombre in lista_cinco_caracteres:
    print(nombre)





# 3. Escribir una función que me permita ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Retornar una lista con el/los nombres de la personas con el nombre más corto (tener en cuenta más de un mínimo)

def ingresar_nombres() -> list:
    '''Ingresa por teclado 5 nombres'''
    lista_de_nombres_ingresados = []
    for i in range(5):
        nombre_ingresado = input(f'Ingrese el nombre ({i + 1}/5): ')
        while len(nombre_ingresado) == 0:
            nombre_ingresado = input(f'El nombre no puede estar vacio, reingrese el nombre ({i}/5): ')
        
        lista_de_nombres_ingresados.append(nombre_ingresado)
    
    return lista_de_nombres_ingresados

def calcular_largo_nombres(lista_nombres: list) -> list:
    ''' Calcula la cantidad de caracteres de la lista pasada y devuelve una lista con el/los nombres con menos caracteres'''
    nombres_cortos = []
    for i in range(len(lista_nombres)):
        if i == 0:
            nombres_cortos.append(lista_nombres[i])
            caracteres_menor_nombre = len(lista_nombres[i])

        elif len(lista_nombres[i]) < caracteres_menor_nombre:
            nombres_cortos = [lista_nombres[i]]
            caracteres_menor_nombre = len(lista_nombres[i])

        elif len(lista_nombres[i]) == caracteres_menor_nombre:
            nombres_cortos.append(lista_nombres[i])
    
    return nombres_cortos

print("EJERCICIO NUMERO 3")
lista_nombres_ingresados = ingresar_nombres()
nombres_cortos = calcular_largo_nombres(lista_nombres_ingresados)

for nombre in nombres_cortos:
    print(nombre)






# 4. Escribir una función que reciba una lista de apellidos comunes como esta:
# Ingresar 10 apellidos y guardarlos en otra lista. Contar cuantas veces se repiten los apellidos comunes.
# apellidos_comunes = ["lopez", "gomez", "fernandez", "perez", "martinez" ]

def ingresar_apellidos() -> list:
    '''Ingresa por teclado 10 apellidos'''
    lista_apellidos_ingresados = []

    for i in range(10):
        apellido_ingresado = input(f'Ingrese el apellido ({i + 1}/10): ')
        while len(apellido_ingresado) == 0:
            apellido_ingresado = input(f'El apellido no puede estar vacio, reingrese el apellido ({i}/10): ')
        
        lista_apellidos_ingresados.append(apellido_ingresado)

    return lista_apellidos_ingresados


def calcular_apellidos_comunes(lista: list) -> list:
    '''Calcula la cantidad de repeticiones de apellidos'''
    lista_repeticiones = []
    lista_apellidos_comunes = []
    for i in range(len(lista)):
        bandera_apellido = 0
        for j in range(len(lista_apellidos_comunes)):
            if lista_apellidos_comunes[j] == lista[i]:
                lista_repeticiones[j] += 1
                bandera_apellido = 1
                break
                
        if bandera_apellido == 0:
            lista_apellidos_comunes.append(lista[i])
            lista_repeticiones.append(1)
    
    for i in range(len(lista_apellidos_comunes)):
        print(f"{lista_apellidos_comunes[i]} se repitio {lista_repeticiones[i]}")


print("EJERCICIO NUMERO 4")
lista_apellidos = ingresar_apellidos()
calcular_apellidos_comunes(lista_apellidos)


# 5.Escribir un programa que me permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años). Utilizar listas paralelas.
# (Hacer dos funciones, una para la carga de productos y otra para mostrarlos)

lista_nombres = []
lista_edades = []
def cargar_listas(cantidad,objeto,valor,lista_objeto,lista_valor) -> list:
    '''Ingresa los nombres y las edades solicitadas'''
    for i in range(cantidad):
        nombre = input(f"Escriba el {objeto} ({i + 1}/{cantidad}): ")
        valor_del_objeto = int(input(f"Escriba {valor}: "))

        lista_objeto.append(nombre)
        lista_valor.append(valor_del_objeto)

def filtrar_edad(nombres:list, edades:list) -> list:
    '''Calcaula quienes son mayores de edad'''

    mayores = []
    for i in range(len(nombres)):
        if edades[i] >= 18:
            mayores.append(nombres[i])
    
    return mayores

def imprimir_lista(objetos):
    for obj in objetos:
        print(obj)

print("EJERCICIO NUMERO 5")
cargar_listas(5,'nombre','la edad',lista_nombres,lista_edades)
lista_mayores = filtrar_edad(lista_nombres,lista_edades)
imprimir_lista(lista_mayores)

# 6. Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Mostrar la cantidad de productos que tienen un precio mayor al primer producto ingresado.
# (Hacer dos funciones, una para la carga de productos y otra para mostrarlos)

def comparar_precios(productos : list ,precios : list ):

    productos_mas_caro_primer_producto = []
    for i in range(len(precios)):
        if i == 0:
            precio_primer_producto = precios[i]
        elif precios[i] > precio_primer_producto:
            productos_mas_caro_primer_producto.append(productos[i])
        
    return productos_mas_caro_primer_producto


lista_productos = []
lista_precios = []

print("EJERCICIO NUMERO 6")
cargar_listas(5,'producto','el precio',lista_productos,lista_precios)
lista_productos_filtrada = comparar_precios(lista_productos,lista_precios)
imprimir_lista(lista_productos_filtrada)


# 7. La utn fra necesita un sistema saber la nota promedio más alta entre 5 alumnos de la Materia Programación I. 
# Para eso debemos guardar.

# Nombre (Ingresa usuario)
# Apellido (Ingresa usuario)
# Legajo (Ingresa usuario entre 10000 y 99999)
# Nota primer parcial (Número aleatorio entre 1 y 10)
# Nota segundo parcial (Número aleatorio entre 1 y 10)

# Aparte de saber cuál fue esa nota debemos mostrar cuál fue el alumno, en caso de haber más de un alumno con la misma nota promedio mostrar a los dos.

import random

lista_alumnos = []
lista_legajos = []
lista_notas = []

def cargar_datos(cantidad) -> list:

    promedio_mas_alto = 0
    lista_promedio_alto = []

    for i in range(cantidad):

        nombre = input(f"Ingresa el nombre del alumno ({i+1}/{cantidad}): ")
        apellido = input("Ingresa el apellido del alumno: ")
        legajo = random.randint(10000, 99999)
        parcial_uno = random.randint(1, 10)
        parcial_dos = random.randint(1, 10)
        promedio = (parcial_uno + parcial_dos) / 2
        print(f"{apellido}, {nombre}: P1({parcial_uno}) - P2({parcial_dos}) - Promedio({promedio})")

        if promedio > promedio_mas_alto:
            promedio_mas_alto = promedio
            lista_promedio_alto = [legajo]
            print(f"NUEVO MEJOR PROMEDIO {legajo}")
        elif promedio == promedio_mas_alto:
            lista_promedio_alto.append(legajo)

        lista_alumnos.append(f"{apellido}, {nombre}")
        lista_legajos.append(legajo)
        lista_notas.append([parcial_uno, parcial_dos, promedio])


    return lista_alumnos, lista_legajos, lista_notas, lista_promedio_alto

def buscar_promedios(alumnos: list, legajos: list, notas: list, promedio_alto: list):
    for legajo in promedio_alto:
        for j in range(len(legajos)):
            if legajo == legajos[j]: 
                print(f"Alumno con mejor promedio: {alumnos[j]}, Legajo: {legajo}, Promedio: {notas[j][2]}")


lista_alumnos, lista_legajos, lista_notas, lista_promedio_alto = cargar_datos(5)


print(lista_alumnos)
buscar_promedios(lista_alumnos, lista_legajos, lista_notas, lista_promedio_alto)
