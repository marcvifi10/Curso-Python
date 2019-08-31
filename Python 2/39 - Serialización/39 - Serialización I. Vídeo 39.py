import pickle

lista_nombres = ["Marc","Alex","Jose"]

# Creamos un archivo (lista_nombres), y lo abrimos con los permisos de escritura binaria (wb)
fichero_binario = open("lista_nombres","wb")

# Bolcamos la lista a ese fichero externo
pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

# Borramos el fihero de la memoria
del (fichero_binario)