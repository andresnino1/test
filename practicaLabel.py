#praccia label
from tkinter import Tk, Frame, Label, PhotoImage
root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

#se crea un objeto llamado miLabel 
#se identifica el contenedor donde va a ir el label --> miFrame
#se usa la opcion text para ingresar un texto
#miLabel=Label(miFrame, text="Hola Mundo")
#
##el modulo place hace referencia al lugar donde va el label
#miLabel.place(x=50, y=50)


#se crea una variable con la clase PhotoImage

miImagen=PhotoImage(file="r2d2.png")

#se utiliza la opcion IMAGE en vez del text
#
Label(miFrame, text="Hola Mundo", fg="red", cursor="arrow").place(x=50, y=270)


root.mainloop()
