nome = str(input('Me diga o nome do aluno.\n'))
nota1 = float(input('Nota da prova mensal.\n'))
nota2 = float(input('Nota da prova bimestral.\n'))
nota3 = float(input('Nota do trabalho bimestral.\n'))
nota4 = float(input('Nota de participação do aluno.\n'))
notatotal = nota1 + nota2 + nota3 + nota4
media = notatotal / 4
print('A média do aluno {} é {}'.format(nome,media))