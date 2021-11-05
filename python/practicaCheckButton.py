from tkinter import *

root=Tk()

root.title("ejemplo")

playa=IntVar()
montagna=IntVar()
cuidad=IntVar()

def opcionesViaje():

    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+="playa"

    if(montagna.get()==1):
        opcionEscogida+="montaña"
    
    if(cuidad.get()==1):
        opcionEscogida+="cuidad"

    textoFinal.config(text=opcionEscogida)

#foto=PhotoImagen(file="avion.png")
#label(root, imagen=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame,text="elige destino", width=50).pack()


Checkbutton(root, text="playa",variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="cuidad",variable=cuidad, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()