# LEONARDO MIRABELLI
# EXAMEN

# UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
# franquicia que se insertará en el mercado argentino y en la cual invertirán.
# Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
# Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
# propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
# Se ingresa de cada encuestado:
# ● nombre
# ● edad (no menor a 18)
# ● está empleado (si-no)
# ● género (Masculino - Femenino - Otro)
# ● voto (APPLE, DUNKIN, IKEA)
# Se necesita saber:






seguir = "si"
voto_empleados_ikea = 0
voto_empleados_apple = 0
voto_otros_dunkin = 0
bandera_voto_femenino = 0
edad_femenino = 0
edad_masculino = 0
edad_otros = 0
contador_femenino = 0
contador_masculino = 0
contador_otros = 0


while seguir == "si":
    nombre = input("Ingrese el nombre del encuestado: ")

    edad = input(f"Ingrese la edad de {nombre}: ")
    edad = int(edad)
    while edad < 18:
        print("No puede ser menor a 18 años ")
        edad = input(f"Reingrese la edad de {nombre}: ")
        edad = int(edad)
    
    empleado = input("Tiene empleo? (si/no): ") 
    while empleado != "si" and empleado != "no":
        print("La respuesta es incorrecta, vuelva a ingresarla.")
        empleado = input("Tiene empleo? (si/no): ") 
    
    genero = input(f"Ingrese el genero de {nombre} (masculino/femenino/otro): ")
    while genero != "masculino" and genero != "femenino" and genero != "otro":
        print("La respuesta es incorrecta, vuelva a ingresarla.")
        genero = input(f"Reingrese el genero de {nombre} (masculino/femenino/otro): ")
    
    voto = input(f"Cual es el voto de {nombre} (apple/dunkin/ikea): ")
    while voto != "apple" and voto != "dunkin" and voto != "ikea":
        print("el voto no es valido, vuelva a registrarlo")
        voto = input(f"Cual es el voto de {nombre} (apple/dunkin/ikea): ")

    # 1. Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya
    # edad no supere los 36 años.
    
    if edad < 37:
        if empleado == "si":
            if voto == "ikea":
                voto_empleados_ikea += 1
            elif voto == "apple":
                voto_empleados_apple += 1

    # 2. Nombre y voto del encuestado de género Femenino con mayor edad.
    

    if genero == "femenino":
        edad_femenino += edad
        contador_femenino += 1
        if bandera_voto_femenino == 0:
            nombre_femenino_mayor_edad = nombre
            voto_femenino_mayor_edad = voto
            edad_femenino_mayor_edad = edad
            bandera_voto_femenino = 1
        elif edad > edad_femenino_mayor_edad:
            nombre_femenino_mayor_edad = nombre
            voto_femenino_mayor_edad = voto
            edad_femenino_mayor_edad = edad
    if genero == "masculino":
        edad_masculino += edad
        contador_masculino += 1
    else:
        edad_otros += edad
        contador_otros += 1
        if voto == "dunkin":
            voto_otros_dunkin += 1
    
    seguir = input("Seguir con la encuesta? (si/no): ")
    
# 3. Porcentaje de encuestados de género Otro que votaron por DUNKIN.
if contador_otros > 0:
    porcentaje_otros_dunkin = (voto_otros_dunkin / contador_otros) * 100
    promedio_edad_otros = edad_otros / contador_otros
else:
    porcentaje_otros_dunkin = "No hubo votos para dunkin del genero otros"
    promedio_edad_otros = "No hubo votos del genero otros"

# 4. Edad promedio de cada género.
if contador_femenino > 0:
    promedio_edad_femenino = edad_femenino / contador_femenino
    print(f"El voto femenino con mayor edad se llama {nombre_femenino_mayor_edad} y su voto fue para {voto_femenino_mayor_edad}")
else:
    promedio_edad_femenino = "No hubo votos del genero femenino"

if contador_masculino > 0:
    promedio_edad_masculino = edad_masculino / contador_masculino
else:
    promedio_edad_masculino = "No hubo votos del genero masculino"

# 5. Determinar cuál fue el género que tuvo menos encuestados.
if contador_femenino > contador_masculino and contador_otros > contador_masculino:
    menos_votos = "masculino"
elif contador_femenino > contador_otros:
    menos_votos = "otros"
else:
    menos_votos = "femenino"

total_voto_empleado_ikea_apple = voto_empleados_apple + voto_empleados_ikea

print(f"La cantidad de encuestados empleados que votaron por ikea o apple que no supera los 36 años es de {total_voto_empleado_ikea_apple} votos, siendo {voto_empleados_apple} para apple y {voto_empleados_ikea} para ikea")
print(f"El porcentaje de genero otros que voto a dunkin fue del: {porcentaje_otros_dunkin}%")
print(f"La edad promedio femenino es de {promedio_edad_femenino}, el masculino es de {promedio_edad_masculino} y el de genero otros {promedio_edad_otros}")
print(f"El genero con menor cantidad de votos es {menos_votos}")