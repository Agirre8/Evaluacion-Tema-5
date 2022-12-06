from  tkinter import *
import datetime

def obtener_hora_actual():
    return datetime.now().strftime("%H:%M:%S")

