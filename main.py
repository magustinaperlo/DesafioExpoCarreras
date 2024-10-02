import tkinter as tk
from tkinter import ttk
import os

def abrir_alta():
    # Llama a la función que crea la ventana para el alta de estudiantes
    os.system('python viewalta.py')
def abrir_listado():
    # Llama a la función que crea la ventana para el listado de estudiantes
    os.system('python viewlistado.py')

def main():
    root = tk.Tk()
    root.title("Gestión de Estudiantes")
    root.geometry("300x200")

    label = ttk.Label(root, text="Seleccione una opción:", font=("Calibri", 16))
    label.pack(pady=20)

    # Botón para ir al formulario de alta
    btn_alta = ttk.Button(root, text="Alta de Estudiantes", command=abrir_alta)
    btn_alta.pack(pady=10)

    # Botón para ir al listado de estudiantes
    btn_listado = ttk.Button(root, text="Listado de Estudiantes", command=abrir_listado)
    btn_listado.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
