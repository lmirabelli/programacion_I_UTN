# E/S 12
# LEONARDO MIRABELLI

# Solicitarle al usuario el ingreso de un color primario.
# Validar que el mismo sea Rojo, Verde o Azul.

while True:
    color = input("Coloque el nombre de un color primario: ")

    if color == 'rojo' or color == "azul" or color == "amarillo":
        break
    else:
        print("*** COLOR EQUIVOCADO ***")


print(f"Muy bien el color {color} es un primario")