import random
import os
I_NOMBRE = 0
I_APELLIDO = 1
I_DNI = 2
I_GENERO = 3
I_NOTA_FINAL = 4

def mostrar_matriz(matriz:list)->None:
    for fil in range(len(matriz)):#PARA LAS FILAS,largo de la lista es la cantidad de filas
        for colum in range(len(matriz[fil])):#PARA LAS COLUMNAS,va iterando cada valor en cada fila
            print(matriz[fil][colum], end=" ")
        print(" ")

def inicializar_matriz(cant_filas:int, cant_columnas:int,valor_inicial)->list:
    matriz = []
    for _ in range(cant_filas):
        fila =[valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz

matriz_alumnos = inicializar_matriz(3, 5, 0)

def cargar_nombre_apellido(mensaje, mensaje_error):
    nombre = input(mensaje)
    while len(mensaje) < 3:
        nombre = input(mensaje_error)
    return nombre

def cargar_entero(mensaje, mensaje_error, min, max):
    numero = int(input(mensaje))
    while numero < min or numero > max:
        numero = int(input(mensaje_error))
    return numero


def cargar_alumnos(matriz_alumnos):
    for i in range(len(matriz_alumnos)):
        nombre = cargar_nombre_apellido("Ingrese el nombre del alumno: ", "El nombre debe tener mas de 3 caracteres. Reingrese el nombre del alumno: ")
        
        apellido = cargar_nombre_apellido("Ingrese el apellido del alumno: ", "El apellido debe tener mas de 3 caracteres. Reingrese el nombre del alumno: ")

        dni = cargar_entero("Ingrese el dni del alumno: ", "El DNI debe tener entre 6 y 9 caracteres. Reingrese el dni del alumno: ", 11111111, 99999999)
        
        genero = input("Ingrese el genero del alumno: ")
        while genero != "M" and genero != "F" and genero != "NB":
            genero = input("Genero no valido. Reingrese el genero del alumno: ")
        
        nota_final = cargar_entero("Ingrese el nota del alumno: ", "La nota debe ser entre 1 y 10. Reingrese el nota del alumno: ", 1, 10)
        
        matriz_alumnos[i][I_NOMBRE] = nombre
        matriz_alumnos[i][I_APELLIDO] = apellido
        matriz_alumnos[i][I_DNI] = dni
        matriz_alumnos[i][I_GENERO] = genero
        matriz_alumnos[i][I_NOTA_FINAL] = nota_final

cargar_alumnos(matriz_alumnos)

def mostar_alumno(lista: list) -> list:
    for fil in range(len(lista)):
        print(f"nombre: {lista[fil][I_NOMBRE]}")
        print(f"apellido: {lista[fil][I_APELLIDO]}")
        print(f"dni: {lista[fil][I_DNI]}")
        print(f"genero: {lista[fil][I_GENERO]}")
        print(f"nota final: {lista[fil][I_NOTA_FINAL]}\n")

#mostar_alumno(matriz_alumnos)

#3.Mostrar Alumnos Promocionados:Mostrar sólo la información de los alumnos con nota mayor a 6 , en caso de no haber informar que no hay
#4.Mostrar Alumnos Aprobados:Mostrar sólo la información de los alumnos con nota 4,5 , en caso de no haber informar que no hay
#5.Mostrar Alumnos Desaprobados:Mostrar sólo la información de los alumnos con nota menor a 4 , en caso de no haber informar que no hay.
def mostar_alumno_notas(lista: list, min: int, max: int, mensaje: str, mensaje_error: str) -> list:
    print(mensaje)
    flag = False
    for fil in range(len(lista)):
        if lista[fil][I_NOTA_FINAL] >= min and lista[fil][I_NOTA_FINAL] <= max:
            print(f"nombre: {lista[fil][I_NOMBRE]}")
            print(f"apellido: {lista[fil][I_APELLIDO]}")
            print(f"dni: {lista[fil][I_DNI]}")
            print(f"genero: {lista[fil][I_GENERO]}")
            print(f"nota final: {lista[fil][I_NOTA_FINAL]}\n")
            flag = True
    
    if flag == False:
        print(mensaje_error)

#mostar_alumno_notas(matriz_alumnos, 6, 10, "Alumnos promocionados: ", "No hay alumnos promocionados")
#mostar_alumno_notas(matriz_alumnos, 4, 5, "Alumnos aprobados: ", "No hay alumnos aprobados.")
#mostar_alumno_notas(matriz_alumnos, 1, 3, "Alumnos desaprobados: ", "No hay alumnos desaprobados.")

#6.Buscar Alumno por DNI:Se debe ingresar el DNI de un alumno y buscar si se encuentra o no en el sistema, mostrar su información también.

def mostrar_alumno_dni(lista:list):
    dni = cargar_entero("Ingrese el dni del alumno: ", "El DNI debe tener entre 6 y 9 caracteres. Reingrese el dni del alumno: ", 11111111, 99999999)
    flag = False
    for fil in range(len(lista)):
        if lista[fil][I_DNI] == dni:
            print(f"nombre: {lista[fil][I_NOMBRE]}")
            print(f"apellido: {lista[fil][I_APELLIDO]}")
            print(f"dni: {lista[fil][I_DNI]}")
            print(f"genero: {lista[fil][I_GENERO]}")
            print(f"nota final: {lista[fil][I_NOTA_FINAL]}\n")
            flag = True
    if flag == False:
        print('No se encuentra en el sistema...')
    
#def mostrar_dato(lista):
# mostrar_alumno_dni(matriz_alumnos)
    
#7.La cantidad de alumnos promocionados, aprobados y desaprobados

def contar_alumnos(lista: list, min: int, max: int) ->list:
    '''
    
    '''
    contador_alumnos = 0
    for fil in range(len(lista)):
        if lista[fil][I_NOTA_FINAL] >= min and lista[fil][I_NOTA_FINAL] <= max:
            contador_alumnos += 1

    return contador_alumnos


print(f"La cantidad de alumnos promocionados: {contar_alumnos(matriz_alumnos, 6, 10)}")
print(f"La cantidad de alumnos aprobados: {contar_alumnos(matriz_alumnos, 4, 5)}")
print(f"La cantidad de alumnos desaprobados: {contar_alumnos(matriz_alumnos, 1, 3)}")
