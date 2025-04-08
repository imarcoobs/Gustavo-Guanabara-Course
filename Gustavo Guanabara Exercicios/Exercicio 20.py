import random

nomes = input("Digite o nome dos alunos separado por vírgulas: \n ")
lista = nomes.split(",")
random.shuffle(lista)
print("A ordem de apresentação será:")
print(lista)
