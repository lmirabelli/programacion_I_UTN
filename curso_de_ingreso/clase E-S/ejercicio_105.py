# LEONARDO MIRABELLI
# E/S 5

# Realizar un programa que permita el ingreso de dos números. Calcular la suma, resta, multiplicación y división de los mismos. Mostrar los resultados por pantalla. Utilizar una variable para mostrar el resultado (concatenar).

primer_numero_ingresado = input("Ingrese el primer numero: ")
segundo_numero_ingresado = input("Ingrese el segundo numero: ")

primer_numero_ingresado = int(primer_numero_ingresado)
segundo_numero_ingresado = int(segundo_numero_ingresado)

resultado_de_la_suma = primer_numero_ingresado + segundo_numero_ingresado
resultado_de_la_division = primer_numero_ingresado / segundo_numero_ingresado
resultado_de_la_resta = primer_numero_ingresado - segundo_numero_ingresado
resultado_de_la_multiplicacion = primer_numero_ingresado * segundo_numero_ingresado

print(f"Suma: {resultado_de_la_suma}, Resta: {resultado_de_la_resta}, Multiplicacion: {resultado_de_la_multiplicacion}, Division:  {resultado_de_la_division}")