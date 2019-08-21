from tkinter import Tk, Frame
raiz=Tk()
raiz.title("ventana inicial")#pone el titulo a la ventana
#raiz.resizable(0,0) #ancho y alto ambos en falso y no se puede redimensionar
                    #0,0 --> ancho y alto no se podrán modificar
                    #1,1 --> se pueden redimensionar en ancho y alto
raiz.iconbitmap("robot.ico")#coloca el icono de la parte superior izquierda de la ventana
                            #elicono se usa con una imagen con extención .ico
                            #en internet hay conversores a ico 
                            #cuando se empaqueta la aplicación este icono será el usado 
#raiz.geometry("650x350")    # ancho y alto
raiz.config(bg="blue")      #bg-->background 


#se crea un frame
miFrame = Frame() 

#se debe empaquetar, este comando hace que el frame se meta dentro de la raiz
#las opciones de empaquetado --> se cambia la posicion y comportamiento del frame
#side = right -- el frame se queda anclado a la derecha cuando se redimenciona
#anchor -- se especifica norte (n) sur (s) oriente occidente para que el frame
#que quede en ese lugar
#n, ne, e, se, s, sw, w, nw, or center


#para rellenar el frame cuando se expande

# el frame se va expandiendo horizontalmente cuando se redimenciona la ventana
miFrame.pack()

miFrame.config(bd=7) #determina el grosor del borde
miFrame.config(relief="groove") #determina el tipo de borde

#Método para configurar el fondo del frame
miFrame.config(bg="red")

#Método para cambiar el tamaño del frame
#La raiz se adapta al tamaño del frame interno, por esto no se debe poner tamaño a la raiz
miFrame.config(width="650", height="350") #


raiz.mainloop()
