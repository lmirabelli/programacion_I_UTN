# LEONARDO MIRABELLI
# E/S 4

# Realizar un programa que permita el ingreso de dos números. Realizar la suma de los mismos y mostrar el resultado por pantalla con el siguiente formato: “La suma de los dos números es: ___”

primer_numero_ingresado = input("Ingrese el primer numero: ")
segundo_numero_ingresado = input("Ingrese el segundo numero: ")

primer_numero_ingresado = int(primer_numero_ingresado)
segundo_numero_ingresado = int(segundo_numero_ingresado)

resultado_de_la_suma = primer_numero_ingresado + segundo_numero_ingresado

print(f"La suma de los dos números es: {resultado_de_la_suma}")