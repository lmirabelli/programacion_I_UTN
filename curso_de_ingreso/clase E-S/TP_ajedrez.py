# AJEDREZ
# LEONARDO MIRABELLI

cantidad_participantes = 0
jugador_mas_ganadas = ''
jugador_menos_ganadas = ''
mas_ganadas = 0
menos_ganadas = 0
edad_menos_ganadas = 0
suma_edad = 0
suma_partidas_ganadas = 0

while True:
    cantidad_participantes += 1
    nombre = input("Ingrese el nombre del participante: ")

    edad = 0
    while edad < 10:
        edad = input(f"Ingrese la edad del participante {nombre}: ")
        edad = int(edad)
        if edad < 10:
            print("Edad invalida")

    while True:
        partidas_ganadas = input(f"Ingrese la cantidad de partidas ganadas de {nombre}: ")
        partidas_ganadas = int(partidas_ganadas)
        if partidas_ganadas >= 0:
            break
    
    if cantidad_participantes == 1:
        mas_ganadas = partidas_ganadas
        jugador_mas_ganadas = nombre
        jugador_menos_ganadas = nombre
        menos_ganadas = partidas_ganadas
        edad_menos_ganadas = edad
    
    else:
        if mas_ganadas < partidas_ganadas:
            mas_ganadas = partidas_ganadas
            jugador_mas_ganadas = nombre

        elif menos_ganadas > partidas_ganadas:
            jugador_menos_ganadas = nombre
            menos_ganadas = partidas_ganadas
            edad_menos_ganadas = edad

    suma_edad += edad
    suma_partidas_ganadas += partidas_ganadas

    promedio_edad = suma_edad / cantidad_participantes


    seguir = input("Desea agregar otro participante: ")
    if seguir == 'no':
        break



print(f"El jugador con mas partidas ganadas es {jugador_mas_ganadas}.")
print(f"El jugador con menos partidas ganadas es {jugador_menos_ganadas} y tiene {edad_menos_ganadas} años")
print(f"El promedio de edad de los participantes es de {promedio_edad}")
print(f"La cantidad de partidas ganadas fueron {suma_partidas_ganadas}")
