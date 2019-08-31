# MANERA 1
def generaPares(limite):
	num = 1

	miLista = []

	while num < limite:
		miLista.append(num*2)

		num = num + 1

	return miLista

print(generaPares(10))

# MANERA 2
def generaPares2(limite):
	num2 = 1

	while num2 < limite:
		# Almacenar los valores de uno en uno
		yield num2 * 2

		num2 = num2 + 1

devuelvePares2 = generaPares2(10)

for i in devuelvePares2:
	print(i)


#MANERA 3 - DEVOLVER LOS 3 PRIMEROS ELEMENTOS

def generaPares3(limite):
	num3 = 1

	while num3 < limite:
		# Almacenar los valores de uno en uno
		yield num3 * 2

		num3 = num3 + 1

devuelvePares3 = generaPares3(10)

# devuelve el primer valor almacenado
print()
print(next(devuelvePares3))

print("Aquí podria ir más codigo")

# devuelve el segundo valor almacenado
print(next(devuelvePares3))

print("Aquí podria ir más codigo")

# devuelve el tercer valor almacenado
print(next(devuelvePares3))

print("Aquí podria ir más codigo")

# devuelve el cuarto valor almacenado
print(next(devuelvePares3))
