from tkinter import *
from tkinter import ttk
import os

from tkinter import messagebox


def insert():
    if var_id.get() == "" or var_nome.get() == "" or var_fone.get() == "":
        messagebox.showerror(title="Erro", message="Digite Todos os Dados")
        return
    tv.insert("", END, values=(var_id.get(), var_nome.get(), var_fone.get()))
    var_id.delete(0, END)
    var_nome.delete(0, END)
    var_fone.delete(0, END)
    var_id.focus()


def delete():

    try:
        itemSelecionado = tv.selection()[0]
        res = messagebox.askyesno(
            "Excluir", "Confirma exclusão do item selecionado?")
        if res == True:
            tv.delete(itemSelecionado)
    except:
        messagebox.showerror(
            title="Erro", message="Selecione um elemento para ser deletado.")


def search():
    try:

        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado, "values")
        print("Id: "+valores[0])
        print("Nome: "+valores[1])
        print("Id: "+valores[2])
    except:
        messagebox.showerror(
            title="Erro", message="Selecione um elemento para ser mostrado.")


path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 80 Crud treeview")
app.geometry("600x500")

lb_id = Label(app, text="Id", anchor=CENTER)
var_id = Entry(app)

lb_nome = Label(app, text="Nome", anchor=CENTER)
var_nome = Entry(app)

lb_fone = Label(app, text="Fone", anchor=CENTER)
var_fone = Entry(app)

tv = ttk.Treeview(app, columns=('id', 'nome', 'fone'), show='headings')

tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)

tv.heading('id', text="ID")
tv.heading('nome', text="Nome")
tv.heading('fone', text="Telefone")

btn_insert = Button(app, text="Inserir", command=insert)
btn_insert.grid(column=0, row=4, sticky=W)
btn_delete = Button(app, text="Deletar", command=delete)
btn_delete.grid(column=1, row=4, sticky=W)
btn_search = Button(app, text="Obter", command=search)
btn_search.grid(column=2, row=4, sticky=W)

lb_id.grid(column=0, row=0, sticky=W)
var_id.grid(column=0, row=1, sticky=W)

lb_nome.grid(column=1, row=0, sticky=W)
var_nome.grid(column=1, row=1, sticky=W)

lb_fone.grid(column=2, row=0, sticky=W)
var_fone.grid(column=2, row=1, sticky=W)

tv.grid(column=0, row=3, columnspan=3, pady=5)

# for id in listNomes:
#     tv.insert("",END,values=id)


app.mainloop()
