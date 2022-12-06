
from tkinter import *
from tkinter.ttk import *

from time import strftime

raiz = Tk()
raiz.title('Clock')

def hora_actual():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, hora_actual)
 

lbl = Label(raiz)
 

lbl.pack(anchor='center')
hora_actual()
 
mainloop()

