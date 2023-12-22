from tkinter import *
import os

def scalaValue():
    print("Valor da Escala: "+ str(sc_escala.get()))

path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 73 Label Frame")
app.geometry("500x500")

lb_sports = LabelFrame(app,text="Esportes", borderwidth=1, relief="groove")
lb_sports.place(x=10,y=10,width=300, height=100)

l_sport1 = Label(lb_sports, text="Futebol")
l_sport1.pack()

l_sport2 = Label(lb_sports, text="Vôlei")
l_sport2.pack()

l_sport3 = Label(lb_sports, text="Basquete")
l_sport3.pack()


app.mainloop()