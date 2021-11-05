class coche():

    def desplazamiento(self):
        print("me desplazo utilizando cuatro ruedas")

class moto():

    def desplazamiento(self):
        print("me desplazo utilizando dos ruedas")

class camion():
    def desplazamiento(self):
        print("me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=camion()

desplazamientoVehiculo(miVehiculo)