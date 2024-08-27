# LEONARDO MIRABELLI
# SIMULACRO


# El dueño de una tienda dedicada a la compra/venta de cartas de Yu-Gi-Oh, 
# Desea ingresar en el sistema las ventas realizadas en el dia de la fecha y conocer 
# ciertos datos en base a las cartas que se vendieron.

# Deberemos desarrollar un sistema para que el dueño pueda ingresar la siguiente información hasta que el decida.

# Nombre de carta
# Precio (no puede ser menor a 0)
# Tipo (Magica, Monstruo, Trampa)
# Rareza (Rara, Super Rara, Ultra Rara)

seguir = 'si'
cantidad_ultra_rara_precio_cincuenta = 0
carta_rara_barata = 0

total_cartas_raras = 0
total_cartas_super_raras = 0
total_cartas_ultra_raras = 0

venta_total_cartas_raras = 0
venta_total_cartas_super_raras = 0
venta_total_cartas_ultra_raras = 0

while seguir == 'si':
    nombre_carta = input('Ingrese nombre de la carta: ')
    tipo_carta = input('Ingrese el tipo de la carta debe ser (magica, monstruo o trampa): ')
    while tipo_carta != "magica" and tipo_carta != "monstruo" and tipo_carta != 'trampa':
        print("el tipo de carta es erroneo, vuelva a igresar: ")
        tipo_carta = input('Reingrese el tipo de la carta debe ser (magica, monstruo o trampa): ')

    rareza_carta = input('Ingrese la rareza de la carta, debe ser (rara, super rara o ultra rara): ')
    while rareza_carta != "rara" and rareza_carta != "super rara" and rareza_carta != "ultra rara":
        print("La rareza de la carta es erronea")
        rareza_carta = input('Reingrese la rareza de la carta, debe ser (rara, super rara o ultra rara): ')

    precio_carta = input('Ingrese el precio de la carta: $')
    precio_carta = int(precio_carta)
    while precio_carta < 0:
        print("El precio es incorrecto: ")
        precio_carta = input('Ingrese el precio de la carta: $')
        precio_carta = int(precio_carta)

    # A) Cantidad de cartas de rareza Ultra raras cuyo precio oscile en 50000 y 80000
    if rareza_carta == 'ultra rara' and precio_carta > 50000 and precio_carta < 80000:
        cantidad_ultra_rara_precio_cincuenta += 1
    
    # B) El nombre y tipo de la carta con menor precio de la rareza Rara.
    if rareza_carta == "rara":
        if carta_rara_barata == 0:
            nombre_carta_rara_barata = nombre_carta
            tipo_carta_rara_barata = tipo_carta
            precio_carta_rara_barata = precio_carta
            carta_rara_barata = 1
        elif precio_carta < precio_carta_rara_barata:
            nombre_carta_rara_barata = nombre_carta
            tipo_carta_rara_barata = tipo_carta
            precio_carta_rara_barata = precio_carta
    
    
    if rareza_carta == "rara":
        total_cartas_raras += 1
        venta_total_cartas_raras += precio_carta
    elif rareza_carta == "super rara":
        total_cartas_super_raras += 1
        venta_total_cartas_super_raras += precio_carta
    elif rareza_carta == "ultra rara":
        total_cartas_ultra_raras += 1
        venta_total_cartas_ultra_raras += precio_carta

    seguir = input("queres agregar otra carta? si/no: ")

# C) El porcentaje de rara, super rara y ultra rara hay sobre el total
total_cartas = total_cartas_raras + total_cartas_super_raras + total_cartas_ultra_raras
porcentaje_cartas_raras = float((total_cartas_raras / total_cartas) * 100)
porcentaje_cartas_super_raras = float((total_cartas_super_raras / total_cartas) * 100)
porcentaje_cartas_ultra_raras = float((total_cartas_ultra_raras / total_cartas) * 100)

# D) Determinar el precio promedio por cada tipo de carta
if total_cartas_raras > 0:
    promedio_precio_rara = f"${float(venta_total_cartas_raras / total_cartas_raras)}"
else:
    promedio_precio_rara = "no se vendio ninguna"

if total_cartas_super_raras > 0:
    promedio_precio_super_rara = f"${float(venta_total_cartas_super_raras / total_cartas_super_raras)}"
else:
    promedio_precio_super_rara = "no se vendio ninguna"

if total_cartas_ultra_raras > 0:
    promedio_precio_ultra_rara = f"${float(venta_total_cartas_ultra_raras / total_cartas_ultra_raras)}"
else:
    promedio_precio_ultra_rara = "no se vendio ninguna"

# E) Determinar cual fue el tipo de carta mas vendida
if total_cartas_raras > total_cartas_super_raras and total_cartas_raras > total_cartas_ultra_raras:
    tipo_mas_vendida = "El tipo de carta mas vendida es de tipo: Rara"
elif total_cartas_super_raras > total_cartas_ultra_raras:
    tipo_mas_vendida = "El tipo de carta mas vendida es de tipo: Super Rara"
else:
    tipo_mas_vendida = "El tipo de carta mas vendida es de tipo: Ultra Rara"

print(f"La cantidad de cartas ultra raras vendidas cuyo precio este entre $50.000 y $80.000: {cantidad_ultra_rara_precio_cincuenta}")
if carta_rara_barata > 0:
    print(f"La carta rara de menor precio fue {nombre_carta_rara_barata} y su tipo {tipo_carta_rara_barata}")
else:
    print("No se puede determinar el precio mas bajo de la carta rara vendida ya que no se vendio ninguna")
print(f"el porcentaje de venta de cartas raras es de {porcentaje_cartas_raras}%, super raras es de {porcentaje_cartas_super_raras}% y de ultra raras {porcentaje_cartas_ultra_raras}%")
print(f"El precio promedio de las cartas raras es de {promedio_precio_rara}, el de super raras es de {promedio_precio_super_rara} y el de ultra rara es de {promedio_precio_ultra_rara} ")
print(f"El tipo de carta mas vendida es {tipo_mas_vendida}")

