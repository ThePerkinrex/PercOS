#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# PercOS Main Script

# Setup
import PercOSApps as Apps
import PercOSUtils as Utils
import AlgebraMathForPercOS as AMath
from time import gmtime, strftime
import os


class PercOS:
    def __init__(self):
        self.state = 0
        self.uFileName = "Users.prcdat"
        self.usr = ""
        self.pas = ""
        self.nUsr = False
        self.dire = Utils.Dire
        self.users = []
        self.superusers = []
        self.normalusers = []
        self.pases = []
        self.perms = []

    def init(self):
        # Init Messages
        version = "Alpha 1.2.0"
        print(Utils.decor("PercOS " + version, 60))
        Utils.printInit()
        Apps.printInit()
        # AMath.printInit()

    def getUsers(self):
        usersFile = open(self.uFileName, 'r')
        usersFileLines = usersFile.readlines()
        usersFile.close()
        for line in usersFileLines:
            args = line.strip('\n').split(',')
            self.users.append(args[0])
            self.pases.append(args[1])
            self.perms.append(args[2])
            if args[2] == '1':
                self.superusers.append(args[0])
            if args[2] == '0':
                self.normalusers.append(args[0])

    def start(self):
        if len(self.users) == 0:

            # there are no users, first start menu

            print("No hay usuarios registrados, creando el usuario inicial, que será admin")

            # FIXME add a loop here
            self.usr = input(" Nombre de usuario: ")
            self.pas = input("        Contraseña: ")
            double_pas = input("Repetir contraseña: ")
            if double_pas == self.pas:
                print("   Usuario: " + self.usr)
                print("Contraseña: " + self.pas)
                c = Utils.getProbedInput("Es esto correcto?(Y/n)", ["y", "n"])
                if c == "y":
                    self.users.append(self.usr)
                    self.pases.append(self.pas)
                    self.perms.append('1')
                    self.superusers.append(self.usr)
                    Utils.writeUsers(self.users, self.pases, self.superusers)
                    self.nUsr = True

        else:

            # asking the user for credentials

            tries = 3;
            while tries > 0:
                print("Tienes " + tries.__str__() + " intentos.\n")
                self.usr = input("Nombre de usuario: ")
                self.pas = input("       Contraseña: ")
                found = False
                for i in range(len(self.users)):
                    if self.usr == self.users[i] and self.pas == self.pases[i]:
                        found = True
                        break
                if found:
                    if self.usr == '':
                        print("Hola devUser")
                        if self.usr in self.superusers:
                            print('devUser - Eres administrador')
                            # dire = dire + 'dev/'
                    else:
                        print("Hola " + self.usr)
                        if self.usr in self.superusers:
                            print(self.usr + ' - Eres administrador')
                            # dire = dire + self.usr + '/'
                    break
                else:
                    print("Incorrecto")
                    tries -= 1

        if self.usr == '':
            dire = Utils.Dire("PercOS_filesystem", "users", 'dev')
        else:
            dire = Utils.Dire("PercOS_filesystem", "users", self.usr)

        if self.nUsr:
            os.mkdir(dire.realdir)

    def callcomm(self, comm):
        if comm == "mkUsero":
            pass
            # if self.usr in self.superusers:
            #     print('Creando nuevo usuario')
            #     print('')
            #     nUsr = input('Nombre de usuario >> ')
            #     nPas = input('       Contrasena >> ')
            #     isSU = Utils.getProbedInput('Quieres que sea admin? (Y/n) ', ['y', 'n'])
            #     if isSU == 'y':
            #         self.superusers.append(nUsr)
            #         self.perms.append('1')
            #     else:
            #         self.normalusers.append(nUsr)
            #         self.perms.append('0')
            #     self.users.append(nUsr)
            #     self.pases.append(nPas)
            #     Utils.writeUsers(self.users, self.pases, self.superusers)
            #     os.mkdir(Utils.Dire("PercOS_filesystem", "users", nUsr).realdir)
            # else:
            #     print('No tienes suficientes permisos para hacer esto')
            # return 0
        # elif comm == "mkFile":
        #    print('add filename extension (.txt .py)')
        #    filename = dire + input(' Filename > ')
        #    Utils.mkFile(filename)
        #    return 0
        elif comm == "mkAdmin":
            if self.usr in self.superusers:
                print('Cambiando permisos')
                nUsr = Utils.getProbedInputNormal('Nombre de usuario >> ', self.users)
                isSU = Utils.getProbedInput('Quieres que sea admin? (Y/n) ', ['y', 'n'])
                if isSU == 'y':
                    if nUsr not in self.superusers:
                        self.superusers.append(nUsr)
                        self.normalusers.remove(nUsr)
                else:
                    if nUsr not in self.normalusers:
                        self.normalusers.append(nUsr)
                        self.superusers.remove(nUsr)
                Utils.writeUsers(self.users, self.pases, self.superusers)
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
            for user in self.users:
                i = self.users.index(user)
                if not user == '':
                    print(user + ' ' + self.perms[i])
                else:
                    print('devUser ' + self.perms[i])
            return 0
        elif comm == "":
            return 0
        else:
            r = Apps.comm(comm, self.usr, self.dire, self)

            if not r:
                print(comm + " no es un comando valido")
            return 0

    # Main Loop
    def main(self):
        self.init()
        self.getUsers()
        self.start()
        while True:
            if self.state == 0:
                comm = ''
                if self.usr == '':
                    comm = input("devUser >> ")
                else:
                    comm = input(self.usr + " >> ")
                # Command detection

                commout = self.callcomm(comm)

                if commout == 1:
                    break

            elif self.state == 2:
                break


p = PercOS()

if __name__ == '__main__':
    p.main()
