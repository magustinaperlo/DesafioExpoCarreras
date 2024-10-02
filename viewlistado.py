import tkinter as tk
from tkinter import ttk
import mysql.connector


# Conexión a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="",  
    database="isaui"
)
mycursor = mydb.cursor()

root = tk.Tk()
root.title("Listado de personas")

style = ttk.Style()  # crear objeto ttk.Style
style.configure("BigFont.TRadiobutton", font=("Helvetica", 14))  # configurar estilo de fuente

label_seleccionar_carrera = ttk.Label(root, text="Seleccionar carrera para filtrar", font=("Calibri", 20, "bold"))
label_seleccionar_carrera.grid(row=0, column=0, sticky="nsew", pady=(10, 0))

frame_superior = tk.Frame(root, bg="gray90")
frame_superior.grid(row=1, column=0, sticky="nsew")

frame_inferior = tk.Frame(root, bg="gray90")
frame_inferior.grid(row=2, column=0, sticky="nsew")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)

# Botones
variable_de_filtro_carrera = tk.StringVar()

frame_superior.rowconfigure(0, weight=1)
frame_superior.rowconfigure(1, weight=1)
frame_superior.columnconfigure(0, weight=1)
frame_superior.columnconfigure(1, weight=1)
frame_superior.columnconfigure(2, weight=1)

# Tabla para mostrar los registros
arbol = ttk.Treeview(frame_inferior, columns=("apellido", "nombre", "dni", "carrera"), show="headings")
arbol.grid(row=0, column=0, sticky="nsew")

arbol.heading("apellido", text="Apellido")
arbol.heading("nombre", text="Nombre")
arbol.heading("dni", text="DNI")
arbol.heading("carrera", text="Carrera")

def mostrar_registros(*args):
    for row in arbol.get_children():
        arbol.delete(row)
    
    carrera_seleccionada = variable_de_filtro_carrera.get() 
    if carrera_seleccionada:
        query = "SELECT apellido, nombre, dni, id_carreras FROM personas WHERE id_carreras = %s"
        mycursor.execute(query, (carrera_seleccionada,))
    else:
        query = "SELECT apellido, nombre, dni, id_carreras FROM personas"
        mycursor.execute(query)
    
    for (apellido, nombre, dni, id_carreras) in mycursor:
        arbol.insert("", "end", values=(apellido, nombre, dni, id_carreras))

carreras = {
    1: "Software",
    2: "Enfermería",
    3: "Diseño de Espacios",
    4: "Guía de Trekking",
    5: "Guía de Turismo",
    6: "Turismo y Hotelería"
}

for i, (id_carrera, nombre_carrera) in enumerate(carreras.items()):
    filtro_carrera = ttk.Radiobutton(frame_superior, text=nombre_carrera, variable=variable_de_filtro_carrera, value=str(id_carrera), style="BigFont.TRadiobutton", command=mostrar_registros)
    row = i // 3  # calcular el índice de fila
    col = i % 3  # calcular el índice de columna
    filtro_carrera.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)  # configuración de grid

mostrar_registros()

root.mainloop()