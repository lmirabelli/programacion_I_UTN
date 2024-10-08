

lista_1 = [4,7,1,16,104,81,12,45]


# 1.Realizar una función que ordene una lista de enteros de forma ascendente (menor a mayor) , la misma debería devolver False en caso de que se ya se encuentre ordenada. True en caso contrario

def ordenar_menor_mayor(lista: list) -> bool:
    '''Ordena la lista ingresada por parametro de menor a mayor'''
    validacion_lista_acomodada = False

    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                validacion_lista_acomodada = True
    
    return validacion_lista_acomodada

menor_mayor_1 = ordenar_menor_mayor(lista_1)
menor_mayor_2 = ordenar_menor_mayor(lista_1)
print(menor_mayor_1)
print(menor_mayor_2)

# 2.Realizar una función que ordene una lista de enteros de forma descendente (mayor a menor) , la misma debería devolver False en caso de que se ya se encuentre ordenada. True en caso contrario

lista_2 = [4,7,1,16,104,81,12,45]

def ordenar_mayor_menor(lista: list) -> bool:
    '''Ordena la lista ingresada por parametro de mayor a menor'''
    validacion_lista_acomodada = False

    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                validacion_lista_acomodada = True
    
    return validacion_lista_acomodada

mayor_menor_1 = ordenar_mayor_menor(lista_2)
mayor_menor_2 = ordenar_mayor_menor(lista_2)
print(mayor_menor_1)
print(mayor_menor_2)

# 3.Realizar una función que ordene una lista de enteros en orden ascendente o descendente dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de intercambios que se realizaron.

lista_3 = [4,7,1,16,104,81,12,45]

def ordenar(lista: list, opcion: int) -> int:
    '''Ordena la lista ingresada de forma seleccionada segun el parametro ingresado (opcion)'''

    numero_de_cambios = 0
    if(opcion == 1):
        for i in range(len(lista) - 1):
            for j in range(i+1, len(lista)):
                if lista[i] > lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                    numero_de_cambios += 1
                    print(f"{lista[i]} -> {lista[j]}")
    elif(opcion == 2):
        for i in range(len(lista) - 1):
            for j in range(i+1, len(lista)):
                if lista[i] < lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                    numero_de_cambios += 1
                    print(f"{lista[i]} -> {lista[j]}")

    return numero_de_cambios

opcion = int(input("Ingrese la opcion 1 para ordenar de menor a mayor y la opcion 2 de mayor a menor: "))

while opcion != 1 and opcion != 2:
    print('La opcion ingresada es no valida')
    opcion = int(input("Ingrese la opcion 1 para ordenar de menor a mayor y la opcion 2 de mayor a menor: "))

ejercicio_3 = ordenar(lista_3,opcion)
print(f"la lista tuvo {ejercicio_3} intercambios")

# 4.Realizar una función que ordene una lista de nombres de la alfabéticamente (A-Z) o viceversa (Z-A) dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de cambios que se realizaron.

lista_nombres = ["gaston", "leonardo", "pablo", "carlos", "marcelo", "rodrigo", "nahuel", "hernan", "imhotep"]

opcion_4 = int(input("Ingrese la opcion 1 para [A-Z] y la opcion 2 [Z-A]: "))
while opcion_4 != 1 and opcion_4 != 2:
        print('La opcion ingresada es no valida')
        opcion_4 = int(input("Ingrese la opcion 1 para [A-Z] y la opcion 2 [Z-A]: "))

ordenar_nombres = ordenar(lista_nombres,opcion_4)
print(f"la lista tuvo {ordenar_nombres} intercambios")
print(lista_nombres)

# 5. Similar a la función anterior, se debe realizar otra que ordene una lista de nombres por su largo, de manera ascendente o descendente, la función debe retornar la cantidad de cambios que se realizaron.

opcion_5 = int(input("Ingrese la opcion 1 para [A-Z] y la opcion 2 [Z-A]: "))
while opcion_5 != 1 and opcion_5 != 2:
        print('La opcion ingresada es no valida')
        opcion_5 = int(input("Ingrese la opcion 1 para [A-Z] y la opcion 2 [Z-A]: "))


def ordenar_alfabeticamente(lista: list, opcion: int) -> int:
    '''Ordena la lista ingresada de forma seleccionada segun el parametro ingresado (opcion)'''

    numero_de_cambios = 0
    if(opcion == 1):
        for i in range(len(lista) - 1):
            for j in range(i+1, len(lista)):
                if len(lista[i]) > len(lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                    numero_de_cambios += 1
                    print(f"{lista[i]} -> {lista[j]}")
    elif(opcion == 2):
        for i in range(len(lista) - 1):
            for j in range(i+1, len(lista)):
                if len(lista[i]) < len(lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                    numero_de_cambios += 1
                    print(f"{lista[i]} -> {lista[j]}")

    return numero_de_cambios

lista_largo_nombres = ordenar_alfabeticamente(lista_nombres, opcion_5)
print(f"la lista tuvo {lista_largo_nombres} intercambios")
print(lista_nombres)






# 6. Crear una función para ordenar por apellido una matriz que tenga dos columnas (nombre-apellido) de la A-Z o viceversa dependiendo de un parámetro que se le envíe.


def ordenar_matrices(lista: list,ordenamiento: int, opcion: int) -> int:
    '''Ordena la lista ingresada de forma seleccionada segun el parametro ingresado (opcion)'''

    if(opcion == 1):
        for i in range(len(lista) - 1):
            for j in range(i+1, len(lista)):
                if lista[i][ordenamiento] > lista[j][ordenamiento]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                    print(f"{lista[i][ordenamiento]} -> {lista[j][ordenamiento]}")
    elif(opcion == 2):
        for i in range(len(lista) - 1):
            for j in range(i+1, len(lista)):
                if lista[i][ordenamiento] < lista[j][ordenamiento]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                    print(f"{lista[i][ordenamiento]} -> {lista[j][ordenamiento]}")


lista_jugadores = [["leonardo","mirabelli",8,0,0],["lionel","messi",16,12,8],["andriy","shevchenko",15,8,4],["nicolas","malvacio",12,3,4],["fernando","enrique",14,8,12],["gabriel","batistuta",22,14,3]]

opcion_6 = int(input("(6)Ingrese la opcion 1 para [A-Z] y la opcion 2 [Z-A]: "))
while opcion_6 != 1 and opcion_6 != 2:
        print('La opcion ingresada es no valida')
        opcion_6 = int(input("Ingrese la opcion 1 para [A-Z] y la opcion 2 [Z-A]: "))

ordenar_matrices(lista_jugadores,1,opcion_6)

print(lista_jugadores)

# 7. Crear una función para ordenar por nombre una matriz que tenga dos columnas (nombre-apellido) de la A-Z o viceversa dependiendo de un parámetro que se le envíe.

opcion_7 = int(input("(7)Ingrese la opcion 1 para [A-Z] y la opcion 2 [Z-A]: "))
while opcion_7 != 1 and opcion_7 != 2:
        print('La opcion ingresada es no valida')
        opcion_7 = int(input("Ingrese la opcion 1 para [A-Z] y la opcion 2 [Z-A]: "))

ordenar_matrices(lista_jugadores,0,opcion_7)

print(lista_jugadores)

# 8. Vamos a guardar la información de un jugador de fútbol en una matriz con las siguientes columnas (nombre,apellido, partidos,goles,asistencias) 
# debemos:

# 1-Mostrar tabla de goleadores
# 2-Mostrar tabla de asistencias
# 3-Los 5 jugadores con más partidos.
# 4-Mostrar top 3 jugadores con más goles 
# 5-Mostrar top 3 jugadores con menos asistencias
ordenar_matrices(lista_jugadores,3,2)

print(lista_jugadores)