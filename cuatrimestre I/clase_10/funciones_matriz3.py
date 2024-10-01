def mostrar_matriz(matriz:list)->None:
    for fil in range(len(matriz)):#PARA LAS FILAS,largo de la lista es la cantidad de filas
        for colum in range(len(matriz[fil])):#PARA LAS COLUMNAS,va iterando cada valor en cada fila
            print(matriz[fil][colum], end=" ")
        print(" ")

def inicializar_matriz(cant_filas:int, cant_columnas:int,valor_inicial)->list:
    matriz = []
    for _ in range(cant_filas):
        fila =[valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz
