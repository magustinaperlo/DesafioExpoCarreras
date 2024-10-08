import re
from tkinter import messagebox

# Función para mostrar los errores acumulados al final
def mostrar_errores_acumulados(errores):
    if errores:
        messagebox.showerror("ATENCIÓN", "\n".join(errores))

# Validar DNI
def validar_dni(dni, errores):
    if not dni.isdigit():
        errores.append("El DNI solo debe contener dígitos.")
    elif len(dni) < 7 or len(dni) > 8:
        errores.append("El número de DNI debe tener 7 u 8 dígitos.")

# Validar teléfono
def validar_telefono(telefono, errores):
    if not telefono.isdigit():
        errores.append("El teléfono solo debe contener dígitos.")
    elif len(telefono) < 6 or len(telefono) > 10:
        errores.append("El número de teléfono debe tener entre 6 y 10 dígitos.")

# Validar correo electrónico
def verificar_correo(correo, errores):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, correo):
        errores.append("El correo no es válido o no existe.")

# Validar campos obligatorios
def validar_campos_obligatorios(entries, errores):
    if any(entry.get().strip() == "" for entry in entries):
        errores.append("Todos los campos del formulario son obligatorios.")