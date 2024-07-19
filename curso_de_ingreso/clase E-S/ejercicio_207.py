# E/S 7
# LEONARDO MIRABELLI

# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

altura_ingresada = input("ingrese su altura en centimetros: ")

altura_ingresada = int(altura_ingresada)

if altura_ingresada < 160:
    print("Posicion: Base")
elif altura_ingresada < 179:
    print("Posicion: Escolta")
elif altura_ingresada < 199:
    print("Posicion: Alero")
else:
    print("Posicion: Ala-Pívot o Pívot")


# ROJO 2
# LEONARDO MIRABELLI

# Al ejecutar el programa, se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:

import random

nota = random.randint(1, 10)  

if nota > 5:
    print(f"Promocion directa, la nota es {nota}")
elif(nota < 4):
    print(f"Desaprobado, la nota es {nota}")
else:
    print(f"Aprobado, la nota es {nota}")