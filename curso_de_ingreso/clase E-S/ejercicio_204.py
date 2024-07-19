# E/S 4
# LEONARDO MIRABELLI

# A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir más de 1.80 metros.

altura_ingresada = input("ingrese su altura: ")

altura_ingresada = float(altura_ingresada)

if altura_ingresada > 1.8:
    print("Usted es pivot")
else:
    print("Usted no es pivot")