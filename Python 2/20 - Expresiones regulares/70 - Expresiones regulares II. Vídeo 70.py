import re

lista_nombres=['Marc Villalobos','Ana Gomez','Maria Martin','Marc Lopez','ninos','ninas']


for elemento in lista_nombres:

	# Busca todos los que empiezan por Marc
	if re.findall('^Marc', elemento):

		print(elemento)

	# Busca todos los que acaban con Martin
	if re.findall('Martin$',elemento):

		print(elemento)

	# Busca todos los que empiezan por nin, oa, s
	if re.findall('nin[oa]s', elemento):

		print(elemento)


lista_dominios=['http://www.google.es',
				'http://www.youtube.com',
				'ftp://www.youtube.com']

for elemento in lista_dominios:

	# Busca todos los que acaban con 'es'
	if re.findall('es$', elemento):

		print(elemento)

	# Busca todos los que empiezan con 'ftp'
	if re.findall('^ftp', elemento):

		print(elemento)

	# Busca si hay el caracter y
	if re.findall('[y]', elemento):

		print(elemento)