from Tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
# Lo situamos en el sitio correcto fila, columna, sticky (alinear el texto (e = derecha, w = izquierda, n = arriba, s = abajo))
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
# Lo que escribamos en este cuadro, aparecera en color rojo
# Justify = Lo que escribamos en este caso estara alineado al centro
cuadroNombre.config(fg="red", justify="center")

cuadroPass = Entry(miFrame)
# Lo situamos en el sitio correcto
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
# Hacemos que por cada caracter que escriba, aparezca un *
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
# Lo situamos en el sitio correcto
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
# Lo situamos en el sitio correcto
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)


nombreLabel = Label(miFrame, text="Nombre: ")
# sticky (alinear el texto (e = derecha, w = izquierda, n = arriba, s = abajo))
# padx = separacion entre elementos eje x
# pady = separacion entre elementos eje y
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Contrasena: ")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Direccion de casa: ")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

raiz.mainloop()