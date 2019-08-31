# Bucle While

import math

numero = int(input("Entra un numero: "))

while numero < 0 or numero == 0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Entra un numero: "))

# Mostrar la raíz cuadrada del numero con solo 2 decimales
print(f"\nSu raíz cuadrada es: {(math.sqrt(numero)):.2f}")