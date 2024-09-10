# 1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_recursividad(numero:int) -> int:

    retorno = 0
    if numero > 0:
        
        retorno = numero + sumar_recursividad(numero - 1)
    
    return retorno



#2. Realizar una función recursiva que calcule la potencia de un número:

def potenciar_recursividad(base:int, potencia:int) -> int:
    
    if potencia == 0:
        retorno = 1
    elif potencia < 0:
        retorno = 1 / potenciar_recursividad(base, potencia * -1)
    else:
        retorno = base * potenciar_recursividad(base, potencia - 1)
    
    return retorno


numero_escogido = int(input("Escoge un numero para la suma de recursividad: "))
suma = sumar_recursividad(numero_escogido)
print(suma)

numero_base = int(input("Escoge un numero para la potencia de recursividad: "))
numero_exponente = int(input("Escoge la potencia de ese numero: "))

potencia = potenciar_recursividad(numero_base,numero_exponente)
print(potencia)