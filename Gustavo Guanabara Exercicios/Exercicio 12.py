carro_nome = str(input('Me diga o nome do carro que você deseja comprar.\n'))
carro_valor = float(input('Me diga o preço do carro que você deseja comprar.\n'))
desconto = 5 * carro_valor
desconto2 = desconto/100
desconto3 = carro_valor - desconto2
print('O carro {} , com o desconto de 5% ira sair por {}.'.format(carro_nome , desconto3))