def devuelve_ciudades(*ciudades): # Con el *, podemos pasarle los elementos que queramos
	for elemento in ciudades:
		for subElemento in elemento:
			# Devolver el elemento
			yield subElemento

ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Valencia","Girona")

# Mostramos la primera letra del primer valor
print(next(ciudades_devueltas))

# Mostramos la segunda letra del primer valor
print(next(ciudades_devueltas))



def devuelve_ciudades2(*ciudades2): # Con el *, podemos pasarle los elementos que queramos
	for elemento in ciudades2:
		yield elemento

ciudades_devueltas2 = devuelve_ciudades2("Madrid","Barcelona","Valencia","Girona")

# Mostramos el primer valor
print(next(ciudades_devueltas2))

# Mostramos el segundo valor
print(next(ciudades_devueltas2))