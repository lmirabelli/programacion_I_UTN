sumaDePares = 0

for i in range(10):
    if i % 2 == 0:
        sumaDePares = sumaDePares + i
        print(sumaDePares)
    else:
        pass



contraseña = input("Ingrese su contraseña: ")

while contraseña != 'utn750':
    print("Contraseña incorrecta, inténtelo de nuevo.")
    contraseña = input("Ingrese su contraseña: ")

print("Contraseña correcta, Bienvenido.")

numero = int(input("Ingrese un número entre 0 y 9 inclusive: "))


while numero < 0 or numero > 9:
    print("Número fuera de rango, inténtelo de nuevo.")
    numero = int(input("Ingrese un número entre 0 y 9 inclusive: "))

print("Número válido")


letra = input("Ingrese una letra en mayuscula: ")


while letra not in ('U', 'T', 'N'):
    print("Letra incorrecta, inténtelo de nuevo.")
    letra = input("Ingrese una letra en mayuscula: ")

print("Letra válida!")


sumaAcumulada = 0
for i in range(5):
    numero = int(input('Ingrese un numero: '))
    sumaAcumulada = sumaAcumulada + numero
    print(str(i+1) + " de 5 numero a elegir, por el moento la suma se encuentra en " + str(sumaAcumulada))

print('La suma acumulada de los 5 numeros elegidos es de: ' + str(sumaAcumulada))
print('El promedio de ese numero es de: ' + str(sumaAcumulada / 5))
