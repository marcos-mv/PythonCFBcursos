import os

def somar(x,y):
    print("Função de Soma!")

    soma = x + y
    
    print ("Soma de " + str(x) + " + "+ str(y)+ " é: " + str(soma)+ "\n")
    
def subtrair(x,y):
    print("Função de Subtração!")

    subtracao = x - y
    
    print ("Subtração de " + str(x) + " + "+ str(y)+ " é: " + str(subtracao)+ "\n")


def multiplicar(x,y):
    print("Função de multiplicação!")

    multiplicacao = x * y
    
    print ("Multiplicação de " + str(x) + " + "+ str(y)+ " é: " + str(multiplicacao) + "\n")


def dividir(x,y):
    print("Função de Divisão!")

    divisao = x / y
    
    print ("Divisão de " + str(x) + " + "+ str(y)+ " é: " + str(divisao)+ "\n")


def calculos(x,y):
    os.system("clear")
    somar(x,y)
    subtrair(x,y)
    multiplicar(x,y)
    dividir(x,y)
    
calculos(10,33)

def texto(*n):
    # print(n[0])
    # print(n[1])
    # print(n[2])
    
    for i in n:
        print(i)
    
texto("Casa", "dos", "artistas", "sbt")


def somar1(*num):
    res = 0
    for i in num:
        res += i
    
    print("resultado: " + str(res))
    
somar1(1,2,3,4,5,6,7,8,9,10)

def carros(c="Fox"):
    print("Modelo: " + c)
        

carros("Uno")

def subtrair1(num):
    res = 0
    
    for i in num:
        res -= i
    print("Subtração: " + str(res))
    
lista = [1,2,5,8,33]

subtrair1(lista)