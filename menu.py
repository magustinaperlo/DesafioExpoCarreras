from tkinter import *
from tkinter import ttk
from viewalta import abrir_alta
from viewlistado import *

class MENU(Frame):
    def __init__(self, master):
        super().__init__(master, height=500, width=800, bg="#b39658")
        self.master = master
        self.pack_propagate(0)
        self.pack(expand=True)
        self.ventana_menu()

    def comando_alta(self):
        self.master.withdraw()
        ventana = Toplevel(self.master)
        ventana.wm_title("Formulario de contacto para ISAUI")
        ventana.wm_resizable(0,0)
        entradas = abrir_alta(ventana)
        def on_closing():
            ventana.destroy()
            self.master.deiconify()  # Muestra la ventana principal nuevamente
    
        ventana.protocol("WM_DELETE_WINDOW", on_closing)
        entradas.mainloop()

    def comando_lista(self):
        abrir_listado()

    def ventana_menu(self):
        frame_menu = LabelFrame(self, text="Menú", bg="white", font=('Calibri', 20), borderwidth=5)
        frame_menu.pack(expand= True, ipadx= 100, ipady= 50)

        contenedor = Frame(frame_menu, bg="white")
        contenedor.pack(expand=True)
        btn_alta = Button(contenedor, text="Agregar Persona", justify= CENTER, font=('Calibri', 25), bg= "DarkOliveGreen3", activebackground= "DarkOliveGreen2", command=self.comando_alta)
        btn_alta.grid(row= 2, rowspan=2, column=1 ,columnspan=2, padx= 15, ipadx= 12, ipady= 35)
        btn_lista = Button(contenedor, text="Ver Personas", justify= CENTER, font=('Calibri', 25), bg= "DarkOrange2", activebackground= "DarkOrange1", command=self.comando_lista)
        btn_lista.grid(row= 2, rowspan=2, column= 4, columnspan=2, padx= 15, ipadx= 32, ipady= 35)

if __name__ == "__main__":  
    ventana = Tk()
    ventana.wm_title("Menú")
    ventana.wm_resizable(0,0)
    ventana.geometry("+200+100")
    menu = MENU(ventana)
    menu.mainloop()