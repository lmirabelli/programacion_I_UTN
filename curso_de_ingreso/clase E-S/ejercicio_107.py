# LEONARDO MIRABELLI
# E/S 7

# Realizar un programa que a partir del ingreso de un sueldo (valor flotante) muestre dicho valor con un incremento del 15%.

salario_original = input("ingrese el valor de su salario: ")

salario_original = float(salario_original)
incremento = salario_original * 0.15
salario_incrementado = salario_original + incremento

print(f"Su nuevo salario es de: {salario_incrementado}")
