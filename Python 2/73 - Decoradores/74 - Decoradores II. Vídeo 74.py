def funcion_decoradora(funcion_parametro):

	# *args determina que las funciones reciben valores por parametros
	# **kwargs permite llamar a la funcion de esta manera: potencia(base=5,exponente=3)
	def funcion_interior(*args, **kwargs):

		# Acciones adicionales que decoran

		print("Vamos a realizar un calculo: ")

		# *args determina que las funciones reciben valores por parametros
		funcion_parametro(*args, **kwargs)

		# Acciones adicionales que decoran

		print("Hemos terminado el calculo")

		print("\n")

	return funcion_interior


@funcion_decoradora
def suma(num1,num2):

	print(num1+num2)

@funcion_decoradora
def resta(num1,num2):

	print(num1-num2)

@funcion_decoradora
def potencia(base,exponente):

	print(base**exponente)

suma(7,5)

resta(12,10)

potencia(base=5,exponente=3)