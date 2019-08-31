import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()


#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='CONFECCION'")

# ACTUALIZAR UNA TABLA
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=50 WHERE NOMBRE_ARTICULO='PELOTA'")

# Guardar los valores de la consulta
#productos = miCursor.fetchall()

#print(productos)

# BORRAR UN ARTICULO
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")


miConexion.commit()

miConexion.close()