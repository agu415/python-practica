from tkinter import *
from tkinter import filedialog



root=Tk()

def abreFichero():

    fichero=filedialog.askopenfilename(tittle="Abrir", initialdir="C:", filetypes=(("ficheros de excel","*.xlsx"),("ficheros de texto","*.txt"),("todos los ficheros","*.*")))

    print(fichero)


Button(root,text="Abrir fichero", command=abreFichero).pack()


root.mainloop()