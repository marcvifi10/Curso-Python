# Ejercicio 4

num1 = float(input("Entra un numero: "))
num2 = float(input("Entra otro numero: "))

op = input("\nEntra la operacion a realizar: ")
op = op.lower()

if op == 's':
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}.")

elif op == 'r':
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}.")

elif op == 'm' or op == 'p':
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}.")

elif op == 'd':
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}.")
