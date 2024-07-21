# INTEGRADOR ESTRUCTURAS REPETITIVAS
# LEONARDO MIRABELLI

contador = 0
suma_negativos = 0
suma_positivos = 0
contador_negativos = 0
maximo_positivo = 'no se ingreso ningun positivo'

while True:
    numero_elegido = input("Elija un numero entre -10000 y 10000 sin que sea 0: ")
    numero_elegido = int(numero_elegido)

    if numero_elegido >= -10000 and numero_elegido <= 10000 and numero_elegido != 0:
        contador += 1
        if numero_elegido > 0:
            suma_positivos += numero_elegido
            if contador == 1:
                maximo_positivo = numero_elegido
            elif maximo_positivo < numero_elegido:
                maximo_positivo = numero_elegido
        else:
            suma_negativos += numero_elegido
            contador_negativos += 1
        
        continuar = input("Desea continuar? si/no: ")
        if continuar == 'no':
            break
    else:
        print(f"El numero {numero_elegido} no esta dentro de los parametros acordados, vuelva a intentarlo")





promedio_positivos = suma_positivos / contador
porcentaje_negativo = (contador_negativos / contador) * 100

print(f"La suma de los numeros negativos es de {suma_negativos}.\nLa suma de los positivos {suma_positivos}\nLa cantidad de numeros negativos ingresados es de {contador_negativos} y su porcentaje fue del {porcentaje_negativo}%\nEl promedio de los numeros positivos es {promedio_positivos} y el positivo mas grande elegido es {maximo_positivo}")
