nombre = input("decime tu nombre: ")
print("Hola " + nombre)

numero1 = input("Elegí un número ")
numero2 = input("elegí otro número ")
resultado = int(numero1) + int(numero2)
print("El resultado de " + numero1 + " + " + numero2 + " nos da como resultado: " + str(resultado))

nombre = input("Coloca aqui tu nombre ")
apellido = input("Coloca aqui tu apellido ")
edad = input("Coloca aqui tu edad ")
print(nombre + " " + apellido + ", " + edad + " años")

alumno = input("Nombre del alumno ")
comision = input("Número de comisión ")
asignatura = input("Asignatura ")
presente = input("estado de presencia (presente / ausente) ")
print("El alumno " + alumno + " de la comisión " + comision + " estuvo " + presente + " en " + asignatura)

lado_cuadrado = input("Cuanto mide el lado del cuadrado ")
superficie_cuadrado = int(lado_cuadrado) ** 2
print("La superficie del cuadrado es: " + str(superficie_cuadrado) + " CM2.")

lado_a_rectangulo = input("coloque la medida del lado corto del rectangulo ")
lado_b_rectangulo = input("coloque la medida del lado largo del rectangulo ")
superficie_rectangulo = int(lado_a_rectangulo) * int(lado_b_rectangulo)
print("La superficie de su rectangulo es de: " + str(superficie_rectangulo) + " CM2")
superficie_triangulo = superficie_rectangulo / 2
print("Si su rectangulo fuera un triangulo escaleno cortandolo de arista a arista su superficie seria de: " + str(superficie_triangulo) + " CM2")

nombre_del_producto = input("Coloque el nombre del producto: ")
precio_del_producto = input("Coloque el precio: ")
valor_iva = 0.21
iva_a_pagar = float(precio_del_producto) * valor_iva
print("El iva del/de la " + nombre_del_producto + " a pagar es: $" + str(iva_a_pagar))

nombre_del_alumno = input("ingrese el nombre y el apellido del alumno: ")
nota_1 = input("ingrese la primera nota: ")
nota_2 = input("ingrese la segunda nota: ")
nota_3 = input("ingrese la tercera nota: ")
print("Las notas de " + nombre_del_alumno + " son " + nota_1 + ", " + nota_2 + " y " + nota_3)

nombre_usuario = input("coloque el nombre del usuario: ")
edad_usuario = input("coloque la edad del usuario: ")
print(nombre_usuario + " va a tener " + str(int(edad_usuario) + 10) + " años dentro de una decada")

