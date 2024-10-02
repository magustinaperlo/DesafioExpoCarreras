from tkinter import *
from tkinter import ttk
import mysql.connector
from ConexionBD import *
from viewalta import *
from viewlistado import *

ventana = Tk()
ventana.title("Menú")
ventana.geometry("800x500")
ventana.configure(bg="#b39658")
ventana.resizable(False, False)

frame_menu = LabelFrame(ventana, text="Menú", bg="white", font=('Calibri', 20), borderwidth=5)
frame_menu.pack(expand= True, ipadx= 100, ipady= 100)

contenedor = Frame(frame_menu, bg="white")
contenedor.pack(expand=True)
btn_alta = Button(contenedor, text="Agregar Persona", justify= CENTER, font=('Calibri', 25), bg= "DarkOliveGreen3", activebackground= "DarkOliveGreen2")
btn_alta.grid(row= 2, rowspan=2, column=1 ,columnspan=2, padx= 15, ipadx= 12, ipady= 35)
btn_lista = Button(contenedor, text="Ver Personas", justify= CENTER, font=('Calibri', 25), bg= "DarkOrange2", activebackground= "DarkOrange1")
btn_lista.grid(row= 2, rowspan=2, column= 4, columnspan=2, padx= 15, ipadx= 32, ipady= 35)

ventana.mainloop()