import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Listado de personas")

style = ttk.Style()  # crear objeto ttk.Style
style.configure("BigFont.TRadiobutton", font=("Helvetica", 14))  # configurar estilo de fuente

label_seleccionar_carrera = ttk.Label(root, text="SELECCIONAR CARRERA PARA FILTRAR", font=("Helvetica", 14, "bold"))
label_seleccionar_carrera.grid(row=0, column=0, sticky="nsew", pady=(10, 0))

frame_superior = tk.Frame(root, bg="gray90")
frame_superior.grid(row=1, column=0, sticky="nsew")

frame_inferior = tk.Frame(root, bg="gray90")
frame_inferior.grid(row=2, column=0, sticky="nsew")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)

# botones
variable_de_filtro_carrera = tk.StringVar()

frame_superior.rowconfigure(0, weight=1)
frame_superior.rowconfigure(1, weight=1)
frame_superior.columnconfigure(0, weight=1)
frame_superior.columnconfigure(1, weight=1)
frame_superior.columnconfigure(2, weight=1)

for i, carrera in enumerate(["Guía de Turismo", "Técnico en Turismo", "Trekking", "Software", "Enfermería", "Espacio"]):
    filtro_carrera = ttk.Radiobutton(frame_superior, text=carrera, variable=variable_de_filtro_carrera, value=carrera, style="BigFont.TRadiobutton")
    row = i // 3  # calculate row index
    col = i % 3  # calculate column index
    filtro_carrera.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)  # grid configuration

arbol = ttk.Treeview(frame_inferior, columns=("apellido", "nombre", "dni", "carrera"), show="headings")
arbol.grid(row=0, column=0, sticky="nsew")

arbol.heading("apellido", text="Apellido")
arbol.heading("nombre", text="Nombre")
arbol.heading("dni", text="DNI")
arbol.heading("carrera", text="Carrera")

arbol.insert("", "end", values=("Pérez", "Juan", "12345678", "Software"))
arbol.insert("", "end", values=("González", "María", "87654321", "Enfermería"))
arbol.insert("", "end", values=("Rodríguez", "Pedro", "34567890", "Técnico en Turismo"))

root.mainloop()