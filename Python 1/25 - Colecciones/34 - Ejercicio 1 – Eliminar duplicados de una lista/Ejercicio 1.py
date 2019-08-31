# Ejercicio 1

lista = [1,2,3,"Marc",2,2,1,"Marc",3]

# Pasamos la lista a conjunto, para que se eliminen los elementos repetidos
conjunto = set(lista)

# Pasamos el conjunto a lista
lista = list(conjunto)

print(conjunto)
print(lista)