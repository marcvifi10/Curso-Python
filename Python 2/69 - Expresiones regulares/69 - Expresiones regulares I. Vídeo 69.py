import re

cadena="Vamos a aprender expresiones regulares"

print(re.search("aprender",cadena))

print(re.search("aprenderrr",cadena))

textoBuscar = "aprender"

# Buscar el textoBuscar dentro de cadena
if re.search(textoBuscar, cadena) is not None:

	print("He encontrado el texto")

else:

	print("No he encontrado el texto")


textoEncontrado = re.search(textoBuscar,cadena)

# Numero de caracter donde empieza a encontrar el textoBuscar
print(textoEncontrado.start())

# Numero de caracter donde acaba a encontrar el textoBuscar
print(textoEncontrado.end())

# Devuelve los dos valores anteriores, donde empieza y donde finaliza la palabra o texto a buscar
print(textoEncontrado.span())

# Devuelve los strings que hemos buscado en una lista
# Si lo encuentra dos veces, lo mostrara dos veces
print(re.findall(textoBuscar,cadena))

# Mostrar las veces repetidas que hay el textoBuscar dentro de la cadena
print(len(re.findall(textoBuscar,cadena)))