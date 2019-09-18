import sqlite3

# Establecemos la conexion con la BDD
# Si no existe, la crea
miConexion = sqlite3.connect("PrimeraBase")

# Creamos un cursor
miCursor = miConexion.cursor()

# Creamos una tabla ejecutando la instruccion SQL
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# Insertamos informacion
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',25,'DEPORTES')")

# Confirmamos los cambios de la tabla
miConexion.commit()


miConexion.close()