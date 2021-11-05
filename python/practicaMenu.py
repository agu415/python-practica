from tkinter import *
from tkinter import messagebox


root=Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Juan", "Procesador de texto version 2021")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia")

def salirAplicacion():
    #valor=messagebox.askquestion("Salir","¿deseas salir de la app?")
    valor=messagebox.askokcancel("Salir","¿deseas salir de la app?")
    if valor==True:
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar","No es posible cerrar documento bloqueado")
    if valor==False:
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)


edicionMenu=Menu(barraMenu,tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")
edicionMenu.add_command(label="Borrar")


herramientaMenu=Menu(barraMenu,tearoff=0)


ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia",command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de...", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edicion", menu=edicionMenu)

barraMenu.add_cascade(label="Herramientas", menu=herramientaMenu)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)





root.mainloop()