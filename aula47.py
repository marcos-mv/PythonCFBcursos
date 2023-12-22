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

#Create Table

vsql = """CREATE TABLE TB_CONTATOS(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR (30),
            T_TELEFONECONTATO VARCHAR (14),
            T_EMAILCONTATO VARCHAR(30)
            );"""
            
def createTable(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela Criada com Sucesso!")
        
    except Error as er:
        print(er)
    
createTable(vcon,vsql)

vcon.close()
    