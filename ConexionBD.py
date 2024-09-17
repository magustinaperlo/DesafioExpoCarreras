import tkinter as tk
import mysql.connector 

mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="AGREGAR NOMBRE", #PONER SU PROPIO USUARIO
        password="AGREGAR CLAVE", #PONER SU PROPIA CLAVE
        database="isaui")
mycursor = mydb.cursor()

def insertar_persona():
        apellido = entry_apellido.get()
        nombre = entry_nombre.get() # ... Obtener los valores de los demás campos
        dni = entry_dni.get()
        telefono = entry_telefono.get()
        correo = entry_correo.get()
        domicilio= entry_domicilio.get()
        ciudad= entry_ciudad.get()
        instagram = entry_instagram.get()
        sql = "INSERT INTO personas (apellido, nombre, dni, telefono, correo, domicilio, ciudad,instagram) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (apellido, nombre, dni, telefono, correo, domicilio, ciudad, instagram)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Registro insertado correctamente.")
