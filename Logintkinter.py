from tkinter import *
from tkinter.ttk import *

ventana =Tk()
ventana.title("Login")
ventana.geometry("300x200")
ventana.resizable( width=False, height=False )

lusu=Label (ventana, text="Usuario")
lusu.pack()

user=StringVar()
eusu=Entry(ventana, width=30,textvariable=user)
eusu.pack()

lpas=Label (ventana, text="Contraseña")
lpas.pack()

pas=StringVar()
epas=Entry(ventana, width=30,show="*",textvariable=pas)
epas.pack()



def ingresar():
    if user.get() == "python" and pas.get()=="12345" :
        ventana.title("Correcto")
        print(user.get()," ",pas.get())
    else:
        ventana.title("Incorrecto")
        print(user.get()," ",pas.get())

btnEntrar= Button(ventana,text="Ingresar",command=ingresar)
btnEntrar.pack()

ventana.mainloop()
