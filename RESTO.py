from tkinter import*
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date


janela = Tk()

janela.title('Software')
janela.geometry('400x200')


label = Label(janela, text='Botão')
label.grid(column=0, row=0)
label.place(x=0, y=20)  # (place) posiciona o botão


def ola():

    label.configure(text='modificar')
    label.grid(column=0, row=0)
    label.place(x=0, y=50)
    label.pack(side=BOTTOM)  # Posicionando a descrição.

botao = Button(janela, text='Janela', bg='white', fg='black', font='Ivi 8 bold', width='15', height='2', command=ola)
botao.grid(column=1, row=0)

botao.place(x=70, y=5)


botao_2 = Button(janela, text='Janela_2', bg='white', fg='black', font='Ivi 8 bold', width='15', height='2', command=ola)
botao_2.grid(column=1, row=0)
botao_2.place(x=70, y=45)
label.pack(side=BOTTOM)



janela.mainloop()
