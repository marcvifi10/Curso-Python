import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

# Creamos una tabla con una clave primaria
# UNIQUE = no se pueden repetir el nombre_articulo
miCursor.execute('''
		CREATE TABLE PRODUCTOS (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
		PRECIO INTEGER,
		SECCION VARCHAR(20))
	''')

# Creamos una lista de productos
productos = [

		("PELOTA",20,"JUGUETERIA"),
		("PANTALON",15,"CONFECCION"),
		("DESTORNILLADOR",25,"FERRETERIA"),
		("JARRON",45,"CERAMICA")
]

# Insertamos los valores
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)


miConexion.commit()

miConexion.close()