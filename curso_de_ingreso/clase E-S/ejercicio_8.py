# LEONARDO MIRABELLI
# E/S 8

# Realizar un programa que a partir del ingreso de un sueldo y de un porcentaje de aumento, calcule y muestre el sueldo con el aumento porcentual ingresado por el usuario.

salario_original = input("ingrese el valor de su salario: ")
aumento = input("Ingresar el porcentaje de aumento")

salario_original = float(salario_original)
aumento = float(aumento)
incremento = salario_original * (aumento / 100)
salario_incrementado = salario_original + incremento

print(f"Su nuevo salario es de: {salario_incrementado}")