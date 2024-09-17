import tkinter as tk
import re
from tkinter import messagebox

#Validar correo electronico
def validar_correo(correo):
   
    # Expresión regular para validar el formato del correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
   
    # Comprobar si el correo cumple con el patrón
    if re.match(patron, correo):
        return True
    else:
        return False


def verificar_correo():
    correo = entrada_correo.get()
    if validar_correo(correo):
        messagebox.showinfo("Éxito", f"{correo} es una dirección de correo válida.")
    else:
        messagebox.showerror("Error", f"{correo} no es una dirección de correo válida.")
    
def validar_dni(event=None):
    dni = vardni.get()  # Obtiene el valor del Entry
    if not dni.isdigit():  # Verifica si el DNI tiene solo números
        messagebox.showerror("Error", "Solamente se aceptan dígitos")
        vardni.delete(0, tk.END)
    elif len(dni) < 7 or len(dni) > 8:  # Verifica que el DNI tenga 7 u 8 dígitos
        messagebox.showerror("Error", "El número debe tener 7 u 8 dígitos")
        vardni.delete(0, tk.END)

def validar_telefono():
    telefono = vartelefono.get()  
    if not telefono.isdigit():  
        messagebox.showerror("Error", "Solamente se aceptan dígitos")
        vartelefono.delete(0, tk.END)
    elif len(telefono) < 6 or len(telefono) > 10:
        messagebox.showerror("Error", "El número de teléfono debe tener entre 6 y 10 dígitos")
        vartelefono.delete(0, tk.END)
