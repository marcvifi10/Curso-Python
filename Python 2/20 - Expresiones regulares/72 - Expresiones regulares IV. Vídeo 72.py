import re

nombre1="marc Villalobos"
nombre2="Javi Gomez"
nombre3="Maria Lopez"

# Busca Marc en la variable nombre1
# Para hace que la busqueda NO sea sensible a minusculas y mayusculas utilizamos re.IGNORECASE
if re.match("Marc",nombre1,re.IGNORECASE):

	print("Hay un Marc!!!")

# Busca los nombres que empiezen por una letra cualquiera, y a continuacion ar
if re.match(".ar",nombre1,re.IGNORECASE):

	print("Hemos encontrado el nombre")

else:

	print("No lo hemos encontrado!!!")

# \d = Busca si comienza por un numero
# search("Lopez",nombre2) = Busca si hay la palabra Lopez en cualquier punto
