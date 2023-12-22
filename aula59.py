from tkinter import *

import os



path = os.path.dirname(__file__)

nameFile = path+"/aula59.txt"

print(nameFile)

def exportData():
    file = open(nameFile,"a")
    file.write("Nome: %s" %vnome.get())
    file.write("\nTelefone: %s" %vfone.get())
    file.write("\nE-mail: %s" %vemail.get())
    file.write("\nOBS: %s" %vobs.get("1.0",END))
    file.write("\n")
    file.close()
    

def printData():
    print("Nome: %s" %vnome.get())
    print("Telefone: %s" %vfone.get())
    print("E-mail: %s" %vemail.get())
    print("OBS: %s" %vobs.get("1.0",END))
    

app = Tk()


app.title("App Marcos")
app.geometry("500x300")
app.configure(background="#dde")

Label(app, text="Nome", background="green", foreground="#009",
      anchor="w").place(x=10, y=10, width=100, height=20)
vnome = Entry(app)
vnome.place(x=10, y=30, width=200, height=20)

Label(app, text="Telefone", background="green", foreground="#009",
      anchor="w").place(x=10, y=60, width=100, height=20)
vfone = Entry(app)
vfone.place(x=10, y=80, width=200, height=20)

Label(app, text="E-mail", background="green", foreground="#009",
      anchor="w").place(x=10, y=110, width=100, height=20)
vemail = Entry(app)
vemail.place(x=10, y=130, width=200, height=20)

Label(app, text="OBS", background="green", foreground="#009",
      anchor="w").place(x=10, y=160, width=100, height=20)
vobs = Text(app)
vobs.place(x=10, y=180, width=200, height=80)

Button(app,text="Salvar", command=exportData).place(x=10,y=270,width=100,height=20)

app.mainloop()
