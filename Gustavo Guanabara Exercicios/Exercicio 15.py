modelo = str(input('Me diga a marca do carro que você alugou.\n'))
dias = int(input("Por quantos dias o carro foi alugado? \n"))  
km = float(input("Quantos km o carro rodou? \n")) 

dias_calculo = dias * 60
km_calculo = km * 0.15
total = dias_calculo + km_calculo

print("O {} custou R${} por {} dias, e custou R${}, pelos km's rodados. No total somando R${}".format(modelo , dias_calculo , dias , km, total ))

