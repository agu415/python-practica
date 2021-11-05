import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

# miCursor.execute ('''
#     CREATE TABLE PRODUCTOS (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,     
#     NOMBRE_ARTICULO VARCHAR(50)UNIQUE, 
#     PRECIO INTEGER,
#     SECCION VARCHAR(20))
#     ''')

# productos=[

#     ( "pelota", 20, "jugueteria"),
#     ( "pantalon", 10, "ropa"),
#     ( "destornillador", 25, "herramientas"),
#     ( "jarron", 45, "ceramica"),
#     ( "pantalones", 34, "ropa"),

#  ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)


miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")



miConexion.commit()

miConexion.close()
 