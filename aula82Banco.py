from tkinter import *
import sqlite3
from sqlite3 import Error

import os


def ConnectDatabase():
    path = "/home/marcos/agenda2"
    con = None

    try:
        con = sqlite3.connect(path)
        print("Conectado")
    except Error as er:
        print(er)
    return con


vcon = ConnectDatabase()

# dql (Data Query Language - is the sublanguage responsible for reading, or querying, data from a database. In SQL, this corresponds to the SELECT )


def dql(query):
    vcon = ConnectDatabase()
    c = vcon.cursor()
    c.execute(query)
    result = c.fetchall()

    vcon.close()

    return result

# Data Manipulation Language (DML) - The Data Manipulation Language is the sublanguage responsible for adding, editing or deleting data from a database. In SQL, this corresponds to the INSERT, UPDATE, and DELETE


def dml(query):
    try:
        vcon = ConnectDatabase()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()

    except Error as er:
        print(er)


def addData(nome, fone):
    sql = "INSErt into TB_AGENDA(NOME, TELEFONE) VALUES ('" + \
        nome+"','"+fone+"')"
    dml(sql)


def updateData(id, nome, fone):
    sql = "UPDATE TB_AGENDA SET (NOME, TELEFONE) VALUES ('" + \
        nome+"','"+fone+"') Where N_IDCONTATO = '"+id+"'"
    dml(sql)


def deleteData(id):
    sql = "DELETE from TB_AGENDA WHere ID = '"+id+"'"
    dml(sql)


def searchData(nome):
    sql = "SELECT * From TB_AGENDA WHEre NOME LIKE '%"+nome+"%' Order BY ID"
    result = dql(sql)
    return result


def populate():
    sql = "SELECT * From TB_AGENDA order BY ID"
    result = dql(sql)
    return result
