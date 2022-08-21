from art import logo
import os

#imprimir a logo
print(logo)

#inicializar a lista de lances
lances = {}

#variavel flag para manter o loop
ativo = 1

#loop para registrar os lances
while ativo == 1:
    #perguntar o nome e o lance
    nome = str(input("Entre com o nome: "))
    lance = float(input("Entre com o valor do lance: "))
    os.system('cls')

    #registrar o lance
    lances[nome] = lance

    #perguntar se há outro lance ou não
    HaOutro = input("Há outro lance para ser feito? (S/N): ")
    HaOutro = HaOutro.lower()
    if HaOutro != 's':
        ativo = 0

    #variaveis flag para identificar e guardar o maior lance
    NomeDoMaior = ''
    maiorLance = 0

    #loop para percorrer os lances
    for registro in lances:
        #checando se o lance é o maior, se for, armazena o nome
        if lances[registro] > maiorLance:
            maiorLance = lances[registro]
            nomeDoMaior = lances[registro] 

    if ativo == 0:
        print("O maior lance foi de %.2f R$" % maiorLance)








