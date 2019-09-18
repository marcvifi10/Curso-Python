import sqlite3

# Establecemos la conexion con la BDD
# Si no existe, la crea
miConexion = sqlite3.connect("PrimeraBase")

# Creamos un cursor
miCursor = miConexion.cursor()

# Creamos una tabla ejecutando la instruccion SQL
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# Insertamos informacion
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',25,'DEPORTES')")

#variosPrductos=[
	
#	("Camiseta",10,"DEPORTES"),
#	("Jarron",10,"CERAMICA"),
#	("Camion",10,"JUGUETERIA")


#]

# Para insertar mucha informacion ejecutamos lo siguiente
# Numero de ?, por numero de campos de la tabla
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosPrductos)

# Confirmamos los cambios de la tabla
#miConexion.commit()

# Ejecutamos una consulta
miCursor.execute("SELECT * FROM PRODUCTOS")

# Para ver la informacion
variosPrductos = miCursor.fetchall()

for producto in variosPrductos:

	print("Nombre Articulo:",producto[0],"\nSeccion:",producto[2])


miConexion.close()