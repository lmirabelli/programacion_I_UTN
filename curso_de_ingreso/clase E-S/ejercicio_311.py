# E/S 11
# LEONARDO MIRABELLI

# Pedir al usuario el ingreso de una nota.
# La misma debe estar comprendida entre 1 y 10 inclusive.

while True:
    nota = input("Ingrese una nota del 1 al 10: ")
    nota = int(nota)

    if nota < 11 and nota > 0:
        break

print(f"La nota fue de {nota}")
