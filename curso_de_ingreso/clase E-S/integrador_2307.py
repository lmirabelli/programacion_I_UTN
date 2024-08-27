
#LEONARDO MIRABELLI
#INTEGRADOR 23/07

"""

Se realiza un estudio de mercado para determinar cuál será la nueva franquicia 
que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes:
    STARBUCKS
    Zara
    MCDONALDS
    Bershka
    KFC

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, 
con el propósito de conocer cuáles son los gustos de los encuestados.

Datos a ingresar:
    Nombre del encuestado|  450
    Edad (no menor a 18)
    Género (Masculino - Femenino - Otro)
    Voto (STARBUCKS, MCDONALDS, ZARA, KFC)
    Situación Laboral (Empleado - Desempleado)



Consignas:
    a-Nombre y situación laboral de la persona con mayor edad que voto por Zara. xxx
    b-Nombre y voto de la persona de sexo Otro de entre 60 y 70 años. xxx
    c-Cantidad de encuestados desempleados que votaron por Starbucks, cuya edad esté entre 30 y 45 años inclusive. xxx
    d-Quien de todos los sexos fue el que mas votó por Zara.
"""

agregar_voto = "si"
votos_starbucks = 0
votos_zara = 0
votos_mcdonalds = 0
votos_kfc = 0
votos_bershka = 0
votos_desempleados_starbuck = 0
votos_zara_femenino = 0
votos_zara_masculino = 0
votos_zara_otros = 0
nombre_encuestado_especial = "nadie"

while agregar_voto == "si":
    #nombre y edad
    nombre_encuestado = input("Ingrese el nombre del encuestado: ")
    edad_encuestado = input("Ingrese la edad del encuestado: ")
    edad_encuestado = int(edad_encuestado)

    while edad_encuestado < 18:
        print("El encuestado de ser mayor a 18")
        edad_encuestado = input("Reingrese la edad del encuestado: ")
        edad_encuestado = int(edad_encuestado)
    
    #genero
    genero_encuestado = input("Ingrese el genero del encuestado (masculino/femenino/otro): ")
    while genero_encuestado != "masculino" and genero_encuestado != "femenino" and genero_encuestado != "otro":
        print(f"El genero {genero_encuestado} no es una opcion valida")
        genero_encuestado = input("Ingrese el genero del encuestado (masculino/femenino/otro): ")
    
    #sitacion laboral
    situacion_laboral_encuestado = input("Ingrese la situacion laboral del encuestado (empleado/no empleado): ")
    while situacion_laboral_encuestado != "empleado" and situacion_laboral_encuestado != "no empleado":
        print(f"{situacion_laboral_encuestado} no es una opcion valida")
        situacion_laboral_encuestado = input("Ingrese la situacion laboral del encuestado (empleado/no empleado): ")
    
    #voto
    voto_encuestado = input("Voto (starbucks, mcdonalds, zara, kfc, bershka): ")
    while voto_encuestado != "starbucks" and voto_encuestado != "mcdonalds" and voto_encuestado != "zara" and voto_encuestado != "kfc" and voto_encuestado != "bershka":
        print(f"{voto_encuestado} no es una opcion valida")    
        voto_encuestado = input("Voto (starbucks, mcdonalds, zara, kfc, bershka)")
    
    #contador de votos
    match voto_encuestado:
        case "mcdonald":
            votos_mcdonalds += 1
        case "starbuck":
            votos_starbucks += 1
        case "zara":
            votos_zara += 1
        case "kfc":
            votos_kfc += 1
        case "bershka":
            votos_bershka += 1

    #votos por zara
    if voto_encuestado == "zara":
        if genero_encuestado == "masculino":
            votos_zara_masculino += 1
        elif genero_encuestado == "femenino":
            votos_zara_femenino += 1
        elif genero_encuestado == "otro":
            votos_zara_otros += 1

        if votos_zara == 1:
            maxima_edad_voto_zara = edad_encuestado
            nombre_voto_zara = nombre_encuestado
            situacion_laboral_voto_zara = situacion_laboral_encuestado
        elif maxima_edad_voto_zara < edad_encuestado:
            maxima_edad_voto_zara = edad_encuestado
            nombre_voto_zara = nombre_encuestado
            situacion_laboral_voto_zara = situacion_laboral_encuestado
        
    #busqueda de voto especial
    if edad_encuestado > 59 and edad_encuestado < 70 and genero_encuestado == 'otro':
        nombre_encuestado_especial = nombre_encuestado

    #votos de desempleados por starbucks
    if voto_encuestado == "starbucks" and situacion_laboral_encuestado == "no empleado" and edad_encuestado > 29 and edad_encuestado < 45:
        votos_desempleados_starbuck += 1

    agregar_voto = input("Desea ingresar otro voto (si/no): ")


if votos_zara > 0:
    print(f"La persona mas grande que voto por zara es {nombre_voto_zara}, tiene {maxima_edad_voto_zara} y esta {situacion_laboral_voto_zara}")
else:
    print("Nadie voto por zara")


print(f"La persona de sexo otros entre 60 y 70 años es: {nombre_encuestado_especial}")


print(f"La cantidad de desempleados que votaron por starbucks es de: {votos_desempleados_starbuck}")

if votos_zara_masculino > votos_zara_femenino and votos_zara_masculino > votos_zara_otros:
    print("Los que mas votaron a zara son masculinos")
elif votos_zara_femenino > votos_zara_otros:
    print("Los que mas votaron a zara son femeninos")
else:  
    print("Los que mas votaron a zara son otros")