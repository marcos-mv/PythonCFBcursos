
x = 10
y = 5


def somar():
    print("Função de Soma!")

    soma = x + y
    
    print ("Soma de " + str(x) + " + "+ str(y)+ " é: " + str(soma))
    
def subtrair():
    print("Função de Subtração!")

    subtracao = x - y
    
    print ("Subtração de " + str(x) + " + "+ str(y)+ " é: " + str(subtracao))


def multiplicar():
    print("Função de multiplicação!")

    multiplicacao = x * y
    
    print ("Multiplicação de " + str(x) + " + "+ str(y)+ " é: " + str(multiplicacao))


def dividir():
    print("Função de Divisão!")

    divisao = x / y
    
    print ("Divisão de " + str(x) + " + "+ str(y)+ " é: " + str(divisao))


def calculos():
    somar()
    subtrair()
    multiplicar()
    dividir()
    
calculos()
