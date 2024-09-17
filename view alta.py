#interfaz muestra
from tkinter import * 

#ventana
ventana = Tk()
ventana.title("Datos de preincripción a las carreras")
ventana.geometry("1366x798")
ventana.configure(bg="#477c94")
ventana.resizable(False, False)

#marco
frame= LabelFrame(ventana, text="Seleccione la carrera", bg="#dbc79c", font= ('Calibri', 20), borderwidth=5)
frame.grid(row= 0, column=0, padx=60, pady=50 )

frame_datos= LabelFrame(ventana, text="Ingrese sus datos:", bg="#dbc79c", font= ('Calibri', 20), borderwidth=5)
frame_datos.grid(row= 1, column=0, columnspan=9, ipadx=100, ipady=10)

#etiquetas 

label_apellido = Label(frame_datos, text="Apellido: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
label_apellido.grid(row= 1, column=1, pady= 10)

label_nombre = Label(frame_datos, text="Nombre: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
label_nombre.grid(row= 2, column=1, pady= 10)

label_dni = Label(frame_datos, text="DNI: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
label_dni.grid(row= 3, column=1, pady= 10)

label_telefono = Label(frame_datos, text="Teléfono: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
label_telefono.grid(row= 4, column=1, pady= 10)

label_domicilio = Label(frame_datos, text="Domicilio: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
label_domicilio.grid(row= 5, column=1, pady= 10)

label_ciudad = Label(frame_datos, text="Ciudad: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
label_ciudad.grid(row= 6, column=1, pady= 10)

label_correo = Label(frame_datos, text="Correo: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
label_correo.grid(row= 7, column=1, pady= 10)

label_instagram = Label(frame_datos, text="Instagram: ", bg="#dbc79c", fg="black", font=('Calibri', 15))
label_instagram.grid(row= 8, column=1, pady= 10)

#entradas
entry_apellido= Entry (frame_datos, bg="white", font=('Calibri', 15))
entry_apellido.grid(row= 1, column=2, ipadx=400)

entry_nombre= Entry (frame_datos, bg="white", font=('Calibri', 15))
entry_nombre.grid(row= 2, column=2, ipadx=400)

entry_dni= Entry (frame_datos, bg="white", font=('Calibri', 15))
entry_dni.grid(row= 3, column=2, ipadx=400)

entry_telefono= Entry (frame_datos, bg="white", font=('Calibri', 15))
entry_telefono.grid(row= 4, column=2, ipadx=400)

entry_domicilio= Entry (frame_datos, bg="white", font=('Calibri', 15))
entry_domicilio.grid(row= 5, column=2, ipadx=400)

entry_ciudad= Entry (frame_datos, bg="white", font=('Calibri', 15))
entry_ciudad.grid(row= 6, column=2, ipadx=400)

entry_correo= Entry (frame_datos, bg="white", font=('Calibri', 15))
entry_correo.grid(row= 7, column=2, ipadx=400)

entry_instagram= Entry (frame_datos, bg="white", font=('Calibri', 15))
entry_instagram.grid(row= 8, column=2, ipadx=400)

#radio botones
btn_software = Radiobutton(frame, text="Desarrollo de Software", value=1, borderwidth=2, bg="#dbc79c", font=('Calibri', 13))
btn_software.grid(row=1, column=3, padx=10, pady=10)

btn_enfermeria = Radiobutton(frame, text="Enfermería",  value=2, borderwidth=2, bg="#dbc79c", font=('Calibri', 13))
btn_enfermeria.grid(row=1, column=4, padx=10, pady=10)

btn_disenio = Radiobutton(frame, text="Diseño de Espacios", value=3, borderwidth=2, bg="#dbc79c", font=('Calibri', 13))
btn_disenio.grid(row=1, column=5, padx=10, pady=10)

btn_guia = Radiobutton(frame, text="Guía en Turismo", value=4, borderwidth=2, bg="#dbc79c", font=('Calibri', 13))
btn_guia.grid(row=1, column=6, padx=10, pady=10)

btn_guia_turismo_hoteleria = Radiobutton(frame, text="Guía de Turismo y Hotelería", value=5, borderwidth=2, bg="#dbc79c", font=('Calibri', 13))
btn_guia_turismo_hoteleria.grid(row=1, column=7, padx=10, pady=10)

btn_trekking = Radiobutton(frame, text="Guía de Trekking y Guía de montaña ",  value=6, borderwidth=2, bg="#dbc79c", font=('Calibri', 13))
btn_trekking.grid(row=1, column=8, padx=10, pady=10)

#botón
button = Button(ventana, text="Guardar", borderwidth=2, bg="#ffffff" ,font=('Calibri', 15))
button.grid(row=3, column=0, padx=10, pady=20,  ipadx=40)

ventana.mainloop()
