salario_pr = int(input("Introduce el salario del presidente: "))
print("Salario presidente: "+ str(salario_pr))

salario_dir = int(input("Introduce el salario del director: "))
print("Salario director: "+ str(salario_dir))

salario_area = int(input("Introduce el salario del Jefe de Area: "))
print("Salario Jefe Area: "+ str(salario_area))

salario_a = int(input("Introduce el salario del administrativo: "))
print("Salario administrativo: "+ str(salario_a))

if salario_a < salario_area < salario_dir < salario_pr:
	print("Todo correcto!!!")

else:
	print("ERROR!!!")