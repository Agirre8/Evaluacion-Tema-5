from tkinter import*
from tkinter.ttk import *
from time import strftime

raiz = Tk()#le añado a la variable raiz todas las funciones de la libreria tkinter
raiz.title("Reloj")#creamos una pestaña llamada reloj con la funcion tittle


def hora_actual():
    hora = strftime("%H:%M:%S %p")#%H para horas M para minutos y S para segundos
    lbl.config(text=hora)
    lbl.after(1000, hora_actual)#pongo 1000 para recargar la figura del reloj cada 1 segundos

lbl = Label(raiz)#defino lbl
lbl.pack(anchor="center")

hora_actual()
mainloop()#ejecuta en bucle el programa 