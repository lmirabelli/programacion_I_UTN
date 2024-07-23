# E/S 11
# LEONARDO MIRABELLI

# Pedir al usuario el ingreso de una nota.
# La misma debe estar comprendida entre 1 y 10 inclusive.

nota = input("Ingrese una nota del 1 al 10: ")
nota = int(nota)

while nota < 1 or nota > 10:
    nota = input("Ingrese una nota del 1 al 10: ")
    nota = int(nota)


print(f"La nota fue de {nota}")
