import tkinter as tk import
mysql.connector
# Datos de conexión a la base de datos (reemplázalos con tus datos)
mydb = mysql.connector.connect(
    #conexion Lautaro
    host="127.0.0.1",
    user="root",
    password="123",
    database="nombre_de_tu_base_de_datos")
mycursor = mydb.cursor()