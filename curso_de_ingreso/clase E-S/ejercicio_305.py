# E/S 5
# LEONARDO MIRABELLI

# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar por pantalla.


contador = 0
acumulador = 0

# Va mostrando el resultado iteracion por iteracion

while contador < 5:
    numero_elegido = input("elige un numero: ")
    numero_elegido = int(numero_elegido)
    acumulador += numero_elegido
    print(acumulador)
    contador += 1
    print(acumulador / contador)



contador = 0
acumulador = 0

# Va a mostrar el resultado solamente al final

while contador < 5:
    contador += 1
    numero_elegido = input(f"elige un numero ({contador}/5): ")
    numero_elegido = int(numero_elegido)
    acumulador += numero_elegido

print(f"La suma de los numeros es: {acumulador}")
print(f"Promedio de los numeros elegidos: {acumulador / 5}")