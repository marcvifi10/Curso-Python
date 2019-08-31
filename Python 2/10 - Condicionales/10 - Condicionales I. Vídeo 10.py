print("2 - Programa de evaluacion: ")
nota_alumno = input("Entra una nota: ")

def evaluacion(nota):
	valoracion = "Aprobado"
	if nota < 5:
		valoracion = "Suspendido!!!"
		print(f"{valoracion}")
	else:
		valoracion = "Aprobado!!!"
		print(f"{valoracion}")

	return valoracion

print(evaluacion(int(nota_alumno)))