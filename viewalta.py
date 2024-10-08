#interfaz muestra
from tkinter import * 
from FuncionesValidacion import verificar_correo, validar_dni, validar_telefono, validar_campos_obligatorios
from ConexionBD import *

class abrir_alta(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 1366, height = 768, bg = "#b39658")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.interfaz()
        self.fin = 0

    def getSeleccionCarrera(self):
        carrera = self.variable.get()
        return carrera

    def getEntradasUsuario(self):
            apellido = self.entry_apellido.get().strip()
            nombre = self.entry_nombre.get().strip() 
            dni = self.entry_dni.get().strip()
            telefono = self.entry_telefono.get().strip()
            correo = self.entry_correo.get().strip()
            domicilio= self.entry_domicilio.get().strip()
            ciudad= self.entry_ciudad.get().strip()
            instagram = self.entry_instagram.get().strip()
            return apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram

    def limpiar_campos(self, entries):
        for entry in entries:
            entry.delete(0, tk.END)

    def guardar_datos(self):
        carrera = self.getSeleccionCarrera()
        entries =[self.entry_apellido, self.entry_nombre, self.entry_dni, self.entry_telefono, self.entry_correo, self.entry_domicilio, self.entry_ciudad, self.entry_instagram]
        if not validar_campos_obligatorios(entries):
            return  # Detener si los campos están vacíos
        
        apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram = self.getEntradasUsuario()
            
        # validaciones del archivo FuncionesValidacion
    
        if not verificar_correo(correo):
            return 
        if not validar_dni(dni):
            return  
        if not validar_telefono(telefono):
            return   
        if (messagebox.askyesno("Confirmar", "¿Desea guardar los datos?")):
            insertar_persona(apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram, carrera)
            self.limpiar_campos(entries)
        else:
            messagebox.showinfo("Cancelado", "No se guardaron los datos.")
        
    def procesar_formulario(self):
        apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram = self.getEntradasUsuario()
        
        if apellido and nombre and dni:  # Simple validación de que algunos campos no estén vacíos
            insertar_persona(apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram)
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
    
    def on_closing(self):
        self.fin = 1    
        self.master.destroy()

    def interfaz(self):
        self.variable = tk.StringVar()
        #marco
        frame= LabelFrame(self, text="Seleccione la carrera", bg="white", font= ('Calibri', 20), borderwidth=5)
        frame.grid(row= 0, column=0, padx=60, pady=50 )

        frame_datos= LabelFrame(self, text="Ingrese sus datos:", bg="#dbc79c", font= ('Calibri', 20), borderwidth=5)
        frame_datos.grid(row= 1, column=0, columnspan=9, ipadx= 50, ipady=10)

        #etiquetas 

        label_apellido = Label(frame_datos, text="Apellido: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
        label_apellido.grid(row= 1, column=1, pady= 10)

        label_nombre = Label(frame_datos, text="Nombre: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
        label_nombre.grid(row= 2, column=1, pady= 10)

        label_dni = Label(frame_datos, text="DNI: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
        label_dni.grid(row= 3, column=1, pady= 10)

        label_telefono = Label(frame_datos, text="Teléfono: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
        label_telefono.grid(row= 4, column=1, pady= 10)

        label_domicilio = Label(frame_datos, text="Domicilio: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
        label_domicilio.grid(row= 5, column=1, pady= 10)

        label_ciudad = Label(frame_datos, text="Ciudad: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
        label_ciudad.grid(row= 6, column=1, pady= 10)

        label_correo = Label(frame_datos, text="Correo: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
        label_correo.grid(row= 7, column=1, pady= 10)

        label_instagram = Label(frame_datos, text="Instagram: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
        label_instagram.grid(row= 8, column=1, pady= 10)

        #entradas
        self.entry_apellido= Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_apellido.grid(row= 1, column=2, ipadx=400)

        self.entry_nombre = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_nombre.grid(row=2, column=2, ipadx=400)

        self.entry_dni = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_dni.grid(row=3, column=2, ipadx=400)

        self.entry_telefono = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_telefono.grid(row=4, column=2, ipadx=400)

        self.entry_domicilio = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_domicilio.grid(row=5, column=2, ipadx=400)

        self.entry_ciudad = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_ciudad.grid(row=6, column=2, ipadx=400)

        self.entry_correo = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_correo.grid(row=7, column=2, ipadx=400)

        self.entry_instagram = Entry(frame_datos, bg="white", font=('Calibri', 15))
        self.entry_instagram.grid(row=8, column=2, ipadx=400)


        #radio botones
        btn_software = Radiobutton(frame, text="Desarrollo de Software", variable=self.variable,value=1, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_software.grid(row=1, column=3, padx=10, pady=10)

        btn_enfermeria = Radiobutton(frame, text="Enfermería",  variable=self.variable,value=2, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_enfermeria.grid(row=1, column=4, padx=10, pady=10)

        btn_disenio = Radiobutton(frame, text="Diseño de Espacios", variable=self.variable,value=3, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_disenio.grid(row=1, column=5, padx=10, pady=10)

        btn_guia = Radiobutton(frame, text="Guía en Turismo", variable=self.variable,value=5, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_guia.grid(row=1, column=6, padx=10, pady=10)

        btn_guia_turismo_hoteleria = Radiobutton(frame, text="Guía de Turismo y Hotelería", variable=self.variable,value=6, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_guia_turismo_hoteleria.grid(row=1, column=7, padx=10, pady=10)

        btn_trekking = Radiobutton(frame, text="Guía de Trekking y Guía de montaña ", variable=self.variable, value=4, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_trekking.grid(row=1, column=8, padx=10, pady=10)

        #Hacer que todos los radio buttons comiencen sin estar marcados.
        self.variable.set(None)

        #botón
        botones = Frame(self, bg="#b39658")
        botones.grid(row=3, column=0, pady= 10)

        btn_guardar = Button(botones, text="Guardar", borderwidth=2,  bg="#ffffff" ,font=('Calibri', 15), command=self.guardar_datos)
        btn_guardar.grid(row=0, column=1, padx=20, pady=20,  ipadx=40)

        # Botón de Volver
        btn_volver = Button(botones, text="Volver", borderwidth=2,  bg="#ffffff" ,font=('Calibri', 15), command=self.volver_a_menu)
        btn_volver.grid(row=0, column=3, padx=20, pady=20, ipadx=40)

    def volver_a_menu(self):
        self.master.withdraw()
        self.master.master.deiconify()  # Muestra la ventana principal nuevamente

"""
ventana = Tk()
ventana.wm_title("Formulario de contacto para ISAUI")
ventana.wm_resizable(0,0)
entradas = abrir_alta(ventana)
entradas.mainloop()
"""