
#PercOS Apps

#Setup
import random
import PercOSUtils as Utils
import inherit
# Setup
import random

import PercOSUtils as Utils
import inherit


#Init Message
def printInit():
    version = "Alpha 1.1.0"
    print(Utils.decor("PercOS Apps " + version, 1))





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


def comm(command, usr, dire, percos):

    #loadcommands()
    r = (True, 0)
    #if command == "calculator" or command == "calc":
    #        print("Abriendo la calculadora")
    #        calculator()
    if command == "upDown":
            upDownGame()
    elif command == "balls":
            ballsGame(usr)
    else:
        l = loadcommands(command, dire, usr, percos)
        if not l[0]:
            r = (False, 0)
        r = (r[0], l[1])
    return r


def loadcommands(comm, dire, usr, percos):
    for cls in inherit.inheritors():
        args = comm.split(" ")
        if args[0] in cls.name.split('|'):
            #print("Author: " + cls.author + "\n")
            args.remove(args[0])
            c = cls(dire, usr, percos)
            ret = c.call(args)
            del c
            if ret is None:
                ret = 0;
            return (True, ret)

    return (False, 0)
