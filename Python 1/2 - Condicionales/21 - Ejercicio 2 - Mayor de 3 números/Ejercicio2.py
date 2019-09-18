# EJERCICIO 2

num1 = int(input("Entra un primer numero: "))
num2 = int(input("Entra un segundo numero: "))
num3 = int(input("Entra un tercer numero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El numero mayor es {num1}.")

elif num2 >= num1 and num2 >= num3:
    print(f"El numero mayor es {num2}")

elif num3 >= num1 and num3 >= num2:
    print(f"El numero mayor es {num3}")