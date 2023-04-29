#Se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#---------------------------------
#Funciones de la app
#---------------------------------
def calcular():
    W = int(a.get())+int(b.get())
    A = int(a.get())-int(b.get())
    L = int(a.get())/int(b.get())
    T = int(a.get())//int(b.get())
    E = int(a.get())*int(b.get())
    R = int(a.get())**int(b.get())
    S = int(a.get())%int(b.get())
    t_resultados.insert(INSERT, f"{a.get()} + {b.get()} = {W}\n")
    t_resultados.insert(INSERT, f"{a.get()} - {b.get()} = {A}\n")
    t_resultados.insert(INSERT, f"{a.get()} / {b.get()} = {L}\n")
    t_resultados.insert(INSERT, f"{a.get()} // {b.get()} = {T}\n")
    t_resultados.insert(INSERT, f"{a.get()} * {b.get()} = {E}\n")
    t_resultados.insert(INSERT, f"{a.get()} ** {b.get()} = {R}\n")
    t_resultados.insert(INSERT, f"{a.get()} % {b.get()} = {S}\n")
def borrar():
    messagebox.showinfo("Minicalculadora 1.0", "Se borraran todos los datos")
    a.set("")
    b.set("")
    t_resultados.delete("1.0", "end")
def salir():
    messagebox.showinfo("Minicalculadora 1.0", "La APP se cerrara, ¿Desea continuar?")
    ventana_principal.destroy()

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
ventana_principal.config(bg="gray")

#------------------------------------------
#Variable de control
#-----------------------------------------

a = StringVar()
b = StringVar()

#----------------------------------------------
#frame entrada datos
#----------------------------------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

#Logo de la APP
logo = PhotoImage(file="img/logo_uis.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=11, y=40)

#Etiqueta para el Titulo
lb_titulo = Label(frame_entrada, text="Minicalculadora 1.0")
lb_titulo.config(bg="white", fg="green", font=("Helvetica", 20))
lb_titulo.place(x=240, y=10)

#Etiqueta para el primer titulo
lb_a = Label(frame_entrada, text="a :")
lb_a.config(bg="white", fg="green", font=("Helvetica", 20))
lb_a.place(x=250, y=60)

#Caja de texto (Entry) para el primer numero
entry_a = Entry(frame_entrada, textvariable=a)
entry_a.config(bg="white", fg="green", font=("Courier", 20))
entry_a.focus_set()
entry_a.place(x=290, y=60, width=100, height=30)

#Etiqueta para el segundo titulo
lb_b = Label(frame_entrada, text="b :")
lb_b.config(bg="white", fg="green", font=("Helvetica", 20))
lb_b.place(x=250, y=100)

#Caja de texto (Entry) para el segundo numero
entry_b = Entry(frame_entrada, textvariable=b)
entry_b.config(bg="white", fg="green", font=("Courier", 20))
entry_b.place(x=290, y=100, width=100, height=30)

#----------------------------------------------
#frame operaciones
#----------------------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

#Boton para calcular
bt_calcular=Button(frame_operaciones, text="calcular", command=calcular)
bt_calcular.place(x=45, y=35,width=100, height=30)

#boton borrar
bt_borrar=Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35,width=100, height=30)

#boton borrar
bt_salir=Button(frame_operaciones, text="salir", command=salir)
bt_salir.place(x=335, y=35,width=100, height=30)


#----------------------------------------------
#frame resultados
#----------------------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

#Area de texto para resultados
t_resultados=Text(frame_resultados)
t_resultados.config(bg="black", fg="green", font=("Courier", 20))
t_resultados.place(x=10, y=10, width=460, height=160)


#run
#se ejecuta la funcion (metodo) mainloop() de la clase Tk().
#A traves de la instancia ventana_princinpal este metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el usuario haga, cada accion del usuario se conoce como evento.
#El mainloop( es un bucle infinito)
ventana_principal.mainloop()
