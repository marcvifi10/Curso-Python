import pickle

class Vehiculo:

	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		enmarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca: ",self.marca)
		print("Modelo: ",self.modelo)
		print("En marcha: ",self.enmarcha)
		print("Acelerando: ",self.acelera)
		print("Frenando: ",self.frena)



coche1 = Vehiculo("Mazda","MX5")

coche2 = Vehiculo("Seat","Leon")

coche3 = Vehiculo("Honda","Civic")

coches = [coche1, coche2, coche3]

fichero = open("losCoches","wb")

pickle.dump(coches, fichero)

fichero.close()

# Borramos el fichero de la memoria
del (fichero)


# rb = read bytes
ficheroApertura = open("losCoches","rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:

	print(c.estado())