# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:33:45 2019

@author: Andres
"""

from tkinter import *
raiz = Tk()
miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

nombreLable = Label(miFrame, text="Nombre: ")
nombreLable.grid(row=0, column=0, sticky="w", padx=2, pady=5)

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, pady=5)
cuadroNombre.config(fg="red", justify="right")

ApellidoLable = Label(miFrame, text="Apellido: ")

ApellidoLable.grid(row=1, column=0, sticky="w", padx=2, pady=5)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, pady=5)

DireccionLable = Label(miFrame, text="Direccion de casa: ")
DireccionLable.grid(row=3, column=0, sticky="w", padx=2, pady=5)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, pady=5)


PassLable = Label(miFrame, text="Password: ")
PassLable.grid(row=2, column=0, sticky="w", padx=2, pady=5)

cuadroPass = Entry(miFrame, show="*", bg="blue", cursor="dot")
cuadroPass.grid(row=2, column=1, pady=5)
# cuadroPass.config(show="+")

raiz.mainloop()
