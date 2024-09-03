# Realizar una calculadora en donde se le pida al usuario una operación
# Validar (“+” , “-” , “/”, “*”) en caso de no ser ninguno de esos especificar error

# (+) -> Suma
# (-) -> Resta
# (/) -> Dividir
# (*) -> Multiplicar

# Luego de tener el operador, pedir dos números y hacer la operación correspondiente.

operacion = input("seleccione la operacion (+,-,/,*): ")

while operacion != "+" or operacion != "-" or operacion != "/" or operacion != "*":
    print("La operacion no es una opcion valida")
    operacion = input("seleccione la operacion (+,-,/,*): ")

numero_uno = int(input("selecciona un numero: "))
numero_dos = int(input("selecciona otro numero: "))
if operacion == "+":
    print(f"{numero_uno} + {numero_dos} = {numero_uno + numero_dos}")
elif operacion == "-":
    print(f"{numero_uno} - {numero_dos} = {numero_uno - numero_dos}")  
elif operacion == "*":
    print(f"{numero_uno} * {numero_dos} = {numero_uno * numero_dos}")
else:
    print(f"{numero_uno} / {numero_dos} = {numero_uno / numero_dos}")

