import pickle

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre=str(nombre)
        self.vida=int(vida)
        self.ataque=int(ataque)
        self.defensa=int(defensa)
        self.alcance=int(alcance)
    def __str__(self):
        return f"Nombre:{self.nombre} \nVida:{self.vida} \nAtaque:{self.ataque} \nDefensa{self.defensa} \nAlcance:{self.alcance}"

class Gestor:
    personaje=[]



    def añadir(self):
        file = open('personajes.pckl', 'ab+')#Abre un archivo para agregar y leer en formato binario. El puntero del archivo se encuentra al final del archivo, si el archivo existe. El archivo se abre en el modo de adición. Si el archivo no existe, crea un nuevo archivo para lectura y escritura.
        file.seek(0)#para mover la posicion de el archivo a 0
        try:
            self.personaje.load(file)
            pass
        except:
            print("Personaje no válido.")
        finally:
            file.close()

    def guardar(self):
        file = open('personajes.pckl', 'wb')#wb+, Abre un archivo para escritura y lectura en formato binario. Sobrescribe el archivo existente si el archivo existe. Si el archivo no existe, crea un nuevo archivo para lectura y escritura.
        pickle.dump(self.personajes, file)#el metodo dump sirve para almacenar objetos en un fichero
        file.close()



Guerrero=Personaje("Guerrero", 12, 3, 4, 5)
print(Guerrero)