# LEONARDO MIRABELLI
# E/S 9

# Realizar un programa que a partir del ingreso del importe de una compra, aplique un 25% de descuento. Mostrar por pantalla cuánto es el total a pagar y cuánto fue el descuento obtenido.


importe = input("ingrese el importe: ")

importe = float(importe)
descuento = importe * 0.25
importe_total = importe - descuento

print(f"El importe total a pagar es de {importe_total}, el descuento fue de {descuento}")