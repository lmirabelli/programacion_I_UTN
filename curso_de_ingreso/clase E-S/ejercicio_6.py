# LEONARDO MIRABELLI
# E/S 6

#Realizar un programa que pida dos números enteros. Calcular y mostrar el resto de la división entre ambos números. Ej: "El resto de dividir 7 por 2 es: 1" .


primer_numero_ingresado = input("Ingrese el primer numero: ")
segundo_numero_ingresado = input("Ingrese el segundo numero: ")

primer_numero_ingresado = int(primer_numero_ingresado)
segundo_numero_ingresado = int(segundo_numero_ingresado)

resultado_division = primer_numero_ingresado % segundo_numero_ingresado

print(f"El resto de dividir {primer_numero_ingresado} por {segundo_numero_ingresado} es: {resultado_division}")