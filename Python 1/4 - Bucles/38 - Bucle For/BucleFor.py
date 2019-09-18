# Bucle for

coleccion = {"Marc":10,"Alex":11}

for i in [1,2,3,4,5,"Marc"]:
    print(i)

print("")

for i in coleccion:
    print(f"{i} -> {coleccion[i]}")

for clave,valor in coleccion.items():
    print(f"{clave} -> {valor}")

coleccion2 = "Marc"

for i in coleccion2:
    print(f"{i}")

for i in coleccion2:
    print(f"{i}",end="  ")

