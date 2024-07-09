edad = int(input("Que edad tenes? "))

if edad == 18: print('Usted tiene 18 años')

if edad > 17:
    print('MAYOR')
else:
    print('MENOR')

altura = float(input("Ingrese su altura en metros: "))

if altura > 1.8:
    print("Usted puede ser pivot")
else:
    print('Usted no puede ser pivot')

edad = int(input("Que edad tenes? "))
if edad > 12 and edad < 18:
    print("Adolecente")
elif edad < 13:
    print('Niño')
else: print('Mayor de Edad')
