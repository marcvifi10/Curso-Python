# Ejercicio 5

saldo = 1000

print("\t.:MENU:.")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")

op = int(input("\nOpcion: "))

if op == 1:
    extra = float(input("Cuanto dinero desea ingresar: "))
    saldo += extra
    print(f"Saldo actual: {saldo}")

elif op == 2:
    retirada = float(input("Cuanto dinero desea retirar: "))

    if retirada > saldo:
        print("ERROR!!!")

    else:
        saldo -= retirada
        print(f"Saldo actual: {saldo}")

elif op == 3:
    print(f"Dinero en la cuenta: {saldo}")

elif op == 4:
    print("Gracias por utilizar el cajero automático")

else:
    print("ERROR!!!")