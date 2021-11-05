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
    
ficheroApertura=open("los coches","rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:

    print(c.estado())