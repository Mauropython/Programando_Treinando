from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import showinfo
from calendar import month_name


cor1 = '#000000' # black
cor2 = '#feffff' # white
cor3 = '#0074eb' #blue
cor4 = 'red'
cor5 = '#000080'
cor6 = 	'#00008B' #darkblue
cor7 = '#696969'
cor8 = '#D8BFD8'
"""
combo = Combobox(janela)
combo.grid(row=0, column=0)
combo['values']= (1,2,3,4)
combo.current(0)
"""
janela = Tk()
janela.title('Python Treinamentos')
janela.geometry('300x300')
janela.configure(background=cor8)
janela.resizable(width=True, height=True) # Reposicionamento da janela principal e bloqueio do maximizar

app_nome_frame = Frame(janela, width=400, height=30, bg=cor3, relief='flat')
app_nome_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

mostrar_frame_frame = Frame(janela, width=400, height=30, bg=cor6, relief='flat')
mostrar_frame_frame.grid(row=1, column=0, columnspan=4, sticky=NSEW)

mostrar_frame_frame2 = Frame(janela, width=400, height=30, bg=cor4, relief='flat')
mostrar_frame_frame2.grid(row=2, column=0, columnspan=5, sticky=NSEW)

mostrar_frame_frame3 = Frame(janela, width=400, height=30, bg=cor1, relief='flat')
mostrar_frame_frame3.grid(row=3, column=0, columnspan=6, sticky=NSEW)
# PArei aqui
app_nome = Label(app_nome_frame, text='1', width=20, height=3, pady=10, relief='flat', anchor=NW, font=('Helvetica 25 bold'), bg=cor7, fg=cor8)
app_nome.grid(row=0, column=0, pady=5)


nome = Entry(janela, width=20)
nome.grid(row=0, column=1)
label_nome = Label(janela, text='Nome:')
label_nome.grid(row=0,column=0)

idade = Entry(janela, width=20)
idade.grid(row=1, column=1)
label_idade = Label(janela, text='Idade:')
label_idade.grid(row=1,column=0)

pais = Entry(janela, width=20)
pais.grid(row=2, column=1)
label_pais = Label(janela, text='País:')
label_pais.grid(row=2,column=0)

ano = Entry(janela, width=20)
ano.grid(row=3, column=1)
label_ano = Label(janela, text='Ano:')
label_ano.grid(row=3,column=0)



#Criação de botões e cores

vermelha = Button(janela, text = 'vermelha', fg = 'red', height= 1, width= 10,)
#vermelha.pack(side = TOP) # botão na parte superior
vermelha.grid(row=0, column=2) #posições das colunas

amarela = Button(janela, text = 'amarela', fg = 'yellow', height= 1, width= 10)
#amarela.pack(side = LEFT)# botão na parte esquerda
amarela.grid(row=1, column=2)

verde = Button(janela, text = 'verde', fg = 'green', height= 1, width= 10)
#verde.pack(side = RIGHT)# botão na parte direita
verde.grid(row=2, column=2)


azul = Button(janela, text = 'azul', fg = 'blue', height= 1, width= 10)
#azul.pack(side = BOTTOM)# botão na parte de baixo
azul.grid(row=3, column=2)


def test():

    n = nome.get()
    i = idade.get()
    p = pais.get()
    a = ano.get()

    label = Label(janela, text=n + '' + i + '' + p + '' + a)
    label.grid(row=5, column=0)

    print(n, i, p, a)

b = Button(janela, text='Cadastrar', bg='white', command=test) #bg muda a cor do botão
b.grid(row=4, column=0)


janela.mainloop()