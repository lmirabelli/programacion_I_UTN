# E/S 9
# LEONARDO MIRABELLI

# Pedir el ingreso de una clave.
# Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

clave = "Python3"


while True:
    clave_ingresada = input("para ingresar coloque la clave: ")
    if clave == clave_ingresada:
        break
    else:
        print("*** CONTRASEÑA INCORRECTA ***")


print("*** BIENVENIDO USER ***")
