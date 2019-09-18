from io import open 

# Abrimos un texto en modo escritura (w)
archivo_texto=open("archivo.txt","w")

# Escribimos contenido en el archivo creado
frase = "Este es un ejemplo \n de escritura"
archivo_texto.write(frase)

# Cerramos el archivo
archivo_texto.close()

