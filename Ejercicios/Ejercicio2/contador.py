import sys

file = open("contador.txt", "a+")#mediante a+, si el fichero contador.txt ya existe lo abre y lo sobreescribe, si no existe lo crea y lo abre
file.seek(0)#para mover la posicion de el archivo a 0

cuenta=file.readline()

if len(cuenta)==0:
    cuenta="0"
    file.write(cuenta)
try:
    contador=int(cuenta)#inicializamos un contador transformando el valor string de la cuenta a un int
    if sys.argv[1]=="inc":
        contador=contador+1
    elif sys.argv[1]=="dec":
        contador=contador-1
    print(contador)
    file.write(str(contador))#como es un txt, lo que le tenemos que escribir son string--str()
    file.close()
except:
    print("Error: Fichero corrupto.")
