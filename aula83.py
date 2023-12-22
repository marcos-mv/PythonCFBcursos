from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

path = os.path.dirname(__file__)

def createPDF():
    try:
        
        cnv = canvas.Canvas(path+"/aulaPdfMarcos.pdf",pagesize=A4)
        cnv.drawString(100,100,"Teste de Criação PDF")
        cnv.save()
    except:
        messagebox.showerror(title="Erro", message="Erro ao criar PDF")
        return
    
    messagebox.showinfo(title="Ação",   message="PDF criado com sucesso!")    
    

app = Tk()

app.title("Aula 83 PDFS")
app.geometry("500x500")

btn_criarPDF = Button(app,text="Criar PDF", command=createPDF)
btn_criarPDF.pack(side="left", padx=10)

app.mainloop()