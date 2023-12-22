from tkinter import *
import os


def showPassword():
    print("Senha Digitada: "+vsenha.get())

path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 68 Images")
app.geometry("500x500")

vsenha = StringVar()

p_senha = Entry(app,textvariable=vsenha,show="*")
p_senha.pack()

btn_mostraSenha=Button(app,text="Mostrar Senha", command=showPassword)
btn_mostraSenha.pack()




app.mainloop()