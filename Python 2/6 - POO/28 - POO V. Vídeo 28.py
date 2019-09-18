class Coche:
	# Declaramos los atributos
	# Declaramos un constructor
	def __init__(self):
		self.largoChasis = 250
		self.anchoChasis = 120

		# Hacemos que la variable ruedas no sea accesible fuera de la clase por los dos __, pero si dentro de ella
		self.__ruedas = 4
		self.estanmarcha = False

	# Declaramos los métodos
	def arrancar(self,arrancamos):
		self.enmarcha = arrancamos

		if (self.enmarcha):
			chequeo = self.chequeo_interno()

		if (self.enmarcha and chequeo):
			return "El coche esta en marcha"

		elif (self.enmarcha and chequeo == False):
			return "Algo ha ido mal en el chequeo"

		else:
			return "El coche esta parado"

	def estado(self):
		print("El coche tiene",self.__ruedas,"ruedas. Un ancho de",self.anchoChasis,"y un largo de",self.largoChasis)

	# Encapsulamos el método con __, para que no se pueda acceder fuera de la clase
	def __chequeo_interno(self):
		print("Realizando chequeo interno")

		self.gasolia = "ok"
		self.aceite = "ok"
		self.puertas = "cerradas"

		if (self.gasolia == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
			return True

		else:
			return False

# Creamos un objeto de la clase Coche
miCoche = Coche()

print("El largo del coche es",miCoche.largoChasis)
print(miCoche.arrancar(True))

print(miCoche.estado())

print("--------------A continuación creamos el segundo objeto--------------")

miCoche2 = Coche()

# Modificar el valor de una propiedad o atributo
miCoche2.largoChasis = 50000

print("El largo del coche es: ",miCoche2.largoChasis)
print(miCoche2.arrancar(False))
print(miCoche2.estado())

