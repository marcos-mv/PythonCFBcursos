# Phonebook system with database

import os
import sqlite3
from sqlite3 import Error
import time


# Database conexion

def ConnectDatabase():
    path = "/home/marcos/agenda"
    con = None

    try:
        con = sqlite3.connect(path)
        print("Conected with database Agenda!")
    except Error as er:
        print(er)
    return con


vcon = ConnectDatabase()


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Operação realizada com sucesso!")
    except Error as er:
        print(er)

    # conexao.close()


def search(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        result = c.fetchall()
        print("Operação realizada com sucesso!")
        return result
    except Error as er:
        print(er)
    # conexao.close()


def menuPrincipal():
    os.system("clear")
    print("1 - Inserir Novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar registro")
    print("4 - Consultar registros")
    print("5 - Consultar registro por Nome")
    print("6 - Encerrar Programa")


def menuInsert():
    os.system("clear")
    print("Inserting new contact!")

    nome = input("Digite o Nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    sql = "INSert INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('" + \
        nome+"','"+telefone+"', '"+email+"')"

    query(vcon, sql)

    time.sleep(2)


def menuDelete():
    os.system("clear")
    print("Deleting contact!")

    id = input("Digite o id do registro a ser deletado: ")

    sql = "DELETE from tb_contatos WHEre (N_IDCONTATO = "+id+")"

    query(vcon, sql)


def menuUpdate():
    os.system("clear")
    print("Updating contact!")

    id = input("Digite o id do registro a ser atualizado: ")

    data = search(vcon, "SELECT * From tb_contatos where N_IDCONTATO="+id)

    dataName = data[0][1]
    dataPhone = data[0][2]
    dataEmail = data[0][3]

    nome = input("Digite o Nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    if (len(nome) == 0):
        nome = dataName
    if (len(telefone) == 0):
        telefone = dataPhone
    if (len(email) == 0):
        email = dataEmail

    sql = "UPDATE tb_contatos SET T_NOMECONTATO = '"+nome+"', T_TELEFONECONTATO = '" + \
        telefone+"', T_EMAILCONTATO='"+email+"'  WHEre N_IDCONTATO = '"+id+"'"

    query(vcon, sql)


def menuSearchAll():    
    os.system("clear")
    print("Searching all Contacts!")

    data = search(vcon, "SELECT * From tb_contatos")
    
    for d in data:
        print(d)
        
    input("\n \nDigite qualquer tecla para voltar ao menu anterior: ")

def menuSearchName():
    os.system("clear")
    print("Searching name!")
    
    nome = input("Digite o nome a ser pesquisado: ")

    data = search(vcon, "SELECT * From tb_contatos WHEre T_NOMECONTATO LIKE '%"+nome+"%'")
    
    for d in data:
        print(d)
        
    input("\n \nDigite qualquer tecla para voltar ao menu anterior: ")


opc = 0
while (opc != 6):
    menuPrincipal()
    opc = int(input("Digite uma opção: "))

    if opc == 1:
        menuInsert()

    elif opc == 2:
        menuDelete()

    elif opc == 3:
        menuUpdate()
    elif opc == 4:
        menuSearchAll()

    elif opc == 5:
        menuSearchName()

    elif opc == 6:
        os.system("clear")
        print("Programa Encerrado!")
        break
    
    elif opc == None:
        os.system("clear")
        menuPrincipal()

    else:
        os.system("clear")
        print("Invalid Option")


vcon.close()

name = input()
