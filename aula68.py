from tkinter import *
import os


path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 68 Images")
app.geometry("500x500")

imgLogo = PhotoImage(file=path+"/aula68.png")

l_logo= Label(app,image=imgLogo)
l_logo.place(x=10, y=10)


app.mainloop()