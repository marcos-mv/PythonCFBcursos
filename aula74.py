from tkinter import *
import os

def printCar():
    print("Carro Selecionado: "+ str(lb_carros.get(ACTIVE)))
    
def addCar():
    if vNewCar !='':
        lb_carros.insert(END,vNewCar.get())
    

path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 74 List Box")
app.geometry("500x500")

ListaCarros = ['Gol', "Polo", "Fusca", "Uno"]

lb_carros = Listbox(app)

for carro in ListaCarros:
    lb_carros.insert(END,carro)
    
lb_carros.pack()

btn_selectCar = Button(app, text="Carro Selecionado", command=printCar)
btn_selectCar.pack()

vNewCar= Entry(app)
vNewCar.pack()

btn_selectCar = Button(app, text="Inserir Carro na Lista", command=addCar)
btn_selectCar.pack()


app.mainloop()