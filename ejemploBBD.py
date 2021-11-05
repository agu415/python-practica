import sqlite3

miConexion=sqlite3.connect("primerBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NombreArticulo VARCHAR (50), PRECIO INTEGRER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15,'DEPORTE')")

#variosProductos=[
    
#     ("Camiseta", 10, "Deportes"),
#     ("Jarron", 10, "Ceramica"),
#     ("camion", 10, "Jugueteria")

#    ]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos= miCursor.fetchall()

print(variosProductos)

miConexion.commit()


miConexion.close()