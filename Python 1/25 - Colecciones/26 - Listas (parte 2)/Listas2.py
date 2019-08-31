# LISTAS

# Ejemplos de listas
lista_ejemplo1 = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
lista_ejemplo2 = [1,2,3]
lista_ejemplo3 = [4,5,6,1,2,3]
lista_ejemplo4 = [5,4,-7,9,0,1,3]

# Operaciones con las listas
# Juntamos las dos listas
lista1 = [1,2]
lista2 = [3,4]
lista3 = lista1 + lista2
print("1 - Juntamos las dos listas: ", lista3)

# Agregamos un elemento al final de la lista
lista4 = ["a","b","c"]
lista4.append("d")
print("2 - Agregamos un elemento al final de la lista: ", lista4)

# Agregamos a la posición 1 (i+1) el siguiente valor en la lista
lista5 = ["a","c","d","e"]
lista5.insert(1,"b")
print("3 - Agregamos en la posición [1] un valor: ", lista5)

# Añade al final de la lista un conjunto de valores
lista6 = [1,2,3,4,5,6]
lista6.extend([7,8,9])
print("4 - Añadimos al final de la lista un conjunto de valores: ", lista6)

# Preguntamos si el valor 3 esta dentro de la lista7
lista7 = [1,2,3,4]
print("5 - Preguntamos si el valor 3 se encuentra en la lista: ", 3 in lista7)

# Ordenar los elementos ascendentemente
lista8 = [3,2,6,4,8,1,-2,9,-6]
lista8.sort()
print("6 - Ordenamos la lista ascendentemente: ", lista8)

# Ordenar los elementos descendentemente
lista9 = [8,4,9,2,3,1,6,7]
lista9.sort(reverse=True)
print("7 - Ordenamos la lista descendentemente: ", lista9)

# Muestra la posición en la que se encuentra el valor dentro de la lista
lista10 = ["a","b","c","d","e","f"]
print("8 - Mostramos la posición el que se encuentra la letra 'd': ", lista10.index("d"))

# Muestra cuantas veces se repite el valor entre parentesis dentro de la lista
lista11 = [1,2,3,1,2,3,1,2,3,1,5,6,7]
print("9 - Mostramos las veces que se repite el numero 1 en la lista: ", lista11.count(1))

# Eliminamos de la lista el valor de la posición que hay entre parentesis
lista12 = [1,2,3,4,5,6,7,8]
lista12.pop(3)
print("10 - Eliminamos el elemento de la posición 3 de la lista: ", lista12)

# Elimina el elemento que hay entre parentesis
lista13 = [1,2,3,4]
lista13.remove(2)
print("11 - Eliminamos de la lista el elemento que esta entre parentesis: ", lista13)

# Mostrar la lista a la inversa
lista14 = [1,2,3,4,5]
lista14.reverse()
print("12 - Mostramos la lista al revés: ", lista14)

# Eliminar todos los elementos de la lista
lista15 = [1,2,3,4,5]
lista15.clear()
print("13 - Eliminamos todos los elementos de la lista: ", lista15)

# Muestra la cantidad de elementos que hay en la lista
lista16 = [1,2,3,4,5,6,7,8,9,10]
print("14 - Cantidad de elementos que tiene la lista: ", len(lista16))

#Mostramos todos los elementos de la lista
lista17 = [1,2,3,4,5,6,7,8,9,10]
print("15 - Elementos que tiene la lista: ", lista17[0:])


