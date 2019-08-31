# Diccionarios

# Creamos un diccionario y le añadimos valores
diccionario = {"azul":"blue","rojo":"red","verde":"green"}

# Agregamos más elementos al diccionario
diccionario["amarillo"] = "yellow"

# Modificamos el valor de uno de los elementos del diccionario
diccionario["azul"] = "BLUE"

# Mostramos todos los elementos
print(diccionario)

# Eliminamos uno de los elementos del diccionario
del(diccionario["amarillo"])

# Mostramos todos los elementos
print(diccionario)

# Mostramos solo el color azul
print(diccionario["azul"])

# Creamos una lista dentro de un diccionario
diccionario2 = {"Marc":[22,1.85],"Alex":[19,1.70]}

print("MARC:",diccionario2["Marc"])