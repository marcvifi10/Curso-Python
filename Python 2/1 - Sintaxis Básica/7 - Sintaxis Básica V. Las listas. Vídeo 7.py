lista = ["Marc","Alex","Juan"]

print(lista[:])

print(lista[:2])

print(lista[1:2])

print(lista[1:3])

# Añadimos un nuevo valor a la lista
lista.append("Marina")

# Devuelve la posición del valor
print(lista.index("Marc"))

# Muestra si el valor esta dentr de la lista
print("Alex" in lista)

# Añadimos más valores a la lista
lista.extend(["N","J"])

# Eliminamos el valor con el valor "Marc"
print(lista)
lista.remove("Marc")
print(lista)

# Eliminar el último elemento de la lista
lista.pop()
print(lista)

# Juntamos dos listas
lista2 = [1,2,3]
lista3 = [4,5,6]

lista4 = lista2 + lista3

print(lista4)