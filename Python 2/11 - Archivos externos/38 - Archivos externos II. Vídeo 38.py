from io import open

# Abrimos el archivo em modo lectura (r), modo escritura o añadir texto (a)
# r+ = lectura + escritura
archivo_texto = open("archivo.txt","r+")

print(archivo_texto.read())

# Situa el cursor en la posición 0
archivo_texto.seek(0)

print()
print(archivo_texto.read())

# Situamos el cursor en la posición o caracter 11 por defecto
archivo_texto.seek(11)
print()
# Lee el archivo
print(archivo_texto.read())

# Lee el archivo hasta el caracter 11
print(archivo_texto.read(11))

# Situamos el puntero justo en la mitad del archivo
archivo_texto.seek(len(archivo_texto.read()/2))
print(archivo_texto.read())

# Situamos el cursor al final de la primera linea
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())

# Añadimos el texto en la primera linea de texto, y luego se vera el texto anterior
archivo_texto.write("CCC")

# Nos devuelve una lista, con las lineas de texto
print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines()

# Modificamos el valor de la linea 2
lista_texto[1] = "Esta linea ha sido incluida desde el exterio \n"

# Llevamos el cursor a la posición 0
archivo_texto.seek(0)

# Escribimos la secuencia de cadenas (todas) con writelines
archivo_texto.writelines(lista_texto)

# Cerramos el archivo
archivo_texto.close()