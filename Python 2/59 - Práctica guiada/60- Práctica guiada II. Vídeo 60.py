from Tkinter import *
from Tkinter import * 
import tkMessageBox
import Tkinter, Tkconstants, tkFileDialog
import tkMessageBox
import sqlite3
# from tkinter import messagebox

root = Tk()

root.title("Practica guiada")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# Establecemos cuantos elementos tendra nuestro menu principal
# tearoff = elimina la barra horizontal discontinua
bddMenu=Menu(barraMenu, tearoff=0)
borrarMenu=Menu(barraMenu, tearoff=0)
crudMenu=Menu(barraMenu, tearoff=0)
ayudaMenu=Menu(barraMenu, tearoff=0)

# Establecemos cual es el texto de los diferentes elementos del menu principal
barraMenu.add_cascade(label="BDD", menu=bddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# Creamos el submenu de BDD
bddMenu.add_command(label="Conectar")
bddMenu.add_command(label="Salir")

# Creamos el submenu de Borrar
borrarMenu.add_command(label="Borrar campos")

# Creamos el submenu de CRUD
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

# Creamos el submenu de Ayuda
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")


#-----------------------Comienzo de campos---------------------

miFrame = Frame(root)
miFrame.pack()

# Input ID
cuadroId=Entry(miFrame)
cuadroId.grid(row=0, column=1, padx=10, pady=10)

# Input Nombre
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
# Texto de color rojo
cuadroNombre.config(fg="red", justify="right")

# Input Password
cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
# Texto con *
cuadroNombre.config(show="*")

# Input Apellido
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

# Input Direccion
cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

# Textbox Comentarios
textComentario=Text(miFrame, width=16, height=5)
textComentario.grid(row=5, column=1, padx=10, pady=10)
# Creamos el Scroll vertical
scrollVert = Scrollbar(miFrame, command=textComentario.yview)
# Situamos el Scroll
scrollVert.grid(row=5, column=2, sticky="nsew")
textComentario.config(yscrollcommand=scrollVert.set)


root.mainloop()