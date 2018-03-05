
class UsersInfo:
    def __init__(self, users, pases, superusers, normalusers, perms):
        self.users = users
        self.pases = pases
        self.superusers = superusers
        self.normalusers = normalusers
        self.perms = perms

class Command:
    name = None
    desc = None
    usage = "The usage for this command hasn't been implemented yet"
    author = None

    def __init__(self, dire, usr, percos):
        self.dire = dire
        self.usr = usr
        self.percos = percos

    def call(self, args=None):
        print("This command hasn't been implemented yet,\n if you think this is an error contact the command author")
        print("Current dir: " + self.dire.dir)
        if not (args is None or args == ''):
            print("Some arguments were in the call: " + args)

    def getUsersInfo(self):
        return self.percos.getUsersInfo()

    def setUsersInfo(self, usersinfo):
        return self.percos.setUsersInfo(usersinfo)
