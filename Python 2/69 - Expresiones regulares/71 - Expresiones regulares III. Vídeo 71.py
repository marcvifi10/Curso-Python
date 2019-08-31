import re

lista_nombres=['Marc','Ana','Alex']

for elemento in lista_nombres:
	# Busca entre el rango [o-t] y [m-n]
	if re.findall('[o-tm-n]',elemento):
		print(elemento)