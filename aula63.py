from tkinter import *

def printSport():
    ve= vesporte.get()
    print(ve)
    
    if ve == "f":
        print("Futebol")
    elif ve == "v":
        print("Vôlei")
    elif ve == "b":
        print("Basquete")
    else:
        print("Selecione um esporte")
        

app = Tk()

app.title("Aula 63 radio Button!")
app.geometry("500x500")

label_esportes = Label(app,text="Esportes")
label_esportes.pack()

vesporte = StringVar()
vcor = StringVar()


radio_button_futebol= Radiobutton(app,text="Futebol",value="f", variable=vesporte )
radio_button_futebol.pack()

radio_button_volei= Radiobutton(app,text="Vôlei",value="v", variable=vesporte )
radio_button_volei.pack()

radio_button_basquete= Radiobutton(app,text="Basquete",value="b", variable=vesporte )
radio_button_basquete.pack()

radio_button_verde= Radiobutton(app,text="Verde",value="green", variable=vcor )
radio_button_verde.pack()

radio_button_azul= Radiobutton(app,text="Azul",value="blue", variable=vcor )
radio_button_azul.pack()

radio_button_amarelo= Radiobutton(app,text="Amarelo",value="Yellow", variable=vcor )
radio_button_amarelo.pack()

btn_esporte = Button(app, text="Esporte Selecionado", command=printSport)
btn_esporte.pack()

app.mainloop()