# E/S 7
# LEONARDO MIRABELLI

# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). (concepto + ellos)
# Calcular la suma de los números positivos y el producto de los negativos.
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

    if numero_elegido > 0:
        positivos += numero_elegido
    else:
        if negativos == 0:
            negativos = numero_elegido
        else:
            negativos = negativos * numero_elegido
    
    seguir = input("desea seguir? si/no: ")

promedio = acumulador / contador
print(f"suma de los numeros es igual: {acumulador}, suma de los positivos: {positivos}, producto de los negativos: {negativos}, el promedio es: {promedio}")



