# E/S 3
# LEONARDO MIRABELLI

# A partir del ingreso de una edad, determinar si la persona es mayor de edad o no. Si es mayor de 18 se mostrará el mensaje “UD ES MAYOR DE EDAD” caso contrario “UD ES MENOR DE EDAD”.

edad_ingresada = input("ingrese su edad: ")

edad_ingresada = int(edad_ingresada)

if edad_ingresada >= 18:
    print("UD ES MAYOR DE EDAD")
else:
    print("UD ES MENOR DE EDAD")