def compruebaMail(mail):

	"""
		La funcion compruebaMail evalua un mail
		recibido en busca de la @. Si tiene una @
		es correcto, si tiene mas de una @ es incorrecto
		si la @ esta al final es incorrecto


		>>> compruebaMail('marcvifi10@outlook.es')
		True

		>>> compruebaMail('marcvifi10outlook.es@')
		False

		>>> compruebaMail('marcvifi10outlook.es')
		False

		>>> compruebaMail('marcvifi10@@outlook.es@')
		False

	"""

	arroba = mail.count('@')

	if(arroba!=1 or mail.rfind('@')==(len(mail)-1) or mail.find('@')==0):
		return False

	else:
		return True


import doctest
doctest.testmod()