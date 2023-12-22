from tkinter import *
from tkinter import ttk
import os

def valueBar(m):
    i = 0
    etapas = m/100
    
    while i < etapas:
        i += 1 
        j=0
        
        while j< 1000000:
            j+=1
        varBarra.set(i)
        app.update()
    
path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 77 ProgressBar")
app.geometry("500x500")

varBarra = DoubleVar()
varBarra.set(0)


pb = ttk.Progressbar(app,variable=varBarra, maximum=100)
pb.place(x=0, y=0, width=500, height=40)

btn = Button(app, text="Definir Barra", command=lambda:valueBar(10000))
btn.place(x=200,y=60)






app.mainloop()