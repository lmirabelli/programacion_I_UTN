import random

def cargar_listas() -> list:
    '''Ingresa el numero de lista de los postulantes, retorna una lista con el numero de lista introducido y la cantidad de votos en todos los turnos en 0.'''

    listas = []
    for i in range(5):
        numero_lista = int(input("Ingrese un numero de lista (debe tener 3 cifras): "))
    
        
        while numero_lista < 100 or numero_lista > 999:
            print("el numero de lista es incorrecto")
            numero_lista = int(input("Elija otro: "))

        lista = [numero_lista,0,0,0,0]
        listas += [lista]
    return listas

def cargar_votos(listas: list) -> int:
    '''Carga la cantidad de votos de cada lista y calcula el total'''
    for i in range(len(listas)):
        for j in range(5):
            if j > 0 and j < 4:
                texto = ""
                if j == 1:
                    texto = "turno mañana"
                elif j == 2:
                    texto = "turno tarde"
                elif j == 3:
                    texto = "turno noche"
                votos = int(input(f"Cargue los votos de {texto} para la lista {listas[i][0]}: "))

                while votos < 0:
                    votos = int(input("No puede ser votos negativos, reingrese la cantidad de votos: "))

                listas[i][j] = votos
            elif j == 4:
                listas[i][j] = listas[i][1] + listas[i][2] + listas[i][3]


def mostrar_resultados(lista: list, total: int):
    '''Muestra los datos'''
    porcentaje = float((lista[4] / total * 100))
    print(f"------------ \n Numero de Lista: {lista[0]} \n votos de la mañana: {lista[1]} \n votos de la tarde: {lista[2]} \n votos de la noche: {lista[3]} \n Porcentaje: {porcentaje:.2f}%")

def calcular_votantes(listas: list) -> int:
    '''Calcula la cantidad de votantes'''
    total = 0
    for i in range(len(listas)):
        total += listas[i][4]
    
    return total

def ordenar_mayor_menor(lista: list,turno: int) -> bool:
    '''Ordena la lista ingresada por parametro de mayor a menor'''
    validacion_lista_acomodada = False

    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if lista[i][turno] < lista[j][turno]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                validacion_lista_acomodada = True
    
    return validacion_lista_acomodada

def definir_listas_votadas_por_nadie(lista: list, total: int) -> list:
    '''Define si alguna lista tuvo menos del 5% de los votos'''
    porcentaje = float((lista[4] / total * 100))
    no_te_voto_nadie = []
    if porcentaje < 5:
        lista_no_votada = [lista[0],porcentaje]
        no_te_voto_nadie += [lista_no_votada]
    
    return no_te_voto_nadie

def calcular_votantes_por_turno(listas: list) -> list:
    '''calcula cuantos votos hubo por turno'''
    manana = 0
    tarde = 0
    noche = 0
    for i in range(len(listas)):
        manana += listas[i][1]
        tarde += listas[i][2]
        noche += listas[i][3]
    
    votos_por_turno = [manana, tarde, noche]
    return votos_por_turno


def definir_ballotage(lista: list,total: int,votos_por_turno:int):
    print(lista[0][4],total)
    if (lista[0][4] / total) < 50:

        print("Hay ballotage")
        votos_totales = votos_por_turno[0] + votos_por_turno[1] + votos_por_turno[2]
        candidato_1 = random.randint(0,votos_totales)
        candidato_2 = votos_totales - candidato_1

        if(candidato_1 > candidato_2):
            print(f"Ganador por Ballotage es {lista[0][0]}")
        else:
            print(f"Ganador por Ballotage es {lista[1][0]}")

    else:
        print("No hay Ballotage")






listas = cargar_listas()
cargar_votos(listas)
total_votantes = calcular_votantes(listas)
for i in range(len(listas)):
    mostrar_resultados(listas[i],total_votantes)
    no_te_voto_nadie = definir_listas_votadas_por_nadie(listas[i],total_votantes)
    
votos_por_turno = calcular_votantes_por_turno(listas)
ordenar_mayor_menor(listas,1)
ordenar_mayor_menor(listas,4)
definir_ballotage(listas,total_votantes,votos_por_turno)





