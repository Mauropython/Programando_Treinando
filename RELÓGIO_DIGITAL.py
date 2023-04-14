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