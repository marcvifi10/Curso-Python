lista = [1,2,3,1]

# Convertimos una lista en una tupla
tupla = tuple(lista)

# Verificamos si el valor 1 esta dentro de la tupla
print(1 in tupla)

# Contamos cuantas veces se repite el valor 1 en la tupla
print(tupla.count(1))

# Contamos cuantos elementos tiene la tupla
print(len(tupla))

mitupla = ("Juan",1,12,1996)
nombre, dia, mes, agno = mitupla
print(nombre)
print(mes)
print(agno)