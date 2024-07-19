# E/S 4
# LEONARDO MIRABELLI

# Mostrar la suma de los números desde el 1 hasta el 10.

contador = 0
acumulador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        acumulador += contador
        print(acumulador)