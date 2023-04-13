from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

def abrir_janela():
	janela2 = tk.Toplevel()
	janela2.geometry('320x220')  # Largura e Comprimento da janela
	janela2.title('janela nova') # Título da janela
	label_nome = tk.Label(janela2, text="Nome:", bg='orange', width=10, height=1, fg='black', relief=FLAT)
	label_nome.grid(row=0, column=0)
	botao_voltar = tk.Button(janela2, text ='Fechar a janela', command=janela2.destroy)
	botao_voltar.grid(row=1, column=0)


janela = tk.Tk()

botao = tk.Button(janela, text = 'Ir para nova janela', command = abrir_janela, width=20, height=1, padx=3, relief='flat', anchor='center', font=('Ivi 15 bold'), bg='white', fg='black')
botao.grid(row=0, column=0) #botão.grid = criação do botão


janela.mainloop()
