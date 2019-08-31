from Tkinter import * 
import tkMessageBox
# from tkinter import messagebox

root = Tk()

# Funcion para construir una ventana emergente
# Primero texto de arriba y luego el de abajo
def infoAdicional():
	tkMessageBox.showinfo("Procesador de Marc", "Procesador de textos version 2019")

# Funcion para construir un aviso
# Primero texto de arriba y luego el de abajo
def avisoLicencia():
	tkMessageBox.showwarning("Licencia","producto bajo licencia GNU")

# Funcion para salir
def salirApp():
	#valor=tkMessageBox.askquestion("Salir","Deseas salir de la aplicacion")
	valor=tkMessageBox.askokcancel("Salir","Deseas salir de la aplicacion")

	# Si es si, salimos
	#if valor=="yes":
	#	root.destroy()

	# Si es aceptar, salimos
	if valor==True:
		root.destroy()

# Funcion para cerrarun documento
def cerrarDocumento():
	valor=tkMessageBox.askretrycancel("Reintentar","No es posible cerrar. Documento bloqueado")

	# Si es false, cerramos
	if valor==False:
		root.destroy()

root.title("Video 52")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# Establecemos cuantos elementos tendra nuestro menu principal
# tearoff = elimina la barra horizontal discontinua
archivoMenu=Menu(barraMenu, tearoff=0)
editionMenu=Menu(barraMenu, tearoff=0)
herramientasMenu=Menu(barraMenu, tearoff=0)
ayudaMenu=Menu(barraMenu, tearoff=0)

# Establecemos cual es el texto de los diferentes elementos del menu principal
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Editar", menu=editionMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# Creamos el submenu de Archivo
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
# Creamos un separador
archivoMenu.add_separator()
# Creamos los siguientes elementos de Archivo
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirApp)

# Creamos el submenu de Editar
editionMenu.add_command(label="Copiar")
editionMenu.add_command(label="Cortar")
editionMenu.add_command(label="Pegar")

# Creamos el submenu de Ayuda
ayudaMenu.add_command(label="Licencia",  command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de...", command=infoAdicional)
ayudaMenu.add_command(label="Documentacion")

root.mainloop()