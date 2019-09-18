midiccionario = {"Alemania":"Berlina","España":"Madrid","Francia":"Paris"}

# Mostramos la capital de Francia
print(midiccionario["Francia"])

# Añadimos otro valor al diccionario
midiccionario["Italia"] = "Roma"
print(midiccionario["Italia"])

# Modificar un valor
midiccionario["Italia"] = "Roma2"
print(midiccionario["Italia"])

# Eliminar un elemento
print(midiccionario)
del midiccionario["Francia"]
print(midiccionario)

# Creamos una tupla
tupla = ["España","Francia","Italia","Alemania"]
# Asignamos un valor a cada valor de la tupla
diccionario2 = {tupla[0]:"Madrid",tupla[1]:"Paris",tupla[2]:"Roma",tupla[3]:"Berlin"}
print(diccionario2)

diccionario3 = {23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"temporadas":[1991,1992,1993,1994]}}
print(diccionario3["Anillos"])
# Mostrar las claves, NO los valores
print(diccionario3.keys())
# Mostrar los valores, NO las claves
print(diccionario3.values())
# Mostrar cuantos valores tiene el diccionario
print(len(diccionario3))
print(diccionario3)