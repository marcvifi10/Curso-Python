from Tkinter import * 

root = Tk()

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
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

# Creamos el submenu de Editar
editionMenu.add_command(label="Copiar")
editionMenu.add_command(label="Cortar")
editionMenu.add_command(label="Pegar")

# Creamos el submenu de Ayuda
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")
ayudaMenu.add_command(label="Documentacion")

root.mainloop()