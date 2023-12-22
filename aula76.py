from tkinter import *
from tkinter import ttk
import os
    
path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 75 Notebook")
app.geometry("500x500")


notebook = ttk.Notebook(app)
notebook.place(x=0, y=0, width=500, height=300)

tab1 = Frame(notebook)
notebook.add(tab1,text="Aba 1")

tab2 = Frame(notebook)
notebook.add(tab2,text="Aba 2")

tab3 = Frame(notebook)
notebook.add(tab3,text="Aba 3")

lb1= Label(tab1, text="Label da Primeira Aba")
lb1.pack()

lb2= Label(tab2, text="Label da Segunda Aba")
lb2.pack()

lb3= Label(tab3, text="Label da Terceira Aba")
lb3.pack()




app.mainloop()