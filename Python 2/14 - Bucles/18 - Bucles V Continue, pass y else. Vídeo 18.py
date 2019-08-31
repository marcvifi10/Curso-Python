for letra in "Python":

	# Ignoramos la h
	if letra == "h":
		continue

	print("Viendo la letra " + str(letra))

nombre = "Marc"
contador = 0

for i in nombre:
	if i == " ":
		continue
	contador += 1

print("\nCantidad de caracteres del nombre: ", len(nombre))
print("\nCantidad de caracteres del nombre: ", contador)


email = input("Introduce un email: ")

for i in email:
	if i == "@":
		arroba = True
		break;

	else:
		arroba = False

print(arroba)


# Ctrl + c, para salir
while True:
	pass