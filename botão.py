from tkinter import messagebox
from tkinter import*
from tkinter import ttk
import tkinter as tk

#cores

cor1 = '#3b3b3b'
cor2 = '#333333'
cor3 = '#ffffff'
cor4 = '#fcc058'
cor5 = '#fcc055'


class MinhaGUI:
    def __init__(self):
        # Criamos a janela principal

        self.janela_principal = Tk()

        # Criando os botões

        self.botao_clique_aqui = Button(self.janela_principal, text='Clique aqui', anchor='center', width=10, height=2, font=('Ivi 10 bold'), bg=cor3, command=self.hello_world)
        self.botao_sair = Button(self.janela_principal, text='Sair', width=10, anchor='center', font=('Ivi 10 bold'), bg=cor3, command=self.janela_principal.quit)



        # Empacotando os botões janela principal

        self.botao_clique_aqui.pack()
        self.botao_sair.pack()



        # Rodando

        mainloop()


    def hello_world(self):
        messagebox.showinfo('COMODORO!')
    def abrir_janela(self):
        janela = tk.Toplevel()

    janela = tk.Tk()

    botao = tk.Button(janela, text = 'Ir para nova janela', command = abrir_janela)
    botao.grid(row=0, column=0)

    janela.mainloop()

gui = MinhaGUI()