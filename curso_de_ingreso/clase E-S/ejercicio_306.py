# E/S 6
# LEONARDO MIRABELLI

# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
# Calcular la suma de los números ingresados y el promedio de los mismos.


seguir = "si"
contador = 0
acumulador = 0
positivos = 0
negativos = 0

while seguir == "si":
    numero_elegido = input("ingrese un numero: ")
    numero_elegido = int(numero_elegido)
    contador += 1
    acumulador += numero_elegido
    seguir = input("desea seguir? si/no: ")

promedio = acumulador / contador
print(f"suma de los numeros es igual: {acumulador}, el promedio es: {promedio}")
