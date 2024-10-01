# Nota 1:Se debería realizar la función inicializar_matriz que está en la diapositiva para definir la longitud de la matriz_resultado que va a ser usada en cada una de las funciones 


# 1. Realizar una función que permita realizar la suma entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante con la suma de las mismas.
# Tanto la matriz A como la matriz B deben tener la misma cantidad de filas y columnas, validar que eso ocurra (Podemos hacer otra función que se encargue de esto) , caso contrario retornar una lista vacía en caso de que no se cumpla.

matriz_a = [[1,2,3],
            [4,5,6,],
            [7,8,9]]

matriz_b = [[1,2,3],
            [4,5,6,],
            [7,8,9]]

def mostrar_matriz(matriz:list)->None:
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int) -> list:
    matriz = []

    for i in range(cantidad_filas):
        fila = [0] * cantidad_columnas
        matriz += [fila]
    
    return matriz


def sumar_matrices(matriz_a:list,matriz_b:list)->list:

    matriz_resultado = list()

    if type(matriz_a) == list and type(matriz_a) == list:
        if len(matriz_a) == len(matriz_b) and len(matriz_a[0]) == len(matriz_b[0]):
            matriz_resultado = inicializar_matriz(len(matriz_a),len(matriz_a[0]))
            for fil in range(len(matriz_a)):
                for col in range(len(matriz_a[0])):
                    matriz_resultado[fil][col] = matriz_a[fil][col] + matriz_a[fil][col]


    return matriz_resultado

suma_matrices = sumar_matrices(matriz_a,matriz_b)

# 2. Realizar una función que permita realizar el producto (multiplicación) de una matriz por un escalar (número entero) , la función deberá recibir la matriz a la que se le quiera realizar el producto, el número entero que multiplique a está matriz, la función devuelve una matriz nueva con el resultado de la multiplicación.

def multiplicar_matriz(matriz:list,multiplicador:int)->list:
    matriz_resultado = list()

    if type(matriz) == list and type(multiplicador) == int:
        matriz_resultado = inicializar_matriz(len(matriz),len(matriz[0]))
        for fil in range(len(matriz)):
            for col in range(len(matriz[0])):
                matriz_resultado[fil][col] = matriz[fil][col] * multiplicador
        
    return matriz_resultado

multiplicacion_matriz = multiplicar_matriz(matriz_a,4)

mostrar_matriz(multiplicacion_matriz)

# 3. Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz opuesta

def oponer_matriz(matriz:list) -> list:
    matriz_opuesta = inicializar_matriz(len(matriz),len(matriz[0]))
    for i in matriz:
        for j in len(matriz[0]):
            matriz_opuesta[i][j] = matriz[i][j] * -1

    return matriz_opuesta


