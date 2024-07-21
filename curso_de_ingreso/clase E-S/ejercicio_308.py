# E/S 8
# LEONARDO MIRABELLI

# Ingresar 10 números enteros. Determinar el máximo y el mínimo

contador = 0

while contador < 10:
    contador += 1
    numero_elegido = input(f"elige un numero ({contador}/10): ")
    numero_elegido = int(numero_elegido)
    if contador == 1:
        minimo = numero_elegido
        maximo = numero_elegido
    elif minimo > numero_elegido:
        minimo = numero_elegido
    elif maximo < numero_elegido:
        maximo = numero_elegido

print(f"El numero maximo elegido fue {maximo} y el minimo fue {minimo}")

