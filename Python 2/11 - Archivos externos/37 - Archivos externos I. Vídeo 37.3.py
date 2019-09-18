from io import open

# Abrimos un archivo en modo lectura (r)
archivo_texto3 = open("archivo.txt","r")

# Guarda la información en una lista
lineas_texto = archivo_texto3.readlines()

# Cerramos el archivo
archivo_texto3.close()

# Imprimimos el contenido leído
print(lineas_texto)

# Imprimimos la primera linea
print(lineas_texto[0])

# Imprimimos la segunda linea
print(lineas_texto[1])