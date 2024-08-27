sin_vacuna_edad_4_12_problemas = 0
loros_digestivos = 0
gatos_digestivos = 0
perros_digestivos = 0
edad_mascota_mas_vieja = 0
tipo_mascota_mas_vieja = ""
bandera_mascota_mas_vieja = 0
mascotas_vacunadas = 0
mascotas_no_vacunadas = 0
cantidad_gatos = 0
total_edad_gatos = 0

for i in range(20):
    edad =  input("coloque la edad de la mascota: ")
    edad = int(edad)
    tipo = input("tipo de mascota: gato/perro/loro")

    while tipo != "gato" and tipo != "perro" and tipo != 'loro':
        print(f"{tipo} no es una opcion valida")
        tipo = input("tipo de mascota: gato/perro/loro")

    peso = input("Coloque el peso de la mascota: ")
    peso = int(peso)
    while peso < 1:
        print(f"{peso} no es valido")
        peso = input("Coloque el peso de la mascota: ")
        peso = int(peso)
    
    diagnostico = input("que problema tiene la mascota: problemas digestivos/parasitos/infeccion")

    while diagnostico != "problemas digestivos" and diagnostico != "parasitos" and diagnostico != "infeccion":
        print("El diagnostico es incorrecto")
        diagnostico = input("que problema tiene la mascota: problemas digestivos/parasitos/infeccion")
    
    vacuna = input("vacuna antirrabica? si/no")

    while vacuna != "si" and vacuna != "no":
        print(f"{vacuna} no es una respuesta")
        vacuna = input("vacuna antirrabica? si/no")
    

    if diagnostico == "infeccion" or diagnostico == "parasitos":
        if edad > 3 and edad < 13 and vacuna == 'no':
                sin_vacuna_edad_4_12_problemas += 1
    elif diagnostico == 'problemas digestivos':
        if tipo == "loro":
            loros_digestivos += 1
        elif tipo == "gato":
            gatos_digestivos += 1
        else:
            perros_digestivos += 1
    
    
    if vacuna == 'si':
        if bandera_mascota_mas_vieja == 0:
            edad_mascota_mas_vieja = edad
            tipo_mascota_mas_vieja = tipo
            bandera_mascota_mas_vieja = 1
        elif edad > edad_mascota_mas_vieja:
            edad_mascota_mas_vieja = edad
        tipo_mascota_mas_vieja = tipo
        mascotas_vacunadas += 1
    else:
        mascotas_no_vacunadas += 1
    
    if tipo == "gato":
        cantidad_gatos += 1
        total_edad_gatos += edad

print(f"la cantidad de mascotas sin vacuna antirrábica, cuya edad está entre los 4 y 12 años, que se presentaron por infección o parásitos: {sin_vacuna_edad_4_12_problemas} mascotas")

if loros_digestivos > gatos_digestivos and loros_digestivos > perros_digestivos:
    mascota_con_mas_problemas_digestivos = "loros"
elif gatos_digestivos > perros_digestivos:
    mascota_con_mas_problemas_digestivos = "gatos"
else:
    mascota_con_mas_problemas_digestivos = "perros"
    
print(f"el tipo de mascota más ingresada con problemas digestivos son los {mascota_con_mas_problemas_digestivos}")
print(f"un {tipo_mascota_mas_vieja} de {edad_mascota_mas_vieja} años es la mascota más vieja con vacuna antirrábica.")

cantidad_de_mascotas = mascotas_no_vacunadas + mascotas_vacunadas
porcentaje_sin_vacunas = mascotas_no_vacunadas / cantidad_de_mascotas
porcentajes_con_vacunas = mascotas_vacunadas / cantidad_de_mascotas

print(f"el porcentaje de mascotas vacunadas es de {porcentajes_con_vacunas}% mientras que las no vacunadas es de {porcentaje_sin_vacunas}%")

promedio_edad_gatos = total_edad_gatos / cantidad_gatos

print(f"el promedio de edad de los gatos atendidos es de {promedio_edad_gatos}")

