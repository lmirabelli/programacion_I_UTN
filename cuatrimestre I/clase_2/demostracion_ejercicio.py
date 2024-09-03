numero = int(input("ingresa un numero: "))
numeros_primos = 0

for i in range(1, numero + 1, 1):
    divisores = 0
    for j in range(2, i + 1, 1):
        resto = i % j
        if resto == 0:
            divisores += 1
            # print(divisores)
        if divisores == 2:
            break
    if divisores == 1:
        numeros_primos += 1
        print(i, end=", ")
    print(i)

print(f"La cantidad de numeros primos entre el 1 y el {numero} es {numeros_primos}")
