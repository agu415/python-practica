import pickle

class persona:

    def __init__(self,nombre,genero,edad):
       self.nombre=nombre
       self.genero=genero 
       self.edad=edad
       print("se ha creado una persona con el nombre de: ", self.nombre)
    
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
class listaPersonas:
    
    personas=[]

    def __init__(self):

        listaDePersonas=open("ficheroExterno","ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print ("cargaron {} personas del fichero externo".format(len(self.personas)))
         
        except: 
            print("el fichero esta vacio")
        
        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    
    def guardarPersonasFicheroExterno(self):
        listaPersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("la informacion del fichero externo es el siguiente: ")
        for p in self.personas:
            print(p)

misLista=listaPersonas()
persona=persona("sandra","femenino", 29)
misLista.agregarPersonas(persona)
misLista.mostrarInfoFicheroExterno()



