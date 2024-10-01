import tkinter as tk
from tkinter import messagebox
import mysql.connector


mydb = mysql.connector.connect(
        host="localhost",
        user="",
        password="", 
        database="isaui")
mycursor = mydb.cursor()

def insertar_persona(apellido,nombre,dni,telefono,correo,domicilio,ciudad,instagram,carrera):
        try:
            
            sql = "INSERT INTO personas (apellido, nombre, dni, telefono, correo, domicilio, ciudad,instagram,id_carreras) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram,carrera)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Éxito", "Registro insertado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al insertar en la base de datos: {err}")