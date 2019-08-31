def areaCuadrado(lado):

	"""Calcula el area de un cuadrado elevando 
	al cuadrado el lado pasado por parametro"""

	return "El area del cuadrado es: " + str(lado*lado)

def areaTriangulo(base,altura):

	"""Calcula el area de un triangulo
	gracias a la altura y la base pasados
	 por parametro"""
	return "El area del triangulo es: " + str(base*altura)

print(areaCuadrado(5))
# Imprime por pantalla el comentario
print(areaCuadrado.__doc__)

help(areaTriangulo)

print(areaTriangulo(2,3)