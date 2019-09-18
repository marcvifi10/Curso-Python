class Coche():

	def desplazamiento(self):
		print("Me desplazo utilizando 4 ruedas")


class Moto():

	def desplazamiento(self):
		print("Me desplazo utilizando 2 ruedas")


class Camion():

	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")


moto = Moto()
moto.desplazamiento()

coche = Coche()
coche.desplazamiento()

camion = Camion()
camion.desplazamiento()

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

camion2 = Camion()

desplazamientoVehiculo(camion2)