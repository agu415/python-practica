import pickle
class vehiculos():

    def __init__(self, marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):

        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("\nmarca: ", self.marca, "\nmodelo: ", self.modelo,
    "\n En marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera,
    "\nfrenando: ", self.frena)

coche1=vehiculos("mazda","mx4")

coche2=vehiculos("nissan","frontier")

coche3=vehiculos("seat","leon")

coches=[coche1,coche2,coche3]

fichero=open("los coches","wb")

pickle.dump(coches, fichero)

fichero.close() 

del (fichero)

