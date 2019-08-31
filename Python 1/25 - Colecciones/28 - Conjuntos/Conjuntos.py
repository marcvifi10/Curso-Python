# Conjuntos

# Creamos un conjunto vacio
# La palabra set determina que es un conjunto
conjunto = set()

# El conjunto lo dejamos vacio
conjunto = {}

# Para agregar elementos hacemos lo siguiente
# No puede tener otro conjunto dentro (listas, diccionarios...)
# Si al agregar, añades dos elementos iguales, solo de mostrarán una vez por pantalla
conjunto = {1,2,3,"Hola",5,6,7,1,2}

# Para agregar más elementos al conjunto, hacemos lo siguiente
conjunto.add(8)
conjunto.add("Adios")
conjunto.add('a')

# Para eliminar elementos del conjunto, hacemos lo siguiente
conjunto.discard('a')

# Para eliminar todos los elementos del conjunto
conjunto.clear()

conjunto.add(3)

print(conjunto)

# Para determinar si un elemento esta dentro del conjunto
print(3 in conjunto)

# Para determinar si un elemento no esta dentro del conjunto
print(3 not in conjunto)