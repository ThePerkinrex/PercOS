from PercOS_filesystem.bin.command import Command
import PercOSUtils as Utils
#import PercOS as p
import os


class MkUser(Command):
    name = "mkUser"
    desc = "Creates an users (if the user is admin)"
    author = "ThePerkinrex"
    usage = "mkUser"

    @staticmethod
    def call(dire, usr, args=None):
        if usr in p.superusers:
            print('Creando nuevo usuario')
            print('')
            nUsr = input('Nombre de usuario >> ')
            nPas = input('       Contrasena >> ')
            isSU = Utils.getProbedInput('Quieres que sea admin? (Y/n) ', ['y', 'n'])
            if isSU == 'y':
                p.superusers.append(nUsr)
                p.perms.append('1')
            else:
                p.normalusers.append(nUsr)
                p.perms.append('0')
            p.users.append(nUsr)
            p.pases.append(nPas)
            Utils.writeUsers(users, pases, superusers)
            os.mkdir(Utils.Dire("PercOS_filesystem", "users", nUsr).realdir)
        else:
            print('No tienes suficientes permisos para hacer esto')
        return 0
