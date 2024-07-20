lado_menor = input("Medida en CM del lado menor del cometa: ")
lado_mayor = input("Medida en CM del lado mayor del cometa: ")
diagonal_menor = input("Medida en CM del diagonal menor del cometa: ")

lado_menor = float(lado_menor)
lado_mayor = float(lado_mayor)
diagonal_menor = float(diagonal_menor)

diagonal_mayor_uno = ((lado_mayor ** 2) - ((diagonal_menor / 2) ** 2)) ** 0.5
diagonal_mayor_dos = ((lado_menor ** 2) - ((diagonal_menor / 2) ** 2)) ** 0.5
diagonal_mayor = diagonal_mayor_uno + diagonal_mayor_dos

varillas = float((lado_menor * 2 + lado_mayor * 2 + diagonal_mayor + diagonal_menor) / 100)
superficie_cometa = (diagonal_mayor_uno * (diagonal_menor / 2)) + (diagonal_mayor_dos * (diagonal_menor / 2))
superficie_cola = superficie_cometa * 0.1
total_papel = float((superficie_cometa + superficie_cola) / 10000)

varillas_diez = varillas * 10
total_papel_diez = total_papel * 10

print(f"Se necesitan {varillas_diez:.2f} Mts de varillas para la estructura y\n{total_papel_diez:.2f} Mts2 de Papel para construir 10 cometas.")