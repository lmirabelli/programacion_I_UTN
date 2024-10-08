#1. Realizar una función llamada es_alfabetico() que recibe una cadena y verifica si la misma tiene sólo caracteres alfabéticos (a-z/A-Z) -> No hace falta tener en cuenta los acentos y algún otro carácter
#Tener en cuenta los caracteres ASCII imprimibles que sólo sean letras

cadena_uno = "hOLA munDO y el unIVErso"

def es_alfabetico(cadena: str) -> bool:
    for caracter in cadena:
        caracter_ascii = ord(caracter)
        if (caracter_ascii < 65 or caracter_ascii > 90) and (caracter_ascii < 97 or caracter_ascii > 122):
            return False
        
    return True

alfabetico = es_alfabetico(cadena_uno)
print(f"1 - alfabetico: {alfabetico}")


#2. Realizar una función llamada es_entero() que recibe una cadena y verifica si la misma tiene sólo caracteres numéricos (0-9)

def es_entero(cadena: str) -> bool:
    for caracter in cadena:
        caracter_ascii = ord(caracter)
        if caracter_ascii < 48 or caracter_ascii > 57:
            return False
        
    return True

numerico = es_entero(cadena_uno)
print(f"2 - numerico: {numerico}")

#3. Realizar una función llamada es_alfanumerico() que recibe una cadena y verifica si la misma tiene sólo caracteres alfanuméricos (a-z/A-Z/0-9)

def es_alfanumerico(cadena):
    alfabetico = es_alfabetico(cadena)
    numerico = es_entero(cadena)

    if alfabetico or numerico:
        return True
    else:
        for caracter in cadena:
            caracter_ascii = ord(caracter)
            if (caracter_ascii > 65 or caracter_ascii < 90) and (caracter_ascii > 97 or caracter_ascii < 122) and (caracter_ascii > 48 or caracter_ascii < 57):
                return True
    return False

alfanumerico = es_alfanumerico(cadena_uno)
print(f"3 - alfanumerico: {alfanumerico}")

#4. Realizar la función es_mayuscula() que me verifica que la cadena que le pase como parámetro está en mayúscula o no.
#Devuelve True si esa cadena está en mayúscula.
#Devuelve False en caso contrario

def es_mayuscula(cadena: str) -> bool:
    for caracter in cadena:
        caracter_ascii = ord(caracter)
        if (caracter_ascii < 65 or caracter_ascii > 90):
            return False
        
    return True

mayuscula = es_mayuscula(cadena_uno)
print(f"4 - mayuscula: {mayuscula}")

# 5. Realizar la función es_minuscula() que me verifica que la cadena que le pase como parámetro está en minúscula o no.
# Devuelve True si esa cadena está en minúscula.
# Devuelve False en caso contrario

def es_minuscula(cadena: str) -> bool:
    for caracter in cadena:
        caracter_ascii = ord(caracter)
        if (caracter_ascii < 97 or caracter_ascii > 122):
            return False
        
    return True

minuscula = es_minuscula(cadena_uno)
print(f"5 - minuscula: {minuscula}")

#6. Realizar una función que me permita convertir un carácter de mi cadena a mayúscula, se le pasa como parámetro un str con un sólo carácter (validar que esto ocurra) y devuelve dicho carácter en mayúscula. 
#En caso de que el carácter no sea alfabético o ya se encuentre en mayúscula, devuelve ese mismo carácter sin cambios, en caso de que haya recibido un str con más de un carácter la función devuelve None.

def devolver_mayuscula(cadena: str) -> str:
    if len(cadena) == 1:
        caracter_ascii = ord(cadena)
        if(caracter_ascii > 96 and caracter_ascii < 123 ):
            return chr(caracter_ascii - 32)
        else:
            return cadena

    else:
        return None
    
cadena_dos = 'u'
cadena_tres = 'K'

dev_cadena_uno = devolver_mayuscula(cadena_uno)
dev_cadena_dos = devolver_mayuscula(cadena_dos)
dev_cadena_tres = devolver_mayuscula(cadena_tres)

print(dev_cadena_uno, dev_cadena_dos, dev_cadena_tres)

#7. Realizar una función que me permita convertir un carácter de mi cadena a minúscula, se le pasa como parámetro un str con un sólo carácter (validar que esto ocurra) y devuelve dicho carácter en minúscula. 
#En caso de que el carácter no sea alfabético o ya se encuentre en mayúscula, devuelve ese mismo carácter sin cambios, en caso de que haya recibido un str con más de un carácter la función devuelve None.

def devolver_minuscula(cadena: str) -> str:
    if len(cadena) == 1:
        caracter_ascii = ord(cadena)
        if(caracter_ascii > 64 and caracter_ascii < 91 ):
            return chr(caracter_ascii + 32)
        else:
            return cadena

    else:
        return None

dev_cadena_uno = devolver_minuscula(cadena_uno)
dev_cadena_dos = devolver_minuscula(cadena_dos)
dev_cadena_tres = devolver_minuscula(cadena_tres)

print(dev_cadena_uno, dev_cadena_dos, dev_cadena_tres)


#8.Realizar una función que me permita convertir toda mi cadena a mayúscula, se le pasa una cadena y devuelve la misma convirtiendo cada carácter alfabético en minúscula a mayúscula.
#Los otros caracteres que no sean alfabéticos simplemente los deja como está.

def conversion_mayusculas(cadena : str ) -> str:

    cadena_mayuscula = ''
    for i in cadena:
        caracter_ascii = ord(i)
        if(caracter_ascii > 96 and caracter_ascii < 123 ):
            cadena_mayuscula += chr(caracter_ascii - 32)
        else:
            cadena_mayuscula += i
    
    return cadena_mayuscula

cadena_mayuscula = conversion_mayusculas(cadena_uno)

print(cadena_mayuscula)

#9.Realizar una función que me permita convertir toda mi cadena a minúscula, se le pasa una cadena y devuelve la misma convirtiendo cada carácter alfabético en mayúscula a minúscula.
#Los otros caracteres que no sean alfabéticos simplemente los deja como está.

def conversion_minuscula(cadena : str ) -> str:

    cadena_minuscula = ''
    for i in cadena:
        caracter_ascii = ord(i)
        if(caracter_ascii > 64 and caracter_ascii < 91 ):
            cadena_minuscula += chr(caracter_ascii + 32)
        else:
            cadena_minuscula += i
    
    return cadena_minuscula

cadena_minuscula = conversion_minuscula(cadena_uno)

print(cadena_minuscula)

#10.Crear una función llamada capitalizar_texto(), en la que recibe una cadena y devuelve la misma con la primer letra en mayúscula y todas las demás en minúscula.

def capitalizar_texto(cadena : str) -> str:
    cadena_capitalizada = ''
    for i in range(len(cadena)):
        if i == 0:
            caracter = conversion_mayusculas(cadena[i])
            cadena_capitalizada += caracter
        else:
            caracter = conversion_minuscula(cadena[i])
            cadena_capitalizada += caracter
    
    return cadena_capitalizada

cadena_capitalizada = capitalizar_texto(cadena_uno)
print(cadena_capitalizada)

#11.Crear una función llamada generar_titulo(), en la que recibe una cadena y devuelve la misma con cada palabra con la primera letra mayúscula y todas las demás en minúscula

def generar_titulo(cadena : str) -> str:
    contador = 0
    cadena_titulo = ''
    for i in range(len(cadena)):
        codigo_ascii = ord(cadena[i])
        if contador == 0:
            caracter = conversion_mayusculas(cadena[i])
            cadena_titulo += caracter
        else:
            caracter = conversion_minuscula(cadena[i])
            cadena_titulo += caracter
        
        if codigo_ascii == 32:
            contador = 0
        else:
            contador += 1
    
    return cadena_titulo

cadena_titulo = generar_titulo(cadena_uno)
print(cadena_titulo)


#12.Crear una función llamada formatear_nombre_apellido() en la que recibe una cadena cualquiera y extrae sólo el nombre y apellido de la misma en el formato correcto: (Nombre Apellido)

def formatear_nombre_apellido(cadena : str) -> str:
    contador = 0
    nombre_completo = ''

    for i in range(len(cadena)):
        codigo_ascii = ord(cadena[i])
        if codigo_ascii == 32:
            nombre_completo += cadena[i]
            contador = 0
        elif codigo_ascii > 64 and codigo_ascii < 91:
            if contador == 0:
                nombre_completo += cadena[i]
                contador += 1
            else:
                nombre_completo += chr(codigo_ascii + 32)
                contador += 1
        elif codigo_ascii > 96 and codigo_ascii < 123:
            if contador != 0:
                nombre_completo += cadena[i]
                contador += 1
            else:
                nombre_completo += chr(codigo_ascii - 32)
                contador += 1
    
    return nombre_completo

nombre_desastre = "123mAriAnO ferNanDEZ 911%@"
cadena_nombre = formatear_nombre_apellido(nombre_desastre)
print(cadena_nombre)

# 13. Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos consecutivos.

def eliminar_duplicados(cadena : str) -> str:
    caracter_anterior = ''
    nueva_cadena = ''
    for i in cadena:
        normalizando = ord(i)
        if normalizando > 64 and normalizando < 91:
            normalizando = normalizando + 32
        if normalizando != caracter_anterior:
            nueva_cadena += i
            caracter_anterior = normalizando
    
    return nueva_cadena

sin_duplicados = eliminar_duplicados('hHoooOolLlla')
print(sin_duplicados)

def borrar_vocales(cadena: str) -> str :
    sin_vocales = ''
    for i in cadena:
        normalizando = ord(i)
        if normalizando > 64 and normalizando < 91:
            normalizando = normalizando + 32
        if normalizando != 97 and normalizando != 101 and normalizando != 105 and normalizando != 111 and normalizando != 117:
            sin_vocales += chr(normalizando)
            # si le pones directamente la variable i va a agregar el caracter sin importar su condicion, de esta manera normalizamos la cadena en minusculas
    
    return sin_vocales

sin_vocales = borrar_vocales(cadena_uno)
print(sin_vocales)

#15.Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena. 

def buscar_coincidencia(cadena: str, coincidencia: str) -> int:
    largo_cadena = len(cadena)
    largo_coincidencia = len(coincidencia)
    contador = 0
    
    for i in range(largo_cadena - largo_coincidencia + 1):
        
        if cadena[i:i + largo_coincidencia] == coincidencia:
            contador += 1

    return contador

cadena_original = "El origen del gen"
coincidencia = "gen"

cuenta_de_coincidencias = buscar_coincidencia(cadena_original, coincidencia)
print(cuenta_de_coincidencias)