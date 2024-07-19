# E/S 5
# LEONARDO MIRABELLI

# Al presionar el botón 'Calcular', se deberá obtener el contenido de la caja de texto txtEdad, transformarlo en número y calcular si es mayor, niño/a(menor de 10) o pre-adolescente. 


edad_ingresada = input("ingrese su edad: ")

edad_ingresada = int(edad_ingresada)

if edad_ingresada >= 18:
    print("UD ES MAYOR DE EDAD")
elif edad_ingresada < 11:
    print("UD ES UN NIÑO")
elif edad_ingresada < 14:
    print("UD ES UN PRE-ADOLECENTE")
else:
    print("UD ES UN ADOLECENTE")