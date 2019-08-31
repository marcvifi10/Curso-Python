for i in [1,2,3,4,5]:
	print("Hola", end=" ")

print("\n")

for i in [1,2,3,4,5,8]:
	print(i, end=" ")

contador = 0
email = False

for i in "marcvifi10@outlook.es":
	if (i == "@" or i == "."):
		contador += 1

if contador == 2:
	print("Email Correcto!!!")

else:
	print("Email Falso!!!")

for i in range(5):
	print("Hola")