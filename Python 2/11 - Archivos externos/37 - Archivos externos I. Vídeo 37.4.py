from io import open

# Abrimos un archivo para añadir información
archivo_texto4 = open("archivo.txt","a")

archivo_texto4.write("\nNueva linea")

# Cerramos el archivo
archivo_texto4.close()
