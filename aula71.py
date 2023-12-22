from tkinter import *
import os

from tkinter import ttk

def printSport():
    print(cb_sports.get())

path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 68 Images")
app.geometry("500x500")


sportsList = ["Futebol", "Vôlei", "Basquete", "Boxe"]

lb_sports = Label(app,text = "Esportes")
lb_sports.pack()

cb_sports = ttk.Combobox(app,values=sportsList , state="readonly")
# cb_sports.set("Futebol")
cb_sports.pack()

btn_sport = Button(app,text="Esporte Selecionado", command=printSport)
btn_sport.pack()


app.mainloop()