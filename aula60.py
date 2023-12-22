from tkinter import *
import sqlite3
from sqlite3 import Error

import os
 
path = os.path.dirname(__file__)

newform=path+"/aula60NovoContato.py"
 
def addContact():
      print("Entrei")
      exec(open(newform).read(),{'x':10}) 


app = Tk()


app.title("App Marcos")
app.geometry("500x300")
app.configure(background="#dde")

barraDeMenus = Menu(app)

menuContatos = Menu(barraDeMenus,tearoff=OFF)
menuContatos.add_command(label = "Novo Contato", command=addContact)
menuContatos.add_command(label = "Pesquisar", command="addContact")
menuContatos.add_command(label = "Editar", command="addContact")
menuContatos.add_command(label = "Deletar", command="addContact")
menuContatos.add_separator()
menuContatos.add_command(label = "Fechar", command=app.quit)

barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)

menuManutencao = Menu(barraDeMenus,tearoff=OFF)
menuManutencao.add_command(label = "Banco de Dados", command="addContact")

barraDeMenus.add_cascade(label="Manutenção", menu=menuManutencao)

menuSobre = Menu(barraDeMenus,tearoff=OFF)
menuSobre.add_command(label = "Quem Somos Nós", command="addContact")

barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)



app.config(menu=barraDeMenus)
app.mainloop()
