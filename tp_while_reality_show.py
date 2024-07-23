
#TP Reality Show
#LEONARDO MIRABELLI

contador_de_jugadores = 0
acumulador_edad = 0 
total_votos = 0

while contador_de_jugadores < 3:
    jugador = input('Ingresar nombre del jugador: ')
    edad_del_jugador = input(f'Ingresar la edad de {jugador}: ')
    edad_del_jugador = int(edad_del_jugador)

    while edad_del_jugador < 25:
        print('No puede ser menor a 25 años')
        edad_del_jugador = input(f'Ingresar la edad de {jugador}: ')
        edad_del_jugador = int(edad_del_jugador)
    
    acumulador_edad += edad_del_jugador

    votos_del_jugador = input(f"Ingrese la cantidad de votos de {jugador}: ")
    votos_del_jugador = int(votos_del_jugador)
    
    while votos_del_jugador < 0:
        print("No puede tener votos negativos")
        votos_del_jugador = input(f"Ingrese la cantidad de votos de {jugador}: ")
        votos_del_jugador = int(votos_del_jugador)
    
    total_votos += votos_del_jugador
    
    if contador_de_jugadores == 0:
        mas_votado = votos_del_jugador
        menos_votado = votos_del_jugador
        jugador_con_mas_votos = jugador
        jugador_con_menos_votos = jugador
        edad_con_menos_votos = edad_del_jugador
    elif votos_del_jugador > mas_votado:
        jugador_con_mas_votos = jugador
        jugador_con_menos_votos = jugador
    elif votos_del_jugador < menos_votado:
        jugador_con_menos_votos = jugador
        edad_con_menos_votos = edad_del_jugador
    
    print(total_votos)
    contador_de_jugadores += 1

promedio_edad = float(acumulador_edad / contador_de_jugadores)

print(f"El jugador mas votado es {jugador_con_mas_votos}")
print(f"El jugador con menos votos es {jugador_con_menos_votos} y su edad es {edad_con_menos_votos}")
print(f"El pormedio de edad es de {promedio_edad}")
print(f"La cantidad total de votos fue de {total_votos}")





# #DATOS JUGADOR 1 -------------------------------------------------------------------------------------------------

# jugador_uno = input("Nombre del Jugador 1 ")

# edad_jugador_uno = int(input("Edad de "+jugador_uno + " : "))
# while edad_jugador_uno < 26:
#     print(jugador_uno + " debe que tener mas de 25 años")
#     edad_jugador_uno = int(input("Edad de "+jugador_uno + " : "))

# votos_jugador_uno = int(input("Votos de "+jugador_uno + " : "))
# while votos_jugador_uno < 0:
#     print(" Los votos de " + jugador_uno + " deben ser positivos")
#     votos_jugador_uno = int(input("Votos de "+jugador_uno + " : "))
    
# #DATOS JUGADOR 2 ------------------------------------------------------------------------------------------------

# jugador_dos = input("Nombre del Jugador 2 ")

# edad_jugador_dos = int(input("Edad de "+jugador_dos + " : "))
# while edad_jugador_dos < 26:
#     print(jugador_dos + " debe que tener mas de 25 años")
#     edad_jugador_dos = int(input("Edad de "+jugador_dos + " : "))

# votos_jugador_dos = int(input("Votos de "+jugador_dos + " : "))
# while votos_jugador_dos < 0:
#     print(" Los votos de " + jugador_dos + " deben ser positivos")
#     votos_jugador_dos = int(input("Votos de "+jugador_dos + " : "))

# #DATOS JUGADOR 3 -------------------------------------------------------------------------------------------------

# jugador_tres = input("Nombre del Jugador 3 ")

# edad_jugador_tres = int(input("Edad de "+jugador_tres + " : "))
# while edad_jugador_tres < 26:
#     print(jugador_tres + " debe que tener mas de 25 años")
#     edad_jugador_tres = int(input("Edad de "+jugador_tres + " : "))

# votos_jugador_tres = int(input("Votos de "+jugador_tres + " : "))
# while votos_jugador_tres < 0:
#     print(" Los votos de " + jugador_tres + " deben ser positivos")
#     votos_jugador_tres = int(input("Votos de "+jugador_tres + " : "))


# # COMPARACION DE LOS MAS VOTADOS ----------------------------------------------------------------------------------

# if votos_jugador_uno > votos_jugador_dos:
#     if votos_jugador_uno > votos_jugador_tres:
#         mas_votado = jugador_uno
#     elif votos_jugador_uno < votos_jugador_tres:
#         mas_votado = jugador_tres
#     else:
#         mas_votado = "Empataron entre" + jugador_uno +" y "+ jugador_tres
# elif votos_jugador_uno < votos_jugador_dos:
#     if votos_jugador_dos > votos_jugador_tres:
#         mas_votado = jugador_dos
#     elif votos_jugador_dos < votos_jugador_tres:
#         mas_votado = jugador_tres
#     else:
#         mas_votado = "Empataron entre" + jugador_dos +" y "+ jugador_tres
# else:
#     if votos_jugador_dos > votos_jugador_tres:
#         mas_votado = jugador_uno + " y " + jugador_dos
#     elif votos_jugador_dos < votos_jugador_tres:
#         mas_votado = jugador_tres
#     else:
#         mas_votado = "Hubo un triple empate"



# # COMPARACION DE LOS MENOS VOTADOS ---------------------------------------------------------------------------------

# if votos_jugador_uno < votos_jugador_dos:
#     if votos_jugador_uno < votos_jugador_tres:
#         edad_menos_votado = edad_jugador_uno
#         menos_votado = jugador_uno
#     elif votos_jugador_uno > votos_jugador_tres:
#         edad_menos_votado = edad_jugador_tres
#         menos_votado = jugador_tres
#     else:
#         edad_menos_votado = "Tienen " + edad_jugador_uno + " y " + edad_jugador_tres + " respectivamente" 
#         menos_votado = "Empataron entre" + jugador_uno +" y "+ jugador_tres
# elif votos_jugador_uno > votos_jugador_dos:
#     if votos_jugador_dos < votos_jugador_tres:
#         edad_menos_votado = edad_jugador_dos
#         menos_votado = jugador_dos
#     elif votos_jugador_dos > votos_jugador_tres:
#         edad_menos_votado = edad_jugador_tres
#         menos_votado = jugador_tres
#     else:
#         edad_menos_votado = "Tienen " + edad_jugador_dos + " y " + edad_jugador_tres + " respectivamente" 
#         menos_votado = "Empataron entre" + jugador_dos +" y "+ jugador_tres
# else:
#     if votos_jugador_dos < votos_jugador_tres:
#         edad_menos_votado = "Tienen " + edad_jugador_uno + " y " + edad_jugador_dos + " respectivamente" 
#         menos_votado = jugador_uno + " y " + jugador_dos
#     elif votos_jugador_dos > votos_jugador_tres:
#         edad_menos_votado = edad_jugador_tres
#         menos_votado = jugador_tres
#     else:
#         edad_menos_votado = "Tienen " + edad_jugador_uno + " ," + edad_jugador_dos + " y " + edad_jugador_tres + " respectivamente" 
#         menos_votado = "Hubo un triple empate"

# # IMPRESION EN CONSOLA ------------------------------------------------------------------------------------------------------

# print("El/Los que mas voto recibio fue: " + mas_votado)
# print("El/Los que menos voto recibio fue: " + menos_votado)
# print("Su edad es : " + str(edad_menos_votado))

# promedio_edad = float((edad_jugador_uno + edad_jugador_dos + edad_jugador_tres) / 3)
# total_votos = votos_jugador_uno + votos_jugador_dos + votos_jugador_tres

# print("El promedio de edad de los jugadores es: " + str(promedio_edad))
# print("La cantidad de votos realizados: " + str(total_votos))

# print("Link de la app funcionando: https://onlinegdb.com/kLSDH29MJ")