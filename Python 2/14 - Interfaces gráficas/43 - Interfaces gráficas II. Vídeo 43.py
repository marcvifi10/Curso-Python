from Tkinter import * 

raiz = Tk()

# Dar titulo a la ventana
raiz.title("Ventana de pruebas")

# Impedir redimensionar la ventana 
# resizable(width,height) (1 = permitir, 0 = negar)
raiz.resizable(1,1)

# Poner un favicon en la ventana
raiz.iconbitmap("./icono.ico")

# Tamano de la ventana
# ancho, alto
#raiz.geometry("250x100")

# Cambiar color de fondo
raiz.config(bg="blue")

raiz.config(bd=12)
raiz.config(relief="groove")

# Creamos un Frame
miFrame = Frame()

# Ponemos el Frame encima de la ventana creada, y anclado a la derecha 
# bottom = abajo, right = derecha, left = izquierda...
# anchor = n(arriba), s(abajo), w(izquierda), e(derecha)
# miFrame.pack(fill="x") (fill="y", expand="True") (fill="both", expand="True")
miFrame.pack(side ="right", anchor = "n")

# Ponemos un color al Frame
miFrame.config(bg="red")

# Damos un tamano al Frame
miFrame.config(width="650", height="350")

# Cambiar el grosor del borde de la ventana
miFrame.config(bd=35)

# Cambiar el tipo de borde del Frame
miFrame.config(relief="groove")

# Cambiar el icono del raton
miFrame.config(cursor="hand2")

raiz.mainloop()