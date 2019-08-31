def evaluaEdad(edad):

	if edad < 0:
		# Lanzamos una excepcion con la palabra raise
		raise TypeError("No se permiten edades negativas")
		raise ZeroDivisionError("No se permiten edades negativas")

	if edad < 20:
		return "eres muy joven"

	elif edad < 40:
		return "eres joven"

	elif edad < 65:
		return "eres adulto"

	elif edad < 100:
		return "eres mayor"

print(evaluaEdad(-2))