print("Programa de becas Año 2017")

distancia_escuela = int(input("Introduce la distancia: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el numero de hermanos: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce el salario familiar: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000:
	print("Tienes derecho a la beca")

else:
	print("No tienes derecho a la beca")