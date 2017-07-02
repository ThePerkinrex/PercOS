
#PercOS Main Script

#Setup
import PercOSApps as Apps
import PercOSUtils as Utils
import AlgebraMathForPercOS as AMath
from time import gmtime, strftime

state = 0

uFileName = "Users.prc"

dire = "PercOS_filesystem/users/"
seen_dire = "/users/"

#Init Messages
version = "Alpha 1.1.2"
print(Utils.decor("PercOS " + version, 60))
Utils.printInit()
Apps.printInit()
AMath.printInit()

#reding the users, passwords and permissions file

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
        
#asking the user for credentials

usr = input("Nombre de usuario: ")
pas = input("       Contrasena: ")
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
        dire = dire + 'dev/'
    else:
        print("Hola " + usr)
        if usr in superusers:
            print(usr + ' - Eres administrador')
        dire = dire + usr + '/'
else:
    print("Incorrecto")
    state = 2

#Main Loop

while True:
    if state == 0:
        comm = ''
        if usr == '':
            comm = input("devUser " + dire + " >> ")
        else:
            comm = input(usr + " " + dire + " >> ")
        #Command detection
        
        if comm == "help":
            Utils.printHelp()
            continue
        elif comm == "mkUser":
            if usr in superusers:
                print('Creando nuevo usuario')
                print('')
                nUsr = input('Nombre de usuario >> ')
                nPas = input('       Contrasena >> ')
                isSU = Utils.getProbedInput('Quieres que sea admin? (Y/n) ', ['y', 'n'])
                if isSU == 'y':
                    superusers.append(nUsr)
                else:
                    normalusers.append(nUsr)
                users.append(nUsr)
                pases.append(nPas)
                Utils.writeUsers(users, pases, superusers)
            else:
                print('No tienes suficientes permisos para hacer esto')
            continue
        elif comm == "mkFile":
            print('add filename extension (.txt .py)')
            filename = dire + input(' Filename > ')
            Utils.mkFile(filename)
            continue
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
            continue
        elif comm == "end":
            print("Terminando PercOS")
            break
        elif comm == "time":
            print(strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
            continue
        elif comm == "userPerms":
            for user in users:
                i = users.index(user)
                if not user == '':
                    print(user + ' ' + perms[i])
                else:
                    print('devUser ' + perms[i])
            continue
        elif comm in Apps.commands:
            Apps.comm(comm)
            continue
        elif comm == "":
            continue
        else:
            print(comm + " no es un comando valido")
            continue
    
    elif state == 2:
        break
