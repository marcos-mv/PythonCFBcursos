from tkinter import *
from tkinter import ttk
import os
import aula82Banco

from tkinter import messagebox


def popular():
    tv.delete(*tv.get_children())
    linhas = aula82Banco.populate()

    for i in linhas:
        tv.insert("", END, values=i)


def insert():
    if var_nome.get() == "" or var_fone.get() == "":
        messagebox.showerror(title="Erro", message="Digite Todos os Dados")
        return
    try:
        aula82Banco.addData(var_nome.get(), var_fone.get())
        tv.insert("", END, values=(var_nome.get(), var_fone.get()))

    except:
        messagebox.showerror(title="Erro", message="Erro ao Inserir")
        return
    popular()
    var_nome.delete(0, END)
    var_fone.delete(0, END)
    var_nome.focus()


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
        tv.delete(*tv.get_children())
        result = aula82Banco.searchData(vnomepesquisar.get())

        for i in result:
            tv.insert("", END, values=i)
    except:
        messagebox.showerror(
            title="Erro", message="Selecione um elemento para ser mostrado.")


path = os.path.dirname(__file__)

app = Tk()

app.title("Agenda com Conexão com Banco")
app.geometry("600x600")

#####

quadroGrid = LabelFrame(app, text="Contatos")
quadroGrid.pack(fill=BOTH, expand=YES, padx=10, pady=10)

tv = ttk.Treeview(quadroGrid, columns=('id', 'nome', 'fone'), show='headings')

tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)

tv.heading('id', text="ID")
tv.heading('nome', text="Nome")
tv.heading('fone', text="Telefone")

tv.pack()
popular()


#########
quadroInserir = LabelFrame(app, text="Inserir novos Contatos")
quadroInserir.pack(fill="both", expand=YES, padx=10, pady=10)

lb_nome = Label(quadroInserir, text="Nome", anchor=CENTER)
lb_nome.pack(side=LEFT)
var_nome = Entry(quadroInserir)
var_nome.pack(side=LEFT, padx=10)

lb_fone = Label(quadroInserir, text="Fone", anchor=CENTER)
lb_fone.pack(side=LEFT)
var_fone = Entry(quadroInserir)
var_fone.pack(side=LEFT, padx=10)


btn_insert = Button(quadroInserir, text="Inserir", command=insert)
btn_insert.pack(side=LEFT, padx=10)

# btn_delete = Button(app, text="Deletar", command=delete)
# btn_delete.grid(column=1, row=4, sticky=W)
# btn_search = Button(app, text="Obter", command=search)
# btn_search.grid(column=2, row=4, sticky=W)


# for id in listNomes:
#     tv.insert("",END,values=id)

#####

quadroPesquisar = LabelFrame(app, text="Pesquisar Contatos")
quadroPesquisar.pack(fill="both", expand=YES, padx=10, pady=10)

lbid = Label(quadroPesquisar, text="Nome")
lbid.pack(side=LEFT)
vnomepesquisar = Entry(quadroPesquisar)
vnomepesquisar.pack(side="left", padx=10)

btn_pesquisar = Button(quadroPesquisar, text="Pesquisar", command=search)
btn_pesquisar.pack(side=LEFT, padx=10)

btn_todos = Button(quadroPesquisar, text="Mostrar Todos", command=popular)
btn_todos.pack(side=LEFT, padx=10)


app.mainloop()
