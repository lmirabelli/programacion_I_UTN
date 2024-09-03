# DIVISION 114
# LEONARDO MIRABELLI


#1

for i in range(10):
    print(i + 1)

#2

for i in range(10,0,-1):
    print(i)

#3

numero_uno = int(input("ingrese un numero: "))
numero_dos = int(input("ingrese otro numero: "))

if numero_uno > numero_dos:
    for i in range(numero_uno, numero_dos - 1, -1):
        print(i)
elif numero_uno < numero_dos:
    for i in range(numero_uno, numero_dos + 1, 1):
        print(i)
else:
    print(numero_uno)

#4

suma_total = 0
contador = 0
for i in range(5):
    numero_elegido = int(input(f"Elija un numero ({i + 1}): "))
    contador += 1
    suma_total += numero_elegido
    if numero_elegido == 0:
        break

promedio = suma_total / contador
print(f"La suma de los numeros escogidos es {suma_total}, y el promedio {promedio}")

#5

for i in range(1,100,2):
    print(i + 1)

#6

numero_uno = int(input("ingrese un numero: "))
divisores = 0

for i in range(2,numero_uno + 1,1): 
    resto = numero_uno % (i)
    if resto == 0:
        divisores += 1

if divisores == 1:
    print("El numero escogido es primo")
else:
    print(f"El numero escogido no es primo, tiene {divisores} divisores")

#7

numero = int(input("ingresa un numero: "))
numeros_primos = 0

for i in range(1, numero + 1, 1):
    divisores = 0
    for j in range(2, i + 1, 1):
        resto = i % j
        if resto == 0:
            divisores += 1
    if divisores == 1:
        numeros_primos += 1
        print(i)


print(f"La cantidad de numeros primos entre el 1 y el {numero} es {numeros_primos}")

#8

numero = int(input("ingresa un numero: "))

for i in range(11):
    resultado_multiplicacion = numero * i
    print(f"{numero} x {i} = {resultado_multiplicacion}")