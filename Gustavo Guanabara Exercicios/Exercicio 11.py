largura = float(input("Largura da parede em metros \n"))
altura = float(input("Altura da parede em metros \n"))

area = largura * altura
litros_tinta = area / 2

print("Área: {}m²".format(area))
print("Tinta necessária: {}L".format(litros_tinta))