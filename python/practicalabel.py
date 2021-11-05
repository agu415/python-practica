from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

#miImagen=PhotoImage(file="mouse.gif")

#Label(miFrame, imagen=miImagen) >>>>>> ingreso de imagenes gif y png

Label(miFrame, text="hola alumnos de python", fg="red" ,font=("Comics Sans MS",18)).place(x=100, y=200)




root.mainloop()

