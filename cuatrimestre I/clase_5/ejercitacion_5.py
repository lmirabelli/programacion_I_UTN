# 1. Desarrollar una función que verifique el DNI de una persona, la misma recibirá un str (se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True

# 2. Desarrollar una función que complete el número de DNI de una persona. Recibirá un str (se asume que solamente contiene caracteres numéricos), deberá medirla (len) y completar con ceros a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. 
#En caso de que el dni sea invalido (que no tiene entre 6 y 8 caracteres) devolvera una cadena que dice : “DNI INVALIDO”


def verificar_dni(numero_dni):
    '''Calcula la cantidad de digitos ingresados, retornando de 6 a 8 digitos como true y sino retorna un false (para el punto 1)'''
    cantidad_digitos = len(numero_dni)

    if cantidad_digitos < 6 or cantidad_digitos > 8:
        return False
    else:
        return True    
    

def completar_dni(numero_dni):
    '''Verifica la cantidad de digitos que tiene el DNI si tiene 6 o 7 lo autocompleta con 0 a la izquierda hasta llegar a 8 digitos, sino lo deja como se ingreso'''
    cantidad_digitos = len(numero_dni)

    if cantidad_digitos == 6:
        numero_dni = f"00{numero_dni}"
    elif cantidad_digitos == 7:
        numero_dni == f"0{numero_dni}"
    
    return numero_dni

dni_ingresado = input("Escriba su numero de DNI: ")

validacion_dni = verificar_dni(dni_ingresado)
dni = completar_dni(dni_ingresado)
print(dni)
print(validacion_dni)



