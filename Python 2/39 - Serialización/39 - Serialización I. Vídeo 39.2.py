import pickle

# rb = read binary
fichero = open("lista_nombres","rb")

lista = pickle.load(fichero)

print(lista)