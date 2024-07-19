# LEONARDO MIRABELLI
# E/S 2

# Realizar un programa que pida el ingreso del nombre de una persona por input y lo muestre con el formato: “Su nombre es: ___“

nombre = input("Ingrese su nombre: ") # Entrada de datos
apellido = input("Ingrese su apellido: ")

print("Su nombre es: ", nombre) # Salida de Datos
print("Su nombre es: " + nombre)
print(f"Su nombre es: {nombre} y su apellido: {apellido}")
print("Su nombre es: {0}".format(nombre))
