cateto_oposto = float(input('Me fale o comprimento do cateto oposto de um triângulo retângulo.\n'))
cateto_adjacente = float(input('Me fale o comprimento do cateto adjacente de um triângulo retângulo.\n'))

potencia1 = cateto_adjacente **2
potencia2 = cateto_oposto **2
soma = potencia1 + potencia2
raíz = soma**(1/2)

print('O valor da hipotenusa é igual a {}.'.format(raíz))