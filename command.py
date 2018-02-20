import PercOS

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
        r = None
        p = self.percos
        print(self.usr, p.superusers)
        if self.usr in p.superusers:
            r = UsersInfo(p.users, p.pases, p.superusers, p.normalusers, p.perms)
        return r

    def setUsersInfo(self, usersinfo):
        r = None
        p = self.percos
        if self.usr in p.superusers:
            p.superusers = usersinfo.superusers
            p.users = usersinfo.users
            p.normalusers = usersinfo.normalusers
            p.pases = usersinfo.pases
            p.perms = usersinfo.perms
            print(p.users, usersinfo.users)
