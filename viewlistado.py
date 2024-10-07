from tkinter import *
from tkinter import ttk
import mysql.connector
from ConexionBD import *

class LISTADO(Frame):
    def __init__(self, master = None):
        super(). __init__(master, bg="#b39658", width=1366, height=768)
        self.master = master
        self.pack_propagate(False)
        self.pack(expand=True)
        mycursor.execute("SELECT * FROM carreras")
        self.carreras = mycursor.fetchall()
        mycursor.execute("SELECT * FROM personas")
        self.personas = mycursor.fetchall()
        self.variable = IntVar(value=0)  

        self.interfaz()
        

    def actualizar_treeview(self):
        seleccionar_carrera = self.variable.get()
        #print(f"Valor seleccionado: {seleccionar_carrera}")
        arbol = self.arbol
        for item in arbol.get_children():
            arbol.delete(item)

            #print(f"Filtrando por carrera ID: {seleccionar_carrera}")

        if seleccionar_carrera != 0:  #Verifica que se haya seleccionado una carrera
            mycursor.execute("SELECT * FROM personas WHERE id_carreras = %s", (seleccionar_carrera,))
        else:
            mycursor.execute("SELECT * FROM personas")  #Sin filtro

        personas_filtradas = mycursor.fetchall()
        #print(f"Personas filtradas: {personas_filtradas}")
        for persona in personas_filtradas:
            carrera = [c[1] for c in self.carreras if c[0] == persona[9]]
            if carrera:
                arbol.insert("", "end", values=(persona[1], persona[2], persona[3], persona[4],
                                                persona[5], persona[6], persona[7], persona[8], carrera[0]))

    def interfaz(self):
        frame = LabelFrame(self, text="Seleccione carrera para filtrar", bg="white", font=('Calibri', 20), borderwidth=5)
        frame.grid(row=0, column=0, padx=5, pady=50)

        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.columnconfigure(0, weight=1)

        #Actualiza la tabla según la carrera seleccionada
        
        # Radio buttons
        btn_todas = Radiobutton(frame, text="Todas las Carreras", variable=self.variable, value=0, command= self.actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_todas.grid(row=1, column=5, padx=10, pady=10)

        btn_software = Radiobutton(frame, text="Desarrollo de Software", variable=self.variable, value=1, command=self.actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_software.grid(row=2, column=2, padx=10, pady=10)

        btn_enfermeria = Radiobutton(frame, text="Enfermería", variable=self.variable, value=2, command=self.actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_enfermeria.grid(row=2, column=3, padx=10, pady=10)

        btn_disenio = Radiobutton(frame, text="Diseño de Espacios", variable=self.variable, value=3, command=self.actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_disenio.grid(row=2, column=4, padx=10, pady=10)

        btn_guia = Radiobutton(frame, text="Guía en Turismo", variable=self.variable, value=5, command=self.actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_guia.grid(row=2, column=5, padx=10, pady=10)

        btn_guia_turismo_hoteleria = Radiobutton(frame, text="Guía de Turismo y Hotelería", variable=self.variable, value=6, command=self.actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_guia_turismo_hoteleria.grid(row=2, column=6, padx=10, pady=10)

        btn_trekking = Radiobutton(frame, text="Guía de Trekking y Guía de montaña", variable=self.variable, value=4, command=self.actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
        btn_trekking.grid(row=2, column=7, padx=10, pady=10)

        #Treeview
        self.arbol = ttk.Treeview(self, columns=("apellido", "nombre", "dni", "carrera", "telefono", "domicilio", "ciudad", "correo", "instagram"), show="headings")
        self.arbol.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        stilo = ttk.Style()
        stilo.configure("Treeview", font=("Robot", 10), rowheight=25)  #Cambia la fuente y el alto de las filas
        stilo.configure("Treeview.Heading", font=("Robot", 13))

        self.arbol.heading("apellido", text="Apellido")
        self.arbol.heading("nombre", text="Nombre")
        self.arbol.heading("dni", text="DNI")
        self.arbol.heading("telefono", text="Teléfono")
        self.arbol.heading("correo", text="Correo")
        self.arbol.heading("domicilio", text="Domicilio")
        self.arbol.heading("ciudad", text="Ciudad")
        self.arbol.heading("instagram", text="Instagrama")
        self.arbol.heading("carrera", text="Carrera")

        #Ancho de las columnas y datos centrados
        self.arbol.column("apellido", anchor='center', width=150)
        self.arbol.column("nombre", anchor='center', width=150)
        self.arbol.column("dni", anchor='center', width=150)
        self.arbol.column("telefono", anchor='center', width=150)
        self.arbol.column("correo", anchor='center', width=150)
        self.arbol.column("domicilio", anchor='center', width=150)
        self.arbol.column("ciudad", anchor='center', width=150)
        self.arbol.column("instagram", anchor='center', width=150)
        self.arbol.column("carrera", anchor='center', width=150)

        #Carga los datos iniciales
        self.actualizar_treeview()

'''def abrir_listado():
    ventana = Tk()
    ventana.wm_title("Listado de personas")
    ventana.wm_resizable(False, False)
    entrada = LISTADO(ventana)
    entrada.mainloop()'''

