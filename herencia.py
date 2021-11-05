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

class furgoneta (vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return "la furgoneta estar cargado"
        else:
            return "la furgoneta no esta cargada"

  

class moto(vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="voy haciendo caballito"
    
    def estado(self):
        print("\nmarca: ", self.marca, "\nmodelo: ", self.modelo,
    "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera,
    "\nfrenando: ", self.frena, "\n", self.hcaballito )

class VElectricos(vehiculos):
    def __init__(self,marca,modelo):

        super().__init__(marca,modelo)
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True


miMoto=moto("honda", "cbr")

miMoto.caballito()

miMoto.estado() 

mifurgoneta=furgoneta("renault","kangoo")

mifurgoneta.arrancar()

mifurgoneta.estado()

print(mifurgoneta.carga(True))

class BiciElectrico(VElectricos,vehiculos):
    pass

miBici=BiciElectrico("venzo","tauros")


