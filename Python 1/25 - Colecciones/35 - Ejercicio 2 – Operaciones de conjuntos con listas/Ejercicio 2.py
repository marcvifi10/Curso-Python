# Ejercicio 2

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

# Elimine los elementos repetidos de las dos listas
a = set(lista1)
b = set(lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = list(a & b)

print(f"Union: {union}")
print(f"Solo elementos A: {soloA}")
print(f"Solo elementos B: {soloB}")
print(f"Intersección: {interseccion}")