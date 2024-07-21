# E/S 10
# LEONARDO MIRABELLI

# Pedir el ingreso de una clave.
# Validar que el ingreso del usuario sea correcto.
# Solo tendrá 3 intentos.

clave = "Python3"
intentos = 0
clave_correcta = 'no'


while intentos < 3:
    intentos += 1
    clave_ingresada = input(f"para ingresar coloque la clave (intento {intentos}/3): ")
    if clave == clave_ingresada:
        clave_correcta = 'si'
        break
    else:
        print("*** CONTRASEÑA INCORRECTA ***")

if(clave_correcta == 'si'):
    print("*** BIENVENIDO USER ***")
else:
    print("*** NO PUSISTES LA CLAVE CORRECTA *** \n segui participando")
