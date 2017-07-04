
#PercOS Apps

#Setup
import random
import PercOSUtils as Utils
from PercOS_filesystem.bin import inherit
import importlib


#Init Message
def printInit():
    version = "Alpha 1.1.0"
    print(Utils.decor("PercOS Apps " + version, 1))




#Calculator
def calculator():
    def getInput(y):
        if y==1:
            x = input("Escribe el primer numero: ")
        else:
            x = input("Escribe el segundo numero: ")
        return x


    print("Opciones: ")
    print("-Suma: escribe 'suma'")
    print("-Resta: escribe 'resta'")
    print("-Multiplicacion: escribe 'mult'")
    print("-Division: escribe 'div'")
    print("-Potencia: escribe 'pot', elevas el 1º nº al 2º")
    print("-Cociente y resto de una division: escribe 'CoRe'")

    sel = input("Selecciona una opcion: ")
    result = 0
    x = float(getInput(1))
    y = float(getInput(2))
    
    if sel=="suma":
        result = x + y
    elif sel == "resta":
        result = x - y
    elif sel == "mult":
        result = x * y
    elif sel == "div":
        result = x / y
    elif sel == "pot":
        result = x ** y
    elif sel == "CoRe":
        result = "Cociente: " + str(x // y) + "\nResto: " + str(x % y)
    else:
        print("Eso no es una opcion")
    print(result)
    state = 0


#Up & Down game
def upDownGame():
    x = random.randint(0,100)
    print("Adivina un numero entre 0 y 100")
    while True:
        y = int(input("Escribe el numero que creas: "))
        if y == x:
            print("Correcto :)")
            break
        elif y < x:
            print("El numero que quieres es mayor")
            continue
        elif y > x:
            print("El numero que quieres es menor")
            continue



#Balls game
def ballsGame(user):
    nballs = 15
    p1 = user
    p2 = input("P1 > " + p1 + ", P2 > ")
    while True:
        print("Hay " + str(nballs) + " pelotas")
        P1in = int(Utils.getProbedInput(p1 + " > ", ["1","2"]))
        if P1in == 1 or P1in == 2:
            nballs -= P1in
            if nballs == 0:
                print(p2 + " gana")
                break
        print("Hay " + str(nballs) + " pelotas")
        p2in = int(Utils.getProbedInput(p2 + " > ", ["1", "2"]))
        if p2in == 1 or p2in == 2:
            nballs -= p2in
            if nballs == 0:
                print(p1 + " gana")
                break

# Apps command detection


def comm(command, usr, dire):

    #loadcommands()
    r = True
    if command == "calculator" or command == "calc":
            print("Abriendo la calculadora")
            calculator()
    elif command == "upDown":
            upDownGame()
    elif command == "balls":
            ballsGame(usr)
    else:
        if not loadcommands(command, dire, usr):
            r = False
    return r


def loadcommands(comm, dire, usr):

    for cls in inherit.inheritors():
        if comm == cls.name:
            #print("Author: " + cls.author + "\n")
            cls.call(dire, usr)
            return True

    return False





