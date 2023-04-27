#Se importa la libreria tkinter con todas sus funciones
from tkinter import *

#---------------------------------
#Funciones de la app
#---------------------------------

#---------------------------------
#ventana principal
#---------------------------------

#se declara una variable llamada "ventana_principal" que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk( )

#Titulo de la ventana
ventana_principal.title("Sistema UIS Socorro")

#Tamaño de la ventana
ventana_principal.geometry("500x500")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fonde de la ventana
ventana_principal.config(bg="white")







frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="red", width=500, height=125)
frame_operaciones.place(x=0, y=0)

frame_mitad = Frame(ventana_principal)
frame_mitad.config(bg="blue", width=500, height=125)
frame_mitad.place(x=0, y=190)

frame_vertical =Frame(ventana_principal)
frame_vertical.config(bg="blue", width=100, height=500)
frame_vertical.place(x=100, y=0)

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="red", width=500, height=125)
frame_resultados.place(x=0, y=375)




ventana_principal.mainloop()
