from io import open

#abrir archivo para agregar info "a"

# archivo_texto=open("archivo.txt","a")

# archivo_texto.write("\n siempre es una buena ocacion para estudiar python")

# archivo_texto.close()





#lectura "r"
archivo_texto=open("archivo.txt","r+") #lectura y escritura

archivo_texto.write("comienzo del texto")

lista_texto=archivo_texto.readlines();

lista_texto[1]="esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()

#print(archivo_texto.readlines())

# archivo_texto.seek(len(archivo_texto.readline()))

# print(archivo_texto.read())

#archivo_texto.seek(11)

# print(archivo_texto.read(11))

# print(archivo_texto.read())




#escritura "w"
# archivo_texto=open("archivo.txt","w")

# frase="estupendo dia para estudiar python \n el miercoles"

# archivo_texto.write(frase)

# archivo_texto.close()