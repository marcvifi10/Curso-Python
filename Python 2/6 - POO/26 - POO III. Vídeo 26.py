class Coche:
	# Declaramos los atributos
	largoChasis = 250
	anchoChasis = 120
	ruedas = 4
	enmarcha = False

	# Declaramos los métodos
	def arrancar(self):
		self.enmarcha = True

	def estado(self):
		if (self.enmarcha):
			return "El coche esta en marcha"

		else:
			return "El coche esta parado"

# Creamos un objeto de la clase Coche
miCoche = Coche()

print("El largo del coche es",miCoche.largoChasis)
print("El coche tiene",miCoche.ruedas,"ruedas.")
miCoche.arrancar()
print(miCoche.estado())
