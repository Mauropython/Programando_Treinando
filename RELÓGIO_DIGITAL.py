"""
operator = input('Digite a operação desejada:(+, -, *, /, %, //)')
n1 = (input('Digite o primeiro número:'))
n2 = (input('Digite o segundo número:'))
n3 = (input('Digite o terceiro número:'))
n4 = (input('Digite o quarto número:'))

if operator == '+':
    operator = int(n1) + int(n2) + int(n3) + int(n4)
elif operator == '-':
    operator = int(n1) - int(n2) - int(n3) - int(n4)
elif operator == '*':
    operator = int(n1) * int(n2) * int(n3) * int(n4)
elif operator == '/':
    operator = int(n1) / int(n2) / int(n3) / int(n4)
elif operator == '//':
    operator = int(n1) // int(n2) // int(n3) // int(n4)
elif operator == '%':
    operator = int(n1) % int(n2) % int(n3) % int(n4)
else:
    operator = 'Operação não suportada ! '

print('O resultado da operação é: ' + str(operator))

"""

# Relógio Digital - front-end

from tkinter import*
from tkinter.ttk import*
from time import strftime

root = Tk()
root.title('Relógio Digital')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=('ds=digital', 100), background= 'dark blue', foreground= '#ffd60a', relief= 'flat')
label.pack(anchor= 'center')
time()

mainloop()