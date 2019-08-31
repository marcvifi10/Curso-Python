# Conjuntos

# Creamos dos conjuntos con elementos
a = {1,2,3}
b = {3,4,5}

# Si los dos conjuntos tienen los mismos elementos, aunque esten desordenados, los dos son iguales
print(a == b)

# Para saber el numero de valores que tiene el conjunto
print(len(a))

# Unir dos conjuntos
c = a | b
print(c)

# Interseccion de dos conjuntos
# Elementos que estan en el conjunto a y b
d = a & b
print(d)

# Diferencia de dos conjuntos
# Elementos que solo estan en el conjunto a
e = a - b
print(e)

# Diferencia de dos conjuntos
# Elementos que solo estan en el conjunto b
f = b - a
print(f)

# Diferencia simetrica
# Elementos que estan en a y b, pero no en los dos
g = a ^ b
print(g)

# Si h es un subconjunto de i
# Si todos los elementos de h estan dentro de i
h = {1,2,3}
i = {1,2,3,4,5,6}

print(h.issubset(i))

# Si i es un superconjunto de h
# Si en i hay todos los elementos de h
print(i.issuperset(h))

# Si ambos conjuntos son disconexos
# No tienen ningun elemento en comun
j = {1,2,3}
k = {3,4,5,6}

print(j.isdisjoint(k))

# Conjuntos immutables
# No podremos agregar más elementos a nuestro conjunto
l = frozenset({1,2,4})

