from tkinter import *
from tkinter import ttk
import mysql.connector

def abrir_listado():
    # Conectar a la base de datos
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='isaui'
    )
    cursor = cnx.cursor()

    cursor.execute("SELECT * FROM carreras")
    carreras = cursor.fetchall()

    cursor.execute("SELECT * FROM personas")
    personas = cursor.fetchall()


    ventana = Tk()
    ventana.title("Listado de personas")
    ventana.geometry("1366x768")
    ventana.configure(bg="#b39658")
    ventana.resizable(False, False)

    variable = StringVar(value="0")  


    frame = LabelFrame(ventana, text="Seleccione carrera para filtrar", bg="white", font=('Calibri', 20), borderwidth=5)
    frame.grid(row=0, column=0, padx=5, pady=50)

    ventana.rowconfigure(0, weight=1)
    ventana.rowconfigure(1, weight=1)
    ventana.rowconfigure(2, weight=1)
    ventana.columnconfigure(0, weight=1)

    #Actualiza la tabla según la carrera seleccionada
    def actualizar_treeview():
        for item in arbol.get_children():
            arbol.delete(item)

        seleccionar_carrera = variable.get()
        if seleccionar_carrera != "0":  #Verifica que se haya seleccionado una carrera
            cursor.execute("SELECT * FROM personas WHERE id_carreras = %s", (seleccionar_carrera,))
        else:
            cursor.execute("SELECT * FROM personas")  #Sin filtro

        personas_filtradas = cursor.fetchall()
        for persona in personas_filtradas:
            arbol.insert("", "end", values=(persona[1], persona[2], persona[3], persona[4],persona[5],persona[6],persona[7],persona[8], [c[1] for c in carreras if c[0] == persona[9]][0]))

    # Radio buttons
    btn_todas = Radiobutton(frame, text="Todas las Carreras", variable=variable, value="0", command=actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
    btn_todas.grid(row=1, column=5, padx=10, pady=10)

    btn_software = Radiobutton(frame, text="Desarrollo de Software", variable=variable, value="1", command=actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
    btn_software.grid(row=2, column=2, padx=10, pady=10)

    btn_enfermeria = Radiobutton(frame, text="Enfermería", variable=variable, value="2", command=actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
    btn_enfermeria.grid(row=2, column=3, padx=10, pady=10)

    btn_disenio = Radiobutton(frame, text="Diseño de Espacios", variable=variable, value="3", command=actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
    btn_disenio.grid(row=2, column=4, padx=10, pady=10)

    btn_guia = Radiobutton(frame, text="Guía en Turismo", variable=variable, value="5", command=actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
    btn_guia.grid(row=2, column=5, padx=10, pady=10)

    btn_guia_turismo_hoteleria = Radiobutton(frame, text="Guía de Turismo y Hotelería", variable=variable, value="6", command=actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
    btn_guia_turismo_hoteleria.grid(row=2, column=6, padx=10, pady=10)

    btn_trekking = Radiobutton(frame, text="Guía de Trekking y Guía de montaña", variable=variable, value="4", command=actualizar_treeview, borderwidth=2, bg="white", font=('Calibri', 13))
    btn_trekking.grid(row=2, column=7, padx=10, pady=10)

    #Treeview
    arbol = ttk.Treeview(ventana, columns=("apellido", "nombre", "dni", "carrera", "telefono", "domicilio", "ciudad", "correo", "instagram"), show="headings")
    arbol.grid(row=1, column=0, sticky="nsew")

    stilo = ttk.Style()
    stilo.configure("Treeview", font=("Robot", 11), rowheight=25)  #Cambia la fuente y el alto de las filas
    stilo.configure("Treeview.Heading", font=("Robot", 14))

    arbol.heading("apellido", text="Apellido")
    arbol.heading("nombre", text="Nombre")
    arbol.heading("dni", text="DNI")
    arbol.heading("telefono", text="Teléfono")
    arbol.heading("correo", text="Correo")
    arbol.heading("domicilio", text="Domicilio")
    arbol.heading("ciudad", text="Ciudad")
    arbol.heading("instagram", text="Instagrama")
    arbol.heading("carrera", text="Carrera")

    #Ancho de las columnas y datos centrados
    arbol.column("apellido", anchor='center', width=150)
    arbol.column("nombre", anchor='center', width=150)
    arbol.column("dni", anchor='center', width=150)
    arbol.column("telefono", anchor='center', width=150)
    arbol.column("correo", anchor='center', width=150)
    arbol.column("domicilio", anchor='center', width=150)
    arbol.column("ciudad", anchor='center', width=150)
    arbol.column("instagram", anchor='center', width=150)
    arbol.column("carrera", anchor='center', width=150)

    #Carga los datos iniciales
    actualizar_treeview()

    ventana.mainloop()
