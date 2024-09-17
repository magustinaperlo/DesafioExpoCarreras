import tkinter as tk
import re
from tkinter import messagebox

#Validar correo electronico
def verificar_correo():
    correo = entry_correo.get()
    # Expresión regular para validar el formato del correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
   
    # Comprobar si el correo cumple con el patrón
    if not re.match(patron, correo):
        messagebox.showerror("Error", f"{correo} no es una dirección de correo válida.")
        entry_correo.delete(0, tk.END)
    
def validar_dni(event=None):
    dni = entry_dni.get()  # Obtiene el valor del Entry
    if not dni.isdigit():  # Verifica si el DNI tiene solo números
        messagebox.showerror("Error", "Solamente se aceptan dígitos")
        entry_dni.delete(0, tk.END)
    elif len(dni) < 7 or len(dni) > 8:  # Verifica que el DNI tenga 7 u 8 dígitos
        messagebox.showerror("Error", "El número debe tener 7 u 8 dígitos")
        entry_dni.delete(0, tk.END)

def validar_telefono():
    telefono = entry_telefono.get()  
    if not telefono.isdigit():  
        messagebox.showerror("Error", "Solamente se aceptan dígitos")
        entry_telefono.delete(0, tk.END)
    elif len(telefono) < 6 or len(telefono) > 10:
        messagebox.showerror("Error", "El número de teléfono debe tener entre 6 y 10 dígitos")
        entry_telefono.delete(0, tk.END)

def eliminar_espacios():
    usuario = entry_user.get().strip()  # Elimina espacios en blanco al principio y al final

    # Verifica que no haya más de 1 espacios consecutivos
    if not usuario or re.search(r'\s{2,}', pelicula):
        messagebox.showwarning("Error", "La entrada no debe tener más de 2 espacios consecutivos ni estar vacía.")
    else:
        listbox.insert(tk.END, usuario)
    
    entry_user.delete(0, tk.END)


