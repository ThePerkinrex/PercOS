#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# PercOS Main Script

# Setup
import PercOSApps as Apps
import PercOSUtils as Utils
from command import UsersInfo
import AlgebraMathForPercOS as AMath
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

            print("There are no registered users, creating the inital user wich will be admin")

            # FIXME add a loop here
            self.usr = input("Username: ")
            self.pas = input("Password:  ")
            double_pas = input("Repeat password: ")
            if double_pas == self.pas:
                print("    User: " + self.usr)
                print("Password: " + self.pas)
                c = Utils.getProbedInput("Is it correct?(Y/n): ", ["y", "n"], 'y')
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
                print("You have " + tries.__str__() + " tries.\n")
                self.usr = input("Username: ")
                self.pas = input("Password: ")
                found = False
                for i in range(len(self.users)):
                    if self.usr == self.users[i] and self.pas == self.pases[i]:
                        found = True
                        break
                if found:
                    if self.usr == '':
                        print("Hello devUser")
                        if self.usr in self.superusers:
                            print('devUser - You\'re admin')
                            # dire = dire + 'dev/'
                    else:
                        print("Hello " + self.usr)
                        if self.usr in self.superusers:
                            print(self.usr + ' - You\'re admin')
                            # dire = dire + self.usr + '/'
                    break
                else:
                    print("Incorrect")
                    tries -= 1

        if self.usr == '':
            dire = Utils.Dire("PercOS_filesystem", "users", 'dev')
        else:
            dire = Utils.Dire("PercOS_filesystem", "users", self.usr)

        if self.nUsr:
            os.mkdir(dire.realdir)

    def getUsersInfo(self):
        r = None
        if self.usr in p.superusers:
            r = UsersInfo(self.users, self.pases, self.superusers, self.normalusers, self.perms)
        else:
            print('You can\'t do that')
        return r

    def setUsersInfo(self, usersinfo):
        r = None
        if self.usr in self.superusers:
            self.superusers = usersinfo.superusers
            self.users = usersinfo.users
            self.normalusers = usersinfo.normalusers
            self.pases = usersinfo.pases
            self.perms = usersinfo.perms
        else:
            print('You can\'t do that')

    def callcomm(self, comm):
        if comm == "mkAdmin":
            if self.usr in self.superusers:
                print('Changing permissions')
                nUsr = Utils.getProbedInputNormal('Username >> ', self.users)
                isSU = Utils.getProbedInput('Do you want him to be admin? (Y/n) ', ['y', 'n'], 'y')
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
                print('You don\'t have enough permissions to do it')
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

            if not r[0]:
                print(comm + " is not a valid command")
            return r[1]

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
