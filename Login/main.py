from tkinter import messagebox as MessageBox
from tkinter import *
from tkinter import ttk as ttk
from usuarios import usuario

root = Tk()

nombreUsuario = StringVar()
contraUsuario= StringVar()

usuarios =[]

def createGUI():
        
    #Ventana principal


    root.title("Login Usuario")

    #Main frame
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=400, height=320)

    titulo=Label(mainFrame, text="Logion RI OC",font=("Arial",24))
    titulo.grid(column=0, row=0, padx=10, pady=10,columnspan=2)

    nombreLabel=Label(mainFrame, text="Nombre: ")
    nombreLabel.grid(column=0, row=1)

    passLabel=Label(mainFrame,text="Contraseña:")
    passLabel.grid(column=0, row=2)


    #Entradas de texto

    nombreEntry= Entry(mainFrame,textvariable=nombreUsuario)
    nombreEntry.grid(column=1, row=1)
    nombreUsuario.set("")


    contraUsuario.set("")
    contraEntry = Entry(mainFrame,textvariable=contraUsuario,show="*")
    contraEntry.grid(column=1, row=2)

    #Botones

    iniciarSeccionButton = ttk.Button(mainFrame,text="Iniciar Seccion",command=iniciarSeccion)
    iniciarSeccionButton.grid(column=1,row=3, ipadx=5,ipady=5, padx=10,pady=10)

    registrarSeccionButton = ttk.Button(mainFrame,text="Registrar",command=registrarUsuario)
    registrarSeccionButton.grid(column=0,row=3, ipadx=5,ipady=5, padx=10,pady=10)



    root.mainloop()

def iniciarSeccion():
    for user in usuarios:
        if user.nombre == nombreUsuario.get():
            test = user.conectar(contraUsuario.get())
            if test:
                MessageBox.showinfo("Conectado", f"Se inicio seccion en {user.nombre} con exito")
            else:
                MessageBox.showerror("Error","Contraseña Incorrecta") 
            break   
    else: 
        MessageBox.showerror("Error","No exixte Usuario") 

def registrarUsuario():
    name = nombreUsuario.get()
    passwd = contraUsuario.get()
    newUser = usuario(name, passwd)
    usuarios.append(newUser)
    MessageBox.showinfo("Registro Exitoso", f"Se registro el usuario{name} con exito")
    name=""
    passwd=""

if __name__ =="__main__":

   # user1 = usuario(input("Ingrese un nombre: "),input("Ingrese su contraseña: "))
    user1 = usuario("David", "12345")
    usuarios.append(user1)
    createGUI() 
