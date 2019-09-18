# EJERCICIO 3

letra = input("Entra una letra: ")
letra = letra.lower() # Pasamos la letra a minusculas

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print(f"La letra {letra} es una vocal.")

else:
    print(f"La letra {letra} NO es una vocal.")