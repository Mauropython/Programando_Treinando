from tkinter import*
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date


janela = Tk() # Formação da janela
janela.title('Calculadora de idade') # Título da janela
janela.geometry('310x400') # Largura e Comprimento da janela (310x400)

#cores

cor1 = '#3b3b3b'
cor2 = '#333333'
cor3 = '#ffffff'
cor4 = '#fcc058'
cor5 = '#fcc055'

#Criando Frames (Quadros)

frame_cima = Frame(janela, width=310, height=120, pady=0, padx=4, relief=FLAT)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=310, pady=0, padx=0, relief=FLAT) # width=largura laterais, height= altura abas.
frame_baixo.grid(row=1, column=0) # row= linha, column= coluna

#Criando labels (rótulos) para frente e para cima / label serve para editar a janela do programa a ser feito

calculadora = Label(frame_cima, text='CALCULADORA', width=25, height=1,padx=3, relief='flat', anchor='center', font=('Ivi 15 bold'), bg=cor2, fg=cor3)
calculadora.place(x=0, y=30)  #fg = cor do fundo, bg = cor da letra

idade = Label(frame_cima, text='DE IDADE', width=11, height=1,padx=0, relief='flat', anchor='center', font=('Arial 35 bold'), bg=cor2, fg=cor4)
idade.place(x=0, y=70)

tempo = Label(frame_baixo, text='TEMPO', width=11, height=1, padx=2, relief='flat', anchor='center', font=('Arial 35 bold'), fg=cor1)
tempo.place(x=0, y=80)

#Criando a função calcular idade


def calcular():
    inicial = calendario1.get()
    termino = calendario2.get()


    #Separando os valores

    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]
    data_inicial = date(ano_1, mes_1, dia_1)

    #Convertendo os valores em formato date/datetime

    mes_2, dia_2, ano_2 = [int(f) for f in termino.split('/')]
    data_nascimento = date(ano_2, mes_2, dia_2)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    app_anos['text'] = anos
    app_meses['text'] = meses
    app_dias['text'] = dias


    #print(inicial, termino)

#Criando labels para frame baixo

idade_inicial = Label(frame_baixo, text='Data inicial', height=1, padx=0, pady=0, relief='flat', anchor='nw', font=('Ivi 11'), bg=cor1, fg=cor3)
idade_inicial.place(x=40, y=30)

calendario1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='mm/dd/y', y=2023)
calendario1.place(x=180, y=30)



data_nascimento = Label(frame_baixo, text='Data de nascimento', height=1, padx=0, pady=0, relief='flat', anchor='nw', font=('Ivi 11'), bg=cor1, fg=cor3)
data_nascimento.place(x=40, y=60)

calendario2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='mm/dd/y', y=2023)
calendario2.place(x=180, y=30)

app_anos = Label(frame_baixo, text='--', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 25 bold'), bg=cor1, fg=cor3)
app_anos.place(x=60, y=135)
app_anos_nome = Label(frame_baixo, text='Anos', height=1, padx=0, pady=0, relief='flat', anchor='nw', font=('Ivi 11 bold'), bg=cor1, fg=cor3)
app_anos_nome.place(x=60, y=175)

app_meses = Label(frame_baixo, text='--', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 25 bold'), bg=cor1, fg=cor3)
app_meses.place(x=140, y=135)
app_meses_nome = Label(frame_baixo, text='Meses', height=1, padx=0, pady=0, relief='flat', anchor='nw', font=('Ivi 11 bold'), bg=cor1, fg=cor3)
app_meses_nome.place(x=140, y=175)

app_dias = Label(frame_baixo, text='--', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 25 bold'), bg=cor1, fg=cor3)
app_dias.place(x=220, y=135)
app_dias_nome = Label(frame_baixo, text='Dias', height=1, padx=0, pady=0, relief='flat', anchor='nw', font=('Ivi 11 bold'), bg=cor1, fg=cor3)
app_dias_nome.place(x=220, y=175)


#Criando botão calcular

botao_calcular = Button(frame_baixo, command=calcular, text='Calcular',width=20, height=1, relief='raised', overrelief='ridge', font=('Ivi 10 bold'), bg=cor1, fg=cor3)
botao_calcular.place(x=70, y=225)

janela.mainloop() # Loop infinito da janela
