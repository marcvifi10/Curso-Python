from Tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

# Ponemos una imagen
miImagen = PhotoImage(file="raton.jpg")

# Creamos una etiqueta y de color rojo
#miLabel = Label(miFrame, text="Hola!!!!!", fg="red", font=("Times New Roman",18))
Label(miFrame, image=miImagen).place(x=100, y=200)

# place = coordenadas
#miLabel.place(x=100,y=200)

root.mainloop()