from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=600, height=300)
miFrame.pack()

miNombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx=10,pady=10)

cuadroTexto=Entry(miFrame)
cuadroTexto.grid(row=2,column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=16, height=5)
textoComentario.grid(row=4,column=1, padx=10,pady=10)

scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=4,column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

nombreLabel=Label(miFrame,text="nombre: ")
nombreLabel.grid(row=0,column=0, sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="apellido: ")
apellidoLabel.grid(row=1,column=0, sticky="e",padx=10,pady=10)

direccinLabel=Label(miFrame,text="direccion: ")
direccinLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame,text="contraseña: ")
passLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

comentarioLabel=Label(miFrame,text="comentario: ")
comentarioLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

def codigoboton():
    miNombre.set("juan")


boton1=Button(raiz, text="Enviar", command=codigoboton)

boton1.pack()

raiz.mainloop()