class Persona:
	def __init__(self, nombre, edad, lugar_residencia):

			self.nombre = nombre
			self.edad = edad
			self.lugar_residencia = lugar_residencia

	def descripcion(self):

		print("-----PERSONA-----","\nNombre:",self.nombre,"\nEdad:",self.edad,"\nLugar de residencia:",self.lugar_residencia)

class Empleado(Persona):

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

		# Llamamos al constructor de la clase padre, con la palabra super()
		super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
		
		self.salario = salario
		self.antiguedad = antiguedad

	# Sobreescribimos el metodo descripcion
	def descripcion(self):

		# Llamamos al metodo de la clase padre, con la palabra super()
		super().descripcion()

		print("Salario:",self.salario,"\nAntiguedad:",self.antiguedad,"\n")


Marc = Persona("Marc",22,"Girona")

Marc.descripcion()

Antonio = Empleado(1500, 15, "Antonio", 55, "Colombia")

Antonio.descripcion()

# Comprobamos si el objeto Antonio, pertenece a la clase Empleado
print("¿Antonio pertenece a la clase Empleado?",isinstance(Antonio, Empleado))
