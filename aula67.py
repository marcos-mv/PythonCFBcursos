from tkinter import *
from tkinter import messagebox

def showMessage():
        messagebox.showinfo(title="Aula 65 Message Box", message="Curso de python Tkinter")
        

        
    
vmsg="Curso de Python/Tkinter"

app = Tk()

app.title("Aula 65 Message Box")
app.geometry("500x500")

vnum_cstexto = StringVar()

fr_quadro1=Frame(app, borderwidth=1, relief="raised")  #relief (flat,raised,sunken, solid)
fr_quadro1.place(x=10,y=10, width=300, height=100)

lb_tipo = Label(fr_quadro1,text="Tipo de caixa (1, 2 ou 3)")
lb_tipo.place(x=10,y=10)
tb_num = Entry(fr_quadro1,textvariable=vnum_cstexto)
vnum_cstexto.set(1)
tb_num.place(x=10,y=30)

btn_msg = Button(fr_quadro1,text="Mostrar mensagem", command= lambda:showMessage())
btn_msg.place(x=10, y=50)


fr_quadro2=Frame(app, borderwidth=1, relief="sunken", background="Blue")  #relief (flat,raised,sunken, solid)
fr_quadro2.place(x=10,y=120, width=300, height=100)

lb_canal = Label(fr_quadro2,text="Marcos Aula 67",background="Blue", foreground="white", font=("Arial", 20))
lb_canal.pack(side=LEFT,fill=X,expand=True)

# btn_msg2 = Button(fr_quadro2,text="Mostrar mensagem", command= lambda:showMessage())
# btn_msg2.place(x=10, y=60)

# btn_reset = Button(app,text="resetar TextBox", command= resetTB)
# btn_reset.pack()


app.mainloop()