producto1 = float(input('ingresa el precio del producto 1: '))
producto2 = float(input('ingresa el precio del producto 2: '))
producto3 = float(input('ingresa el precio del producto 3: '))

print('Los precios ingresados son: $' + str(producto1) + ', $' + str(producto2) + ', $' + str(producto3))
suma_de_valores = producto1 + producto2 + producto3
precio_promedio = (producto1 + producto2 + producto3) / 3
iva = 0.21
iva_cobrado = (producto1 + producto2 + producto3) * iva
precio_con_iva = suma_de_valores + iva_cobrado
print('La suma de ellos es: $' + str(suma_de_valores))
print('El preco promedio es: $' + str(precio_promedio))
print('Precio con iva: $' + str(precio_con_iva) + ' el fue de: $' + str(iva_cobrado))