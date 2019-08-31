def areaTriangulo(base,altura):

	"""
		Calcula el area de un triangulo

		>>> areaTriangulo(3,6)
		'El area del triangulo es: 9'

		>>> areaTriangulo(4,5)
		'El area del triangulo es: 10'

	"""

	return "El area del triangulo es: "+str((base*altura)/2)

import doctest
doctest.testmod()

# Si el resultado es 9 (resultado correcto), no devuelve nada
# Si el resultado es incorrecto, mostrara un mensaje de error
# Se tiene que escribir debajo de >>>areaTriangulo(3,6), exactamente lo que tiene que devolver