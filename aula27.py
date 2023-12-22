import os
import time

carros = []


class Carro:
    nome = ""
    potencia = 0
    cor = ""
    marca = ""
    estado = False

    def __init__(self, nome, potencia, cor, marca):

        self.nome = nome
        self.potencia = potencia
        self.marca = marca

        self.velMax = int(potencia)*2

        self.estado = False

        self.cor = cor

    def ligar(self):
        self.estado = True

    def desligar(self):
        self.desligar = False

    def info(self):
        print("Nome ... " + self.nome)
        print("Potencia ... " + str(self.potencia))
        print("Cor ... " + self.cor)
        print("Marca ... " + self.marca)
        print("Estado de Funcionamento ... " + "Ligado" if self.estado else "Estado de Funcionamento ... Desligado")
        print("Velocidade Máxima ... " + str(self.velMax))

        input("Pressione algo para voltar ao menu")


def Menu():
    os.system("clear")

    print('1 - Adicionar novo carro')
    print('2 - Informações de carro')
    print('3 - Excluir carro')
    print('4 - Ligar carro')
    print('5 - Desligar carro')
    print('6 - Listar carros')
    print('7 - Sair')

    print('Quantidade de carros: ' + str(len(carros)))

    opc = input("Digite uma opção: ")

    return int(opc)


def adicionarCarro():
    os.system("clear")

    nome = input("Nome do carro: ")
    potencia = input("Potencia do carro: ")
    cor = input("Cor : ")
    marca = input("Marca: ")

    newCarro = Carro(nome, potencia, cor, marca)

    carros.append(newCarro)

    print("Carro adicionado com sucesso!")

    time.sleep(1)


def informacoes():

    os.system("clear")
    num = input(
        "Informe o número do veiculo que deseja verificar as informações:   ")

    try:
        carros[int(num)].info()
    except:
        print("Carro não existe na lista!")
        time.sleep(10)


def excluirCarro():

    os.system("clear")
    num = input("Informe o número do veiculo que deseja excluir:   ")

    try:
        del carros[int(num)]
    except:
        print("Carro não existe na lista!")
        time.sleep(1)


def ligarCarro():

    os.system("clear")
    num = input("Informe o número do veiculo que deseja Ligar:   ")

    try:
        carros[int(num)].ligar()
        print("Carro ligado")
        time.sleep(1)
    except:
        print("Carro não existe na lista!")
        time.sleep(1)


def desligarCarro():

    os.system("clear")
    num = input("Informe o número do veiculo que deseja Desligar:   ")

    try:
        carros[int(num)].ligar()
        print("Carro Desligado")
        time.sleep(1)
    except:
        print("Carro não existe na lista!")
        time.sleep(1)


def listarCarros():

    os.system("clear")

    p = 0

    for i in carros:
        print( str(p) + " - " + i.nome)
        p += 1
    input("Aperte qualquer tecla para voltar ao Menu")


ret = Menu()

while ret < 7:
    if ret == 1:
        adicionarCarro()
    elif ret == 2:
        informacoes()
    elif ret == 3:
        excluirCarro()
    elif ret == 4:
        ligarCarro()
    elif ret == 5:
        desligarCarro()
    elif ret == 6:
        listarCarros()
    ret = Menu()

os.system("clear")

print("Programa Finalizado")



