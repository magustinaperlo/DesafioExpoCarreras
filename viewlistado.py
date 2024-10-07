import tkinter as tk
from tkinter import ttk
from ConexionBD import mycursor

root = tk.Tk()
root.title("Listado de personas")

style = ttk.Style()  # Crear objeto ttk.Style
style.configure("BigFont.TRadiobutton", font=("Helvetica", 14))  # Configurar estilo de fuente

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

# Variable para guardar la carrera seleccionada
variable_de_filtro_carrera = tk.StringVar()

frame_superior.rowconfigure(0, weight=1)
frame_superior.rowconfigure(1, weight=1)
frame_superior.columnconfigure(0, weight=1)
frame_superior.columnconfigure(1, weight=1)
frame_superior.columnconfigure(2, weight=1)

carreras = ["Guía de Turismo", "Turismo y Hoteleria", "Guia de Trekking", "Software", "Enfermería", "Diseño de Espacios"]

# Función para manejar la selección del filtro
def actualizar_filtro():
    carrera_seleccionada = variable_de_filtro_carrera.get()
    obtener_datos(carrera_seleccionada)

# Crear los RadioButtons para cada carrera
for i, carrera in enumerate(carreras):
    filtro_carrera = ttk.Radiobutton(frame_superior, text=carrera, variable=variable_de_filtro_carrera, value=carrera, style="BigFont.TRadiobutton", command=actualizar_filtro)
    row = i // 3  # Calcular fila
    col = i % 3  # Calcular columna
    filtro_carrera.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)

arbol = ttk.Treeview(frame_inferior, columns=("apellido", "nombre", "dni", "carrera"), show="headings")
arbol.grid(row=0, column=0, sticky="nsew")

arbol.heading("apellido", text="Apellido")
arbol.heading("nombre", text="Nombre")
arbol.heading("dni", text="DNI")
arbol.heading("carrera", text="Carrera")

# Función para llenar el Treeview con los datos filtrados por carrera
def obtener_datos(carrera_seleccionada=None):
    # Limpiar el Treeview
    for item in arbol.get_children():
        arbol.delete(item)
    
    # Consulta SQL para obtener los datos de personas y el nombre de la carrera
    query = """
        SELECT p.apellido, p.nombre, p.dni, c.nombre as carrera
        FROM personas p
        JOIN carreras c ON p.id_carreras = c.id_carreras
    """
    
    # Agregar el filtro por carrera si se selecciona una
    if carrera_seleccionada:
        query += f" WHERE c.nombre = '{carrera_seleccionada}'"
    
    mycursor.execute(query)
    filas = mycursor.fetchall()  # Obtener todos los resultados
    
    # Insertar cada fila en el Treeview
    for fila in filas:
        arbol.insert("", "end", values=fila)

# Botón para actualizar los datos manualmente


btn_volver = tk.Button(root, text="Volver", borderwidth=2,  bg="#ffffff" ,font=('Calibri', 15), command=root.destroy)
btn_volver.grid(row=4, column=0, padx=10, pady=20,  ipadx=40)

btn_actualizar = tk.Button(root, text="Actualizar", command=lambda: obtener_datos(variable_de_filtro_carrera.get()))
btn_actualizar.grid(row=3, column=0, pady=10)

# Llamamos a obtener_datos() al iniciar
obtener_datos()

root.mainloop()
