from io import open

# Abrimos un archivo en modo lectura (r)
archivo_texto2 = open("archivo.txt","r")

# Lee el archivo y lo guarda el contenido leído en una variable
texto = archivo_texto2.read()

# Cerramos el archivo
archivo_texto2.close()

# Imprimimos el contenido que ha leido
print(texto)