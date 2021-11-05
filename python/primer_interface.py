from tkinter import *

raiz=Tk()

raiz.title("ventana de prueba")

raiz.resizable(1,1)

#raiz.geometry("650x350")

miFrame=Frame()

miFrame.pack(side="left", anchor="n")

miFrame.config(bg="red")

miFrame.config(width="640", height="350")

miFrame.config(relief="groove")

miFrame.config(bd=35)


raiz.mainloop()