
class usuario():

    numeUser = 0

    def __init__(self,nombre,contra):
        self.nombre = nombre
        self.contra = contra

        self.conectado = False
        self.intentos= 3

        usuario.numeUser+=1

    def conectar(self,contrasena=None):
        if contrasena == None:
            myContra = input("Ingrese Contraseña: ")
        else:
            myContra=contrasena

        if myContra == self.contra:
            print("Se ha conectado con exito!")
            self.conectado = True
            return True
        else:
            self.intentos-=1
            if self.intentos > 0:

                print("Contraseña Incoorrecta")
                if contrasena != None:
                    return False
                print("Intentos Restantes:", self.intentos)
                self.conectar()
            else:
                print("Error, no se pudo iniciar seccion.")
                print("Adios")

    def desconectar(self):
        if self.conectado:
            print("Se cerro la coneccion con exito")
            self.conectado=False
        else:
            print("No ha iniciado seccion")

    def __str__(self):
        if self.conectado:
            connect = "Conectado"
        else:
            connect = "Desconectado"
        return f"Mi nombre de usuario es: {self.nombre} y estoy {connect}."


#user1 = usuario(input("Ingrese un nomre: "),input("Ingrese su contraseña: "))

#p#rint(user1)
#user1.conectar()
#print(user1)

#user1.desconectar()
#print(user1)