from tkinter import *
from tkinter import ttk
import os
    
path = os.path.dirname(__file__)

app = Tk()

app.title("Aula 79 TreeView")
app.geometry("600x500")

listNomes = [['0','Marcos','1111'],['1','Maria','2222'],['2','Ana','3333']]

tv = ttk.Treeview(app,columns=('id','nome','fone'), show='headings')

tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=250)
tv.column('fone',minwidth=0,width=100)

tv.heading('id',text="ID")
tv.heading('nome',text="Nome")
tv.heading('fone',text="Telefone")

# for id in listNomes:
#     tv.insert("",END,values=id)
    
for id, nome, fone in listNomes:
    tv.insert("",END,values=(id,nome,fone))
    

tv.pack()








app.mainloop()