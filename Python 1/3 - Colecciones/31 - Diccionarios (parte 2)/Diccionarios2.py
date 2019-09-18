# Diccionarios

equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo"}

# Busca si hay un valor 13, y si no lo hay mostrará un mensaje de error
print(equipo.get(13,"No existe un jugador con ese dorsal"))

# Decimos si el valor numero 10 esta dentro del diccionario
print(10 in equipo)

# Mostrara solo las claves del diccionario
# En este caso son los dorsales
print(equipo.keys())

# Mostrara solo los valores del diccionario
# En este caso son los nombres
print(equipo.values())

# Mostrara todos los valores del diccionario
print(equipo.items())

# Mostrara cuantos elementos hay en el equipo
print("Número de jugadores: ",len(equipo))

# Borrar todos los valores del diccionario
equipo.clear()
print(equipo)