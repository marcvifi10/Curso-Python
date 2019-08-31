from Tkinter import * 

raiz = Tk()

# Dar titulo a la ventana
raiz.title("Ventana de pruebas")

# Impedir redimensionar la ventana 
# resizable(width,height) (1 = permitir, 0 = negar)
raiz.resizable(1,1)

# Poner un favicon en la ventana
# raiz.iconbitmap("i.ico")

# Tamano de la ventana
# ancho, alto
raiz.geometry("250x100")

# Cambiar color de fondo
raiz.config(bg="blue")

raiz.mainloop()