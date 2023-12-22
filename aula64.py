from tkinter import *

def printSport():
    ve= vesporte.get()
    print(ve)
        

app = Tk()

app.title("Aula 64 Option Menu")
app.geometry("500x500")

lista_esportes = ["Futebol", "Vôlei", "Basquete", "Tênis"]

label_esportes = Label(app,text="Esportes")
label_esportes.pack()

vesporte = StringVar()
vesporte.set(lista_esportes[0])#valor Padrão

vcor = StringVar()

op_esportes = OptionMenu(app, vesporte, *lista_esportes)
op_esportes.pack()




btn_esporte = Button(app, text="Esporte Selecionado", command=printSport)
btn_esporte.pack()

app.mainloop()