from tkinter import *
import sqlite3
from sqlite3 import Error

import os

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

#dql (Data Query Language - is the sublanguage responsible for reading, or querying, data from a database. In SQL, this corresponds to the SELECT )

def dql(query):
    vcon = ConnectDatabase()
    c = vcon.cursor()
    c.execute(query)
    result = c.fetchall()
    
    vcon.close()
    
    return result

#Data Manipulation Language (DML) - The Data Manipulation Language is the sublanguage responsible for adding, editing or deleting data from a database. In SQL, this corresponds to the INSERT, UPDATE, and DELETE

def dml(query):
    try:
        vcon = ConnectDatabase()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
        
    except Error as er:
        print(er)
    

def addData(nome,fone,email,obs):
    sql = "INSErt into TB_CONTATOS(T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_OBS) VALUES ('"+nome+"','"+fone+"','"+email+"','"+obs+"')"
    dml(sql)
    
def updateData(id,nome,fone,email,obs):
    sql = "UPDATE TB_CONTATOS SET (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_OBS) VALUES ('"+nome+"','"+fone+"','"+email+"','"+obs+"') Where N_IDCONTATO = '"+id+"'"
    dml(sql)
    
def deleteData(id):
    sql = "DELETE from TB_CONTATOS WHere ID = '"+id+"'"
    dml(sql)

def searchData():
    sql = ""
    dql(sql)
    
def searchDataByID(id):
    sql = "SELECT * From TB_CONTATOS WHEre N_IDCONTATO = '"+id+"'"
    dql(sql)
    
    
    