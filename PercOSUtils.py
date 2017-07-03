
#PercOS Utils

#Setup
import AlgebraMathForPercOS as AMath
import distutils.file_util as FUtil
import os

uFileName = "Users.prc"

#Function for decoring messages
def decor(st, m):
    nhastag = 40
    return ("\n" * m ) + ("#" * nhastag) + "#######################\n" + st + "\n" + ("#" * nhastag) + "#######################" + ("\n")


#Init Message
def printInit():
    version = "Alpha 1.0.4"
    print(decor("PercOS Utils " + version, 1))

#Help message
def printHelp():
    print("Lista de comandos")
    print("Si el comando tiene un asterisco es que es invalido")
    print("calculator > abre la calculadora, tambien es posible usar 'calc'")
    print("upDown > abre el juego UpDown")
    print("balls > abre el juego Balls")
    print("end > termina el sistema operativo")
    print("mkUser > crea un usuario (si el usuario es admin.)")
    print("mkAdmin > cambia los permios de un usuario (si el usuario es admin.)")
    print("time > imprime la fecha y la hora")
    print("help > muestra este mensaje de ayuda")

#Advanced input functions
def getProbedInput(prompt, accepted):
    while True:
        value = input(prompt).lower()

        if value in accepted:
            return value
        else:
            print(value + ' no es una respuesta valida.')

def getProbedInputNormal(prompt, accepted):
    while True:
        value = input(prompt)

        if value in accepted:
            return value
        else:
            print(value + ' no es una respuesta valida.')

#Function for writing to the users.txt file
def writeUsers(users, pases, superusers):
    f = open(uFileName, 'w')
    for user in users:
        i = users.index(user)
        pas = pases[i]
        perm = '0'
        if user in superusers:
            perm = '1'
        f.write(user + ',' + pas + ',' + perm + '\n')
    f.close()

#function for making and writing files
def mkFile(filename):
    lines = []
    while True:
        line = input(' ')
        if line == '\\':
            break
        else:
            lines.append(line)
    FUtil.write_file(filename, lines)

def concat(list):
    r = ""
    for s in list:
        r += s
    return r

def concatDirs(list):
    r = ""
    for s in list:
        r += s + "/"
    return r

def dirdow(dir):
    ls = dir.split("/")
    ls.remove("")
    ls.pop()
    r = concatDirs(ls)
    r.rstrip("/")
    return r
        
class Dire:

    def __init__(self, baseDir, usersDir, user):
        self.dir = "/" + usersDir + "/" + user
        self.realdir = os.getcwd() + "/" + baseDir + self.dir
        self.bd = baseDir

    def cd(self, toGo):
        if ".." in toGo:
            if toGo.startsWith("/"):
                print("Can't go lower than the base directory.")
            else:
                levdow = toGo.split("/").count("..")
                i = 0
                while i<levdow:
                    i += 1
                    self.dir = dirdow(self.dir)
                self.realdir = os.getcwd() + "/" + self.bd + self.dir

        else:
            if toGo.startsWith("/"):
                self.dir = toGo
                self.realdir = os.getcwd() + "/" + self.bd + self.dir
            else:
                self.dir = self.dir + "/" + toGo
                self.realdir = os.getcwd() + "/" + self.bd + self.dir
