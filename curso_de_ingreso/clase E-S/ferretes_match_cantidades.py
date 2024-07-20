lamparas = 800
porcentaje_descuento = 0

cantidad_comprada = input("Ingrese la cantidad de lamparas a comprar: ")
cantidad_comprada = int(cantidad_comprada)


print("-----------------------------")
print("Marcas disponibles: 1-ArgetninaLuz, 2-FelipeLamparas, 3-Otras")
marca_lampara = input("Elija una marca: ")
marca_lampara = int(marca_lampara)


while marca_lampara < 1 and marca_lampara > 3:
    print("La opcion marcada no existe")
    print("-----------------------------")
    print("Marcas disponibles: 1-ArgentinaLuz, 2-FelipeLamparas, 3-Otras")
    marca_lampara = print("Elija la marca de la lampara con las opciones de arriba: ")
    marca_lampara = int(marca_lampara)


match cantidad_comprada:
        case 6 | _ if cantidad_comprada > 6:
            porcentaje_descuento = 50
        case 5:
            if marca_lampara == "ArgentinaLuz":
                porcentaje_descuento = 40
            else:
                porcentaje_descuento = 30
        case 4:
            if marca_lampara == "ArgentinaLuz" or marca_lampara == "FelipeLamparas":
                porcentaje_descuento = 25
            else:
                porcentaje_descuento = 20
        case 3:
            if marca_lampara == "ArgentinaLuz":
                porcentaje_descuento = 15
            elif marca_lampara == "FelipeLamparas":
                porcentaje_descuento = 10
            else:
                porcentaje_descuento = 5


total_sin_descuentos = lamparas * cantidad_comprada
descuento_total = total_sin_descuentos * porcentaje_descuento / 100
subtotal_pagar = total_sin_descuentos - descuento_total


print("*** MARCA DE LA LAMPARA ***")
if marca_lampara == 1:
    print("ArgentinaLuz")
elif marca_lampara == 2:
    print("FelipeLamparas")
else:
    print("Otra Marca")

print(f"Cantidad de lamparas: {cantidad_comprada}")
print(f"Subtotal: ${total_sin_descuentos}")
print(f"Descuento por cantidad y marca: ${descuento_total} ({porcentaje_descuento}%)")

descuento_adicional = 0
if subtotal_pagar > 4000:
    porcentaje_adicional = 5
    descuento_adicional = subtotal_pagar * porcentaje_adicional / 100
    print(f"Descuento adicional: ${descuento_adicional} ({porcentaje_adicional}%)")

total_pagar = subtotal_pagar - descuento_adicional

print(f"total: ${total_pagar}")
