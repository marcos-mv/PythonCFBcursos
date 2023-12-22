import random

import os

os.system('clear')
tentativas = 1

valor = random.randrange(0,100)

jogador = int(input("Digite um número até acertar: "))

while valor != jogador:
    os.system('clear')
    tentativas += 1
    if (valor > jogador):
        print("O número é maior, tente novamente!")
    elif (valor < jogador):
        print("O número é menor, tente novamente")
    jogador = int(input("Digite um número até acertar: "))
        
        
print("Parabens você acertou em: " + str(tentativas) + " tentativas!")

    

