# VALIDACIONES
# LEONARDO MIRABELLI

apellido = input("Ingrese el apellido: ")

edad = 0
while edad < 18 or edad > 90:
    edad = input("ingrese la edad: ")
    edad = int(edad)
    if edad < 18 or edad > 90:
        print("Edad fuera de rango")



while True:
    estado_civil = input("Ingrese estado civil (“Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a” ): ")
    if(estado_civil == 'Soltero' or estado_civil == 'Soltera'):
        break
    elif(estado_civil == 'Casado' or estado_civil == 'Casada'):
        break
    elif(estado_civil == 'Divorciado' or estado_civil == 'Divorciada'):
        break
    elif(estado_civil == 'viiudo' or estado_civil == 'viiuda'):
        break
    else:
        print(f"{estado_civil} no es respuesta valida")

while True:
    legajo = input("Ingrese el numero de legajo: ")
    legajo = int(legajo)
    if legajo > 0 and legajo < 10000:
        break
    else:
        print("Legajo invalido")


print(f"{apellido} tiene {edad} años, esta {estado_civil} y su numero de legajo es el {legajo}")