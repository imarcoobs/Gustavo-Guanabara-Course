## CALCULAR AUMENTO DE 15% EM SALÁRIO.

nome = str(input('Diga o nome do funcionário que ira receber o aumento de 15% no seu salário.\n'))

salario = int(input('Qual o salário atual do(a) {} ? \n'.format(nome)))
aumento = salario * 0.15
total = aumento + salario

print('{} ira receber {} após o aumento de 15% em seu salário.'.format(nome,total))
