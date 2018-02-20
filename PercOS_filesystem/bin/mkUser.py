from command import Command
import PercOSUtils as Utils
import os


class MkUser(Command):
    name = "mkUser"
    desc = "Creates an users (if the user is admin)"
    author = "ThePerkinrex"
    usage = "mkUser"

    def call(self, args=None):
        p = self.getUsersInfo()
        if p is not None:
            print('Creating new user')
            print('')
            nUsr = input('Username >> ')
            nPas = input('Password >> ')
            isSU = Utils.getProbedInput('Do you want to make admin? (Y/n) ', ['y', 'n'])
            if isSU == 'y':
                p.superusers.append(nUsr)
                p.perms.append('1')
            else:
                p.normalusers.append(nUsr)
                p.perms.append('0')
            p.users.append(nUsr)
            p.pases.append(nPas)
            Utils.writeUsers(p.users, p.pases, p.superusers)
            os.mkdir(Utils.Dire("PercOS_filesystem", "users", nUsr).realdir)
            self.setUsersInfo(p)
        else:
            print("You don't have enough permissions to perform this")
        return 0
        pass
