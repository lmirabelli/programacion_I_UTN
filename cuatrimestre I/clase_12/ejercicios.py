
# CADENAS





# 7. Realizar una función que me quite los espacios de mi cadena, recibe una cadena y devuelve una nueva cadena con los espacios eliminados.

# 8. Crear una función llamada repetir_cadena() que lo que va a hacer es replicar lo mismo que hace el operador * en cadenas pero separando las mismas por un espacio, se le pasa como parámetro la cadena que va a repetir, y un entero que me indique la cantidad de veces que la misma se va a repetir. 
# Devuelve como resultado una cadena resultante.

# NOTA: Resolver sin usar operador *

# Ejemplo de uso:
# cadena = “Hola”
# cadena_repetida = repetir_cadena(cadena,5)

# print(cadena_repetida) -> ‘’hola hola hola hola hola‘’ 

# 1. Realizar una función que me permita ordenar una matriz de productos [nombre,precio,stock] por precio de mayor a menor y tomando como segundo criterio el stock (mayor a menor también)

stock_mercaderia = [["coca cola",2100,12],["pepsi",1900,18],["lays",2100,13],["cafe",1900,4],["yerba",1950,16]]


def ordenar_menor_mayor(lista: list,primario : int,secundario : int , condicion : str) -> list:
    '''Ordena la lista ingresada por parametro de menor a mayor'''

    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if condicion == "igual":
                if (lista[i][primario] > lista[j][primario]) or (lista[i][primario] == lista[j][primario] and lista[i][secundario] > lista[j][secundario]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else:
                if (lista[i][primario] > lista[j][primario]) or (lista[i][primario] == lista[j][primario] and lista[i][secundario] < lista[j][secundario]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                

    
    return lista

def ordenar_mayor_menor(lista: list,primario : int,secundario : int, condicion: str) -> list:
    '''Ordena la lista ingresada por parametro de mayor a menor'''

    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if condicion == "igual":
                if (lista[i][primario] < lista[j][primario]) or (lista[i][primario] == lista[j][primario] and lista[i][secundario] < lista[j][secundario]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else:
                if (lista[i][primario] < lista[j][primario]) or (lista[i][primario] == lista[j][primario] and lista[i][secundario] > lista[j][secundario]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    
    return lista

stock_mercaderia_mayor_precio_mayor_stock= ordenar_mayor_menor(stock_mercaderia,1,2,"igual")
print(stock_mercaderia_mayor_precio_mayor_stock)

# 2. Realizar una función que me permita ordenar una matriz de productos [nombre,precio,stock] por precio de mayor a menor y tomando como segundo criterio el nombre (alfabeticamente)

# 3. Realizar una función que me permita ordenar una matriz (cualquiera) por doble criterio , recibirá la matriz a ordenar, el índice de la columna del primer criterio, el índice de la columna del segundo criterio, el orden de ordenamiento (mayor o menor) (mismo para ambos criterios) 
# Se puede usar la matriz del ejercicio 1 como ejemplo

# 4. Dada la función anterior mejorarla a tal nivel que me permita elegir un orden diferente para cada criterio, por ejemplo capaz quiero ordenar de mayor a menor el primer criterio y de menor a mayor el segundo criterio.
# Usar de base lo desarrollado en el ejercicio 2, debería funcionar para resolver de la misma manera. El criterio del precio se ordenará de mayor a menor y el criterio del nombre alfabéticamente (menor a mayor)

stock_mercaderia_mayor_precio_alfabetico= ordenar_mayor_menor(stock_mercaderia,1,0,"")
print(stock_mercaderia_mayor_precio_alfabetico)

# 5. Realizar una función que me cuente la cantidad de vocales de mi cadena, la misma recibe una cadena y devuelve la cantidad de vocales que encontró.
# 6. Realizar una función que me cuente la cantidad de consonantes de mi cadena, la misma recibe una cadena y devuelve la cantidad de consonantes que encontró.

def contar_vocales( cadena : str,vocales : list, tipo) -> int:
    cantidad = 0
    for i in cadena:
        if i != " ":
            bandera = 0
            for j in vocales:
                if tipo == "vocales":
                    if i == j:
                        cantidad += 1
                else:
                    if i != j:
                        bandera += 1
            if bandera == 5:
                cantidad += 1   

    return cantidad

cadena_original = input("escriba la palabra/frase de la cual quiere que se cuente las vocales: ")
vocales = ["a","e","i","o","u"]

numero_vocales = contar_vocales(cadena_original, vocales, "vocales")
numero_consonantes = contar_vocales(cadena_original, vocales, "")
print(f"{cadena_original} tiene {numero_vocales}")
print(f"{cadena_original} tiene {numero_consonantes}")