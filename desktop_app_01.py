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
ventana_principal.config(bg="yellow")

#----------------------------------------------
#frame entrada datos
#----------------------------------------------


#----------------------------------------------
#frame operaciones
#----------------------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="blue", width=500, height=125)
frame_operaciones.place(x=0, y=250)

#----------------------------------------------
#frame resultados
#----------------------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="red", width=500, height=125)
frame_resultados.place(x=0, y=375)



#run
#se ejecuta la funcion (metodo) mainloop() de la clase Tk().
#A traves de la instancia ventana_princinpal este metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el usuario haga, cada accion del usuario se conoce como evento.
#El mainloop( es un bucle infinito)
ventana_principal.mainloop()
