from Tkinter import * 

root = Tk()

root.title("Ejemplo")

playa = IntVar()
montana = IntVar()
rural = IntVar()

def opcionesViaje():

	opcionEscogida=""

	if(playa.get()==1):
		opcionEscogida+=" playa"

	if(montana.get()==1):
		opcionEscogida+=" monatana"

	if(rural.get()==1):
		opcionEscogida+=" rural"

	textoFinal.config(text=opcionEscogida)

#foto=PhotoImage(file="avion.png")
#Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="PLaya", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montana", variable=montana, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=rural, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()



root.mainloop()