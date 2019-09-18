# Condicionales combinados

edad = int(input("Entra una edad: "))

if edad > 0:
    print("\nEdad correcta")

    if edad >= 18:
        print("\nEs mayor de edad.")

    else:
        print("\nEs menor de edad.")

else:
    print("\nEdad incorrecta")