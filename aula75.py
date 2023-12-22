from tkinter import *
import os

def printValue():
    print("Valor SpinBox: "+ str(sb_values.get()))
    

    

path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 75 List Box")
app.geometry("500x500")

# sb_values = Spinbox(app,from_= 0, to=10)

sb_values = Spinbox(app,values=(0,1,2,3,4,5))

sb_values.pack()

btn_value = Button(app, text="Imprimir Valor", command=printValue)
btn_value.pack()



app.mainloop()