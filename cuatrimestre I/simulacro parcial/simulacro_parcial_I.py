# Una competencia de baile califica a los mejores bailarines de la ciudad.
# De 10 participantes los tres jurados fueron calificando al mejor bailarín o bailarina de la
# ciudad
# Cada bailarín o bailarina se los identifica con un número que comienza del 1 hasta el 10
# Realizar (en lo posible) un menú de opciones:
# 1
# 1. Calificar Bailarines: Se realiza una carga secuencial de todas las notas que eligió
# cada jurado de cada uno de los bailarines.
# 2. Mostrar Notas: Muestra en un lindo formato los siguientes datos:
# Nro Participante, Nota Jurado 1,Nota Jurado 2,Nota Jurado 3,Nota Promedio:
# 3. Ordenar Bailarines jurado 2: Ordena a los participantes por la mejor nota que les
# puso el jurado 2.
# 4. Triple 7: Encontrar y mostrar a los participantes que tengan un 7 de nota en todos los
# jurados. En caso de no haber indicar que no existen.
# 5. Jurado malo: Muestra a todos los bailarines que fueron aplazados por el jurado 3
# (Aplazo seria nota menor 4)
# 6. TOP 3: Muestra el top 3 de los participantes con mayor nota promedio.
# 7. Verificar Ganador: El ganador de la competencia se verifica con el bailarín/bailarina
# que tenga mayor nota promedio. En caso de empate se tendrá en cuenta la nota del
# jurado 1. En caso de igualdad nuevamente se muestran todos los ganadores que
# hayan resultado.

tabla = []
cantidad_bailarines = 10
triple_siete = []
jurado_malo = []

def ordenar_mayor_menor(lista: list) -> bool:
    '''Acomoda de mayor a menor los puntajes del promedio (columna con index 4)'''
    validacion_lista_acomodada = False

    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if lista[i][4] < lista[j][4]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                validacion_lista_acomodada = True
    
    return validacion_lista_acomodada


def puntuar_de_jurados() -> int:
    ''' inserta el puntaje de cada jurado'''
    puntaje = int(input("Colocar el puntaje del jurado: "))
    while puntaje < 1 or puntaje > 10:
        print("El puntaje colocado es invalido... ")
        puntaje = int(input("Colocar el puntaje del jurado: "))
    return puntaje


def puntuar_bailarines(tabla : list, cantidad_bailarines : int) -> list:
    ''' Recorre la cantidad de bailarines asignados (10)'''
    for i in range(cantidad_bailarines):
        print(f"Bailarin {i+1}")
        bailarin = [i+1,0,0,0,0]
        for j in range(3):
            print(f"Jurado {j+1}")
            bailarin[j+1] = puntuar_de_jurados()
        bailarin[4] = ((bailarin[1] + bailarin[2] + bailarin[3]) / 3) + bailarin[1] / 10000
        
        if bailarin[1] == 7 and bailarin[2] == 7 and bailarin[3] == 7:
            triple_siete.append(bailarin)
        if bailarin[3] < 4:
            jurado_malo.append(bailarin)
        tabla.append(bailarin)
    return tabla



def mostrar_notas(tabla: list, ocasion: str, posiciones: int):
    '''imprime en consola los resultados pedidos'''
    print(ocasion)
    if ocasion != "ganador":
        for i in range(posiciones):
            print(f"Bailarin {tabla[i][0]}: \n Jurado 1: {tabla[i][1]} \n Jurado 2: {tabla[i][2]} \n Jurado 3: {tabla[i][3]} \n Promedio: {tabla[i][4]} \n ---")
    elif ocasion == "ganador":
        print(f"The Winner is: el bailarin {tabla[0][0]}")
    if posiciones == 0:
        print(f"Ningun Balarin {ocasion}")
    print("---------------------------------------------------")



puntuar_bailarines(tabla, cantidad_bailarines)
mostrar_notas(tabla, "", len(tabla))
ordenar_mayor_menor(tabla)
mostrar_notas(triple_siete, "tuvo un 7 de parte de los 3 jurados", len(triple_siete))
mostrar_notas(jurado_malo, "fue aplazado por el jurado 3", len(jurado_malo))
mostrar_notas(tabla, "TOP 3", 3)
mostrar_notas(tabla, "ganador", 1)

