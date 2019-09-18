# Ejercicio 1

num1 = int(input("Entra un numero: "))
num2 = int(input("Entra otro numero: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos son pares.")

elif num1 % 2 == 0 and num2 % 2 != 0:
    print(f"El numero {num1} es par.")

elif num1 % 2 != 0 and num2 % 2 == 0:
    print(f"El numero {num2} es par.")

else:
    print("Ambos numeros son impares.")