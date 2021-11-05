import pickle


#>>>>> leer un fichero binario
fichero=open("lista_nombre","rb")

lista=pickle.load(fichero)

print(lista)





#>>>>>>>> crear archivo binario
# lista_nombre=["pedro","anita","maria","juan"]

# fichero_binario=open("lista_nombre","wb") #"wb" writte binari

# pickle.dump(lista_nombre, fichero_binario)

# fichero_binario.close()

# del (fichero_binario)
