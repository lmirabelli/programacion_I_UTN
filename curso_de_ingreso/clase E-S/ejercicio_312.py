# E/S 12
# LEONARDO MIRABELLI

# Solicitarle al usuario el ingreso de un color primario.
# Validar que el mismo sea Rojo, Verde o Azul.

color = input("Coloque el nombre de un color primario: ")

while color != 'rojo' and color != 'azul' and color != 'verde':
    print("*** COLOR EQUIVOCADO ***")
    color = input("Coloque el nombre de un color primario: ")



print(f"Muy bien el color {color} es un primario")