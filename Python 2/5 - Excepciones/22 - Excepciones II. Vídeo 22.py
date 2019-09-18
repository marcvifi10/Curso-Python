def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):	
	
	# Intenta esto
	try:	
		return num1/num2

	# except + tipo_de_excepcion
	except ZeroDivisionError:
		print("No se puede dividir un numero por 0!!!")
		return "Operacion erronea"

while True:
	#Excepción tipo de valor
	try:
		op1=(int(input("Introduce el primer número: ")))

		op2=(int(input("Introduce el segundo número: ")))

		break

	except ValueError:
		print("Los valores introducidos no son correctos!!! Intentalo de nuevo")

	# Siempre de va a ejecutar
	finally:
		print("Operación comprobada!!!")
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")