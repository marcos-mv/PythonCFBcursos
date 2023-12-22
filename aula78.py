from tkinter import *
from tkinter import ttk
import os
    
path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 78 grid")
app.geometry("500x500")

lb_Cadastro = Label(app, text="Cadastro")
lb_Nome = Label(app, text="Digite seu Nome: ")
et_Nome = Entry(app)

lb_Idade = Label(app, text="Digite sua idade")
et_idade = Entry(app)

btn = Button(app, text="Cadastre")


lb_Cadastro.grid(column=0,row=0, columnspan=3, pady=15)

lb_Nome.grid(column=0,row=1,sticky='w')

et_Nome.grid(column=0,row=2,padx=5)

lb_Idade.grid(column=0, row=3)

et_idade.grid(column=0,row=4)



app.mainloop()