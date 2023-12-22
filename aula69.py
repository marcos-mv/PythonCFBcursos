from tkinter import *
import os


path = os.path.dirname(__file__)

def futebol():
    print("Futebol "+str(vFutebol.get()))

def volei():
    print("Vôlei " +str(vVolei.get()))
    
def basquete():
    print("Basquete " +str(vBasquete.get()))

app = Tk()

app.title("Aula 68 Images")
app.geometry("500x500")

vFutebol = BooleanVar()
vVolei = BooleanVar()
vBasquete = BooleanVar()

imgLogo = PhotoImage(file=path+"/aula68.png")

fr_quadro1=Frame(app,borderwidth=1, relief=SUNKEN)
fr_quadro1.place(x=10,y=10, width=400, height=300)

l_logo= Label(fr_quadro1,image=imgLogo)
l_logo.place(x=10, y=10)

cb_futebol = Checkbutton(fr_quadro1,text="Futebol",variable=vFutebol,onvalue=True,offvalue=False, command=futebol)
cb_futebol.pack(side=LEFT)

cb_volei = Checkbutton(fr_quadro1,text="Volei",variable=vVolei,onvalue=True,offvalue=False, command=volei)
cb_volei.pack(side=LEFT)

cb_futebol = Checkbutton(fr_quadro1,text="Basquete",variable=vBasquete,onvalue=True,offvalue=False, command=basquete)
cb_futebol.pack(side=LEFT)

app.mainloop()