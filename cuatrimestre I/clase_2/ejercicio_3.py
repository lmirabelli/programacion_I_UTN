# DIVISION 114
# LEONARDO MIRABELLI

# La división de higiene está trabajando en un control de stock para productos sanitarios. 
# Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos: 
# 1. El tipo (validar "barbijo", "jabón" o "alcohol") 
# 2. El precio: (validar entre 100 y 300) 
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades) 
# 4. La marca y el Fabricante. 

# Se debe informar lo siguiente: 


bandera_barbijo = 0
bandera_stock = 0
stock_total_jabon = 0

for i in range(5):
    producto = input("ingresa el producto (barbijo, jabon, alcohol): ")

    while producto != "barbijo" and producto != "jabon" and producto != "alcohol":
        print("el producto seleccionado es incorrecto.")
        producto = input("ingresa el producto (barbijo, jabon, alcohol): ")
    
    precio = int(input(f"ingrese el precio de el {producto}: "))

    while precio < 100 or precio > 300:
        print("el precio no es correcto.")
        precio = int(input(f"ingrese el precio de el {producto}: "))

    stock = int(input(f"ingrese el stock del {producto}: "))

    while stock < 0 or stock > 1000:
        print("el stock no es correcto.")
        stock = int(input(f"ingrese el stock del {producto}: "))
    
    marca = input("ingresa la marca: ")
    fabricante = input("ingresa el fabricante: ")

# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante. 
    if producto == "barbijo":
        if bandera_barbijo == 0:
            precio_barbijo = precio
            stock_barbijo = stock
            fabricante_barbijo = fabricante
            bandera_barbijo = 1
        elif precio_barbijo < precio:
                precio_barbijo = precio
                stock_barbijo = stock
                fabricante_barbijo = fabricante

# B. Del ítem con más unidades, el fabricante. 

    if bandera_stock == 0:
        item_mas_stock = producto
        fabricante_mas_stock = fabricante
        cantidad_mas_stock = stock
        bandera_stock = 1
    elif cantidad_mas_stock > stock:
        item_mas_stock = producto
        fabricante_mas_stock = fabricante
        cantidad_mas_stock = stock

# C. Cuántas unidades de jabones hay en total.

    if producto == "jabon":
        stock_total_jabon += stock

if bandera_barbijo != 0:
    print(f"el stock de los barbijos mas caros es {stock_barbijo} y el fabricante es {fabricante_barbijo}")
else:
    print("no hay stock de barbijos")
print(f"el fabricante del producto con mas stock es {fabricante_mas_stock}")
print(f"la cantidad de jabones es {stock_total_jabon}")