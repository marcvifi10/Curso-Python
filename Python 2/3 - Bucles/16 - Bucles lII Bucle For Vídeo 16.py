# Comienza por el 5 hasta el 10
for i in range(5,10):
	print(f"valor de la variable {i}")

# Comienza por el 5 hasta el 50, saltando de 3 en 3
for i in range(5,50,3):
	print(f"valor de la variable {i}")

# Validar un email
valido = False

email = input("Entra un email: ")

for i in range(len(email)):
	if email[i] == "@":
		valido = True

if valido:
	print("Correcto!!!")

else:
	print("Incorrecto!!!")