from tkinter import *
import os

def scalaValue():
    print("Valor da Escala: "+ str(sc_escala.get()))

path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 72 Images")
app.geometry("500x500")

lb_valor = Label(app,text="Valor")
lb_valor.pack()

sc_escala = Scale(app,from_=0, to=100, orient=HORIZONTAL)
sc_escala.set(0)
sc_escala.pack()

sc_escala2 = Scale(app,from_=0, to=100, orient=VERTICAL)
sc_escala2.set(0)
sc_escala2.pack()

btn_value = Button(app,text="Valor da Escala", command=scalaValue)
btn_value.pack()



app.mainloop()