from tkinter import *
from tkinter import messagebox

def showMessage(type,msg):
    
    if type == "1":
        messagebox.showinfo(title="Aula 65 Message Box", message=msg)
    elif type == "2":
        messagebox.showwarning(title="Aula 65 Message Box", message=msg)
    elif type == "3":
        messagebox.showerror(title="Aula 65 Message Box", message=msg)
        
def resetTB():
    res = messagebox.askyesno("resetar", "Confirma reset do Textbox?")
    #askyesno / askquestion - SIM e NÂO (True e False)
    #askokcancel - ok e cancelar (True e False)
    #askretrycancel - repetir e cancelar (True e False)
    #askyesnocancel - Sim , Não e Cancelar (True, False, None)
    
    
    if (res == True):
        tb_num.delete(0,END)
        tb_num.insert(0,"1")
        
    
vmsg="Curso de Python/Tkinter"

app = Tk()

app.title("Aula 65 Message Box")
app.geometry("500x500")

vnum_cstexto = StringVar()

Label(app,text="Tipo de caixa (1, 2 ou 3)").pack()
tb_num = Entry(app,textvariable=vnum_cstexto)
vnum_cstexto.set(1)
tb_num.pack()

btn_msg = Button(app,text="Mostrar mensagem", command= lambda:showMessage(vnum_cstexto.get(),vmsg))
btn_msg.pack()

btn_reset = Button(app,text="resetar TextBox", command= resetTB)
btn_reset.pack()






app.mainloop()