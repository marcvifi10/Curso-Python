# TUPLAS

# Declaramos una tupla
tupla1 = (1,2,3,"a","b")

# Mostramos una tupla entera
tupla2 = (1,2,3,4,5,6)
print("1 - Mostrando una tupla: ", tupla2)

#Mostramos una posición concreta de una tupla
tupla3 = ("a","b","c","d","e","f")
print("2 - Mostrando la posicion 3 de la tupla: ", tupla3[2])

# Mostramos una tupla de la posición 1 hasta el final
tupla4 = (1,2,3,2,3,5,6,5)
print("3 - Mostrando una tupla de la posición hasta el final: ", tupla4[1:])

# Comprobamos si el elemento 4 esta en la tupla5
tupla5 = (1,2,3,4,5,6,7,8,9)
print("4 - Comprobamos si el elemento 4 esta en la tupla: ", 4 in tupla5)

# Mostramos el elemento que se encuentra en la posición 5
tupla6 = (1,2,3,4,5,6,7,8)
print("5 - Mostramos el elemento que se encuentra en la posición 5: ", tupla6.index(5))

# Contamos las veces que se repite el elemento que esta entre parentesis
tupla7 = ("a","b","c","d","e","a")
print("6 - Contamos las veces que se repite el elemento que esta entre parentesis: ", tupla7.count("a"))

# Contamos los elementos que tiene la tupla
tupla8 = (1,2,3,4,5,6,7)
print("7 - Contamos los elementos que tiene la tupla: ", len(tupla8))

# Convertimos una tupla a una lista
tupla9 = (4,5,"Hola")
lista1 = list(tupla9)
print("8 - Convertimos una tupla a una lista: ", lista1)

# Convertimos una lista a una tupla
lista2 = [1,2,3,4]
tupla10 = tuple(lista2)
print("8 - Convertimos una lista a una tupla: ", tupla10)