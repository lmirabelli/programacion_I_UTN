import os
from funciones import *


def menu():
    calculos_realizados = 'no'
    bandera_primer_operando = 'no'
    bandera_segundo_operando = 'no'
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))
        if opcion == 1:
            primer_operando = int(input("Ingreso Primer Operando"))
            bandera_primer_operando = "si"
        elif opcion == 2:
            segundo_operando = int(input("Ingreso Primer Operando"))
            bandera_segundo_operando = 'si'
        elif opcion == 3:
            if bandera_primer_operando == 'si' and bandera_segundo_operando == 'si':
                resultado_suma = sumar(primer_operando, segundo_operando)
                resultado_resta = restar(primer_operando, segundo_operando)
                resultado_multiplicacion = multiplicar(primer_operando, segundo_operando)
                resultado_division = dividir(primer_operando, segundo_operando)
                resultado_potencia = potenciar(primer_operando, segundo_operando)
                resultado_factorizacion_uno = factorial(primer_operando)
                resultado_factorizacion_dos = factorial(segundo_operando)
                calculos_realizados = 'si'
            else:
                print("Debe completar la opcion 1 y opcion 2")
        elif opcion == 4:
                if calculos_realizados == 'si':
                    print(f"suma: {resultado_suma}")
                    print(f"resta: {resultado_resta}")
                    print(f"multiplicacion: {resultado_multiplicacion}")
                    print(f"division: {resultado_division}")
                    print(f"potencia: {resultado_potencia}")
                    print(f"factorial del primer numero: {resultado_factorizacion_uno}")
                    print(f"factorial del segundo numero: {resultado_factorizacion_dos}")
                else:
                    print("Debe obtener los resultados de los calculos en la opcion 3")
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
            
        # os.system('clear')
    
    
menu()
