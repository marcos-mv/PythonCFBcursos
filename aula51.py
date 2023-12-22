import sqlite3

from sqlite3 import Error

#Creating Conexion

def ConnectDatabase():
    path = "/home/marcos/agenda"
    con = None
    
    try:
        con = sqlite3.connect(path)
        print("Conectado")
    except Error as er:
        print(er)
    return con

vcon=ConnectDatabase()

#Insert data

def insertData(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("registro Inserido!!")
        
    except Error as er:
        print(er)
        
#Delete data

def deleteData(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("registro removido!!!")
    except Error as er:
        print(er)
        
dsql = "DELETE From TB_CONTATOS WHEre N_IDCONTATO = 8"

# deleteData(vcon,dsql)        


# Update Data
def updateData(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("registro atualizado")
        
    except Error as er:
        print(er)
        
usql = "UPDATE TB_CONTATOS SET T_NOMECONTATO ='Samantha', T_TELEFONECONTATO = '9999999', T_EMAILCONTATO = 'samantha@gmail.com'  where N_IDCONTATO = 3"
        
updateData(vcon, usql)


cont = "s"

while(cont == "s"):
    

    name = input("Digite o nome: ")
    phone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    vsql = "INSErt INTO TB_CONTATOS(T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES('"+name+"', '"+phone+"', '"+email+"');"
    
    insertData(vcon,vsql)
    
    cont = input("Deseja continuar s/n ?: ")
    
    if cont == "s":
        pass
    else:
        print("Programa Encerrado.")
        break
        


vcon.close()
    