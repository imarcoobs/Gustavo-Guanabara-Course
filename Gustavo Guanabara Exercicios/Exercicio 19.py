import random

aluno1 = str(input('Me diga o nome do aluno número 1: \n'))
aluno2 = str(input('Me diga o nome do aluno número 2: \n'))
aluno3 = str(input('Me diga o nome do aluno número 3: \n'))
aluno4 = str(input('Me diga o nome do aluno número 4: \n'))

numero = random.randint(1,4)

print('O aluno sorteado foi o número {}'.format(numero))
