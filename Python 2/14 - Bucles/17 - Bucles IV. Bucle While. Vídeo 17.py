# EJEMPLO 1
i = 1

while i < 10:
	print("Ejecucion " + str(i))
	i += 1

print("\nTerminó el programa\n\n")


# EJEMPLO 2
edad = int(input("Entra una edad: "))

while edad <= 0 or edad > 110:
	print("Edad incorrecta!!! \nVuelve a intentarlo. ")
	edad = int(input("\nEntra una edad: "))

print("Edad del aspirante: " + str(edad))


# RAÍZ CUADRADA
import math

print("\n\nPrograma de cálculo de raíz cuadrada")
numero = int(input("Entra un numero: "))

intentos = 0

while numero < 0:
	print("No se puede calcular!!!")

	if intentos == 2:
		print("Has consumido demasiados intentos.")
		break;

	numero = int(input("Entra un numero: "))

	if numero < 0:
		intentos = intentos + 1

if intentos < 2:
	solucion = math.sqrt(numero)
	print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))


