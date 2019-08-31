nombreUsuario = input("Entra un nombre: ")

print("El nombre es:",nombreUsuario)

# Pasamos el nombre a mayusculas
print("El nombre es:",nombreUsuario.upper())

# Pasamos el nombre a minusculas
print("El nombre es:",nombreUsuario.lower())

# Pasamos el nombre la primera letra en mayusculas, y el resto en minusculas
print("El nombre es:",nombreUsuario.capitalize())


edad = input("Entra una edad:")

# Comprueba si el valor es un digito
print(edad.isdigit())

while (edad.isdigit() == False):
	print("Entra un valor numerico!!!")
	edad = input("Entra una edad:")


if (int(edad) < 18):
	print("No puede pasar")

else:
	print("Puedes pasar")




