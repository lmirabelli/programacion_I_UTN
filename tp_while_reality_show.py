#DATOS JUGADOR 1 -------------------------------------------------------------------------------------------------

jugador_1 = input("Nombre del Jugador 1 ")

edad_jugador_1 = int(input("Edad de "+jugador_1 + " : "))
while edad_jugador_1 < 26:
    print(jugador_1 + " debe que tener mas de 25 años")
    edad_jugador_1 = int(input("Edad de "+jugador_1 + " : "))

votos_jugador_1 = int(input("Votos de "+jugador_1 + " : "))
while votos_jugador_1 < 0:
    print(" Los votos de " + jugador_1 + " deben ser positivos")
    votos_jugador_1 = int(input("Votos de "+jugador_1 + " : "))
    
#DATOS JUGADOR 2 ------------------------------------------------------------------------------------------------

jugador_2 = input("Nombre del Jugador 2 ")

edad_jugador_2 = int(input("Edad de "+jugador_2 + " : "))
while edad_jugador_2 < 26:
    print(jugador_2 + " debe que tener mas de 25 años")
    edad_jugador_2 = int(input("Edad de "+jugador_2 + " : "))

votos_jugador_2 = int(input("Votos de "+jugador_2 + " : "))
while votos_jugador_2 < 0:
    print(" Los votos de " + jugador_2 + " deben ser positivos")
    votos_jugador_2 = int(input("Votos de "+jugador_2 + " : "))

#DATOS JUGADOR 3 -------------------------------------------------------------------------------------------------

jugador_3 = input("Nombre del Jugador 3 ")

edad_jugador_3 = int(input("Edad de "+jugador_3 + " : "))
while edad_jugador_3 < 26:
    print(jugador_3 + " debe que tener mas de 25 años")
    edad_jugador_3 = int(input("Edad de "+jugador_3 + " : "))

votos_jugador_3 = int(input("Votos de "+jugador_3 + " : "))
while votos_jugador_3 < 0:
    print(" Los votos de " + jugador_3 + " deben ser positivos")
    votos_jugador_3 = int(input("Votos de "+jugador_3 + " : "))


# COMPARACION DE LOS MAS VOTADOS ----------------------------------------------------------------------------------

if votos_jugador_1 > votos_jugador_2:
    if votos_jugador_1 > votos_jugador_3:
        mas_votado = jugador_1
    elif votos_jugador_1 < votos_jugador_3:
        mas_votado = jugador_3
    else:
        mas_votado = "Empataron entre" + jugador_1 +" y "+ jugador_3
elif votos_jugador_1 < votos_jugador_2:
    if votos_jugador_2 > votos_jugador_3:
        mas_votado = jugador_2
    elif votos_jugador_2 < votos_jugador_3:
        mas_votado = jugador_3
    else:
        mas_votado = "Empataron entre" + jugador_2 +" y "+ jugador_3
else:
    if votos_jugador_2 > votos_jugador_3:
        mas_votado = jugador_1 + " y " + jugador_2
    elif votos_jugador_2 < votos_jugador_3:
        mas_votado = jugador_3
    else:
        mas_votado = "Hubo un triple empate"



# COMPARACION DE LOS MENOS VOTADOS ---------------------------------------------------------------------------------

if votos_jugador_1 < votos_jugador_2:
    if votos_jugador_1 < votos_jugador_3:
        edad_menos_votado = edad_jugador_1
        menos_votado = jugador_1
    elif votos_jugador_1 > votos_jugador_3:
        edad_menos_votado = edad_jugador_3
        menos_votado = jugador_3
    else:
        edad_menos_votado = "Tienen " + edad_jugador_1 + " y " + edad_jugador_3 + " respectivamente" 
        menos_votado = "Empataron entre" + jugador_1 +" y "+ jugador_3
elif votos_jugador_1 > votos_jugador_2:
    if votos_jugador_2 < votos_jugador_3:
        edad_menos_votado = edad_jugador_2
        menos_votado = jugador_2
    elif votos_jugador_2 > votos_jugador_3:
        edad_menos_votado = edad_jugador_3
        menos_votado = jugador_3
    else:
        edad_menos_votado = "Tienen " + edad_jugador_2 + " y " + edad_jugador_3 + " respectivamente" 
        menos_votado = "Empataron entre" + jugador_2 +" y "+ jugador_3
else:
    if votos_jugador_2 < votos_jugador_3:
        edad_menos_votado = "Tienen " + edad_jugador_1 + " y " + edad_jugador_2 + " respectivamente" 
        menos_votado = jugador_1 + " y " + jugador_2
    elif votos_jugador_2 > votos_jugador_3:
        edad_menos_votado = edad_jugador_3
        menos_votado = jugador_3
    else:
        edad_menos_votado = "Tienen " + edad_jugador_1 + " ," + edad_jugador_2 + " y " + edad_jugador_3 + " respectivamente" 
        menos_votado = "Hubo un triple empate"

# IMPRESION EN CONSOLA ------------------------------------------------------------------------------------------------------

print("El/Los que mas voto recibio fue: " + mas_votado)
print("El/Los que menos voto recibio fue: " + menos_votado)
print("Su edad es : " + str(edad_menos_votado))

promedio_edad = float((edad_jugador_1 + edad_jugador_2 + edad_jugador_3) / 3)
total_votos = votos_jugador_1 + votos_jugador_2 + votos_jugador_3

print("El promedio de edad de los jugadores es: " + str(promedio_edad))
print("La cantidad de votos realizados: " + str(total_votos))

print("Link de la app funcionando: https://onlinegdb.com/kLSDH29MJ")