#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# PercOS Main Script

# Setup
import PercOSApps as Apps
import PercOSUtils as Utils
import AlgebraMathForPercOS as AMath
from time import gmtime, strftime
import os

state = 0

uFileName = "Users.prcdat"

#dir = Utils.Dire("PercOS_filesystem","users")

# Init Messages
version = "Alpha 1.2.0"
print(Utils.decor("PercOS " + version, 60))
Utils.printInit()
Apps.printInit()
AMath.printInit()

# reading the users, passwords and permissions file

usersFile = open(uFileName,'r')
usersFileLines = usersFile.readlines()
usersFile.close()

users = []
superusers = []
normalusers = []
pases = []
perms = []

for line in usersFileLines:
    args = line.strip('\n').split(',')

    users.append(args[0])
    pases.append(args[1])
    perms.append(args[2])

    if args[2] == '1':
        superusers.append(args[0])
    if args[2] == '0':
        normalusers.append(args[0])

usr = ""
pas = ""
nUsr = False

if len(users) == 0:

    # there are no users, first start menu

    print("No hay usuarios registrados, creando el usuario inicial, que será admin")

    # FIXME add a loop here
    usr = input(" Nombre de usuario: ")
    pas = input("        Contraseña: ")
    double_pas = input("Repetir contraseña: ")
    if double_pas == pas:
        print("   Usuario: " + usr)
        print("Contraseña: " + pas)
        c = Utils.getProbedInput("Es esto correcto?(Y/n)", ["y","n"])
        if c == "y":
            users.append(usr)
            pases.append(pas)
            perms.append('1')
            superusers.append(usr)
            Utils.writeUsers(users, pases, superusers)
            nUsr = True


else:

    # asking the user for credentials

    tries = 3;
    while tries>0:
        print("Tienes " + tries.__str__() + " intentos.\n")
        usr = input("Nombre de usuario: ")
        pas = input("       Contraseña: ")
        found = False
        for i in range(len(users)):
            if usr == users[i] and pas == pases[i]:
                found = True
                break
        if found:
            if usr == '':
                print("Hola devUser")
                if usr in superusers:
                    print('devUser - Eres administrador')
                #dire = dire + 'dev/'
            else:
                print("Hola " + usr)
                if usr in superusers:
                    print(usr + ' - Eres administrador')
                #dire = dire + usr + '/'
            break
        else:
            print("Incorrecto")
            tries -= 1

dire = Utils.Dire

if usr == '':
    dire = Utils.Dire("PercOS_filesystem", "users", 'dev')
else:
    dire = Utils.Dire("PercOS_filesystem", "users", usr)

if nUsr:
    os.mkdir(dire.realdir)

def callcomm(comm):
    if comm == "mkUsero":
        if usr in superusers:
            print('Creando nuevo usuario')
            print('')
            nUsr = input('Nombre de usuario >> ')
            nPas = input('       Contrasena >> ')
            isSU = Utils.getProbedInput('Quieres que sea admin? (Y/n) ', ['y', 'n'])
            if isSU == 'y':
                superusers.append(nUsr)
                perms.append('1')
            else:
                normalusers.append(nUsr)
                perms.append('0')
            users.append(nUsr)
            pases.append(nPas)
            Utils.writeUsers(users, pases, superusers)
            os.mkdir(Utils.Dire("PercOS_filesystem", "users", nUsr).realdir)
        else:
            print('No tienes suficientes permisos para hacer esto')
        return 0
    # elif comm == "mkFile":
    #    print('add filename extension (.txt .py)')
    #    filename = dire + input(' Filename > ')
    #    Utils.mkFile(filename)
    #    return 0
    elif comm == "mkAdmin":
        if usr in superusers:
            print('Cambiando permisos')
            nUsr = Utils.getProbedInputNormal('Nombre de usuario >> ', users)
            isSU = Utils.getProbedInput('Quieres que sea admin? (Y/n) ', ['y', 'n'])
            if isSU == 'y':
                if nUsr not in superusers:
                    superusers.append(nUsr)
                    normalusers.remove(nUsr)
            else:
                if nUsr not in normalusers:
                    normalusers.append(nUsr)
                    superusers.remove(nUsr)
            Utils.writeUsers(users, pases, superusers)
        else:
            print('No tienes suficientes permisos para hacer esto')
        return 0
    elif comm == "end":
        print("Terminando PercOS")
        return 1
    elif comm == "time":
        print(strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
        return 0
    elif comm == "userPerms":
        for user in users:
            i = users.index(user)
            if not user == '':
                print(user + ' ' + perms[i])
            else:
                print('devUser ' + perms[i])
        return 0
    elif comm == "":
        return 0
    else:
        r = Apps.comm(comm, usr, dire)

        if not r:
            print(comm + " no es un comando valido")
        return 0


# Main Loop

while True:
    if state == 0:
        comm = ''
        if usr == '':
            comm = input("devUser >> ")
        else:
            comm = input(usr + " >> ")
        # Command detection

        commout = callcomm(comm)

        if commout == 1:
            break

    elif state == 2:
        break
