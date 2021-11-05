from tkinter import *

root=Tk()

varOption=IntVar()

Label(root, text="Genero: ").pack()

def imprimir():

    #print(varOption.get())

    if varOption.get()==1:
        
        etiqueta.config(text="has elegido masculino")

    elif varOption.get()==2:

        etiqueta.config(text="has elegido femenino")

    else:
         
        etiqueta.config(text="has elegido otras opciones")

Radiobutton(root, text="masculino", variable=varOption, value=1, command=imprimir).pack()

Radiobutton(root, text="femenino", variable=varOption, value=2, command=imprimir).pack()

Radiobutton(root, text="otras opciones", variable=varOption, value=3, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()



root.mainloop()
