# E/S 9
# LEONARDO MIRABELLI

# Pedir el ingreso de una clave.
# Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

clave = "Python3"
clave_correcta = 'no'


while clave_correcta == 'no':
    clave_ingresada = input(f"para ingresar coloque la clave: ")
    if clave == clave_ingresada:
        clave_correcta = 'si'
    else:
        print("*** CONTRASEÑA INCORRECTA ***")


print("*** BIENVENIDO USER ***")
