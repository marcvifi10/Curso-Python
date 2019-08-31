from Tkinter import *
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()


def abreFichero():

	# initialdir = directorio por el que empieza a buscar
	# filetypes = busca el tipo de archivo determinado
	fichero=tkFileDialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros PDF","*.pdf"),
		("Ficheros de texto","*.txt"),("Todos los archivos","*.*")))

	print(fichero)


Button (root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()