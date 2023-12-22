import os
import random
from colorama import Fore
from time import sleep

jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vitoria = "n"

velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print(jogarNovamente)


def tela():
    global velha
    os.system("clear")
    global jogadas

    print("     0   1   2    ")
    print("0:  " + velha[0][0] + "  |" + velha[0][1] + "  |" + velha[0][2])
    print("    -----------")
    print("1:  " + velha[1][0] + "  |" + velha[1][1] + "  |" + velha[1][2])
    print("    -----------")
    print("2:  " + velha[2][0] + "  |" + velha[2][1] + "  |" + velha[2][2])

    print("Jogadas:  " + Fore.GREEN + str(jogadas) + Fore.RESET)


def playerTurn():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:

        try:
            linha = int(input("Linha..: "))
            coluna = int(input("Coluna..: "))
            print("Estou aqui")
            while (velha[linha][coluna] != " "):
                linha = int(input("Linha..: "))
                coluna = int(input("Coluna..: "))
            velha[linha][coluna] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha ou coluna inválida")
    sleep(1)


def cpuTurn():
    global jogadas
    global quemJoga
    global vitoria
    global maxJogadas

    if quemJoga == 1 and jogadas < maxJogadas:
        linha = random.randrange(0, 3)
    if quemJoga == 1 and jogadas < maxJogadas:
        coluna = random.randrange(0, 3)

        while velha[linha][coluna] != " ":
            linha = random.randrange(0, 3)
            coluna = random.randrange(0, 3)
        velha[linha][coluna] = "O"
        jogadas += 1
        quemJoga = 2
    sleep(1)


def checkVictory():

    global velha
    vitoria = "n"
    simbolos = ["X","O"]

    print(vitoria)

    for s in simbolos:
        print(s)
        vitoria = "n"

        # verifica linhas
        indiceLinhas = 0
        indiceColunas = 0

        while indiceLinhas < 3:
            soma = 0
            print(soma)
            indiceColunas = 0

            while indiceColunas < 3:
                print(velha[indiceLinhas][indiceColunas])
                if (velha[indiceLinhas][indiceColunas] == s):
                    soma += 1
                indiceColunas += 1

        if (soma == 3):
            vitoria = s
            break
        indiceLinhas += 1

        if (vitoria != "n"):
            break

        # verifica colunas
        indiceLinhas = 0
        indiceColunas = 0

        while indiceColunas < 3:
            soma = 0
            indiceLinhas = 0

            while indiceLinhas < 3:
                if (velha[indiceLinhas][indiceColunas] == s):
                    soma += 1
                indiceLinhas += 1

        if (soma == 3):
            vitoria = s
            break
        indiceColunas += 1

        if (vitoria != "n"):
            break

        # verifica Diagonal esquerda -> direita

        soma = 0
        indiceDiag = 0
        while indiceDiag < 3:
            if (velha[indiceDiag][indiceDiag] == s):
                soma += 1
            indiceDiag += 1

        if (soma == 3):
            vitoria = s
            break

        indiceDiag += 1

        if (vitoria != "n"):
            break

        # verifica Diagonal 2

        soma = 0
        indiceDiagL = 0
        indiceDiagC = 2

        while indiceDiagC >= 0:
            if (velha[indiceDiagL][indiceDiagC] == s):
                soma += 1
            indiceDiagL += 1
            indiceDiagC -= 1
        if (soma == 3):
            vitoria = s
            break

    print(vitoria)

    return vitoria


def redefinir():
    global jogarNovamente
    global jogadas
    global quemJoga
    global maxJogadas
    global vitoria

    jogarNovamente = "s"
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    vitoria = "n"

    global velha
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


while jogarNovamente == "s":
    while True:
        tela()
        playerTurn()
        cpuTurn()

        vit = checkVictory()

        print(vit)

        if vit != "n" or jogadas >= maxJogadas:
            break

    tela()

    print(Fore.RED + "FIm de JOGO" + Fore.YELLOW)

    if vit == "X" or vit == "0":
        print("resultado: Jogador " + vit + " Venceu")
    else:
        print("resultado: Empate")

    jogarNovamente = input(Fore.GREEN + "Jogar nojogarNovamente? [s/n]: " + Fore.RESET)
    redefinir()
