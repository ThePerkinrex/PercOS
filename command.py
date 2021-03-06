
class UsersInfo:
    def __init__(self, users, pases, superusers, normalusers, perms):
        self.users = users
        self.pases = pases
        self.superusers = superusers
        self.normalusers = normalusers
        self.perms = perms


class Command:
    name = None
    desc = "The description of this command hasn't been implemented yet"
    usage = "The usage for this command hasn't been implemented yet"
    author = "an anonymous user"

    def __init__(self, dire, usr, percos):
        self.dire = dire
        self.usr = usr
        self.percos = percos

    def call(self, args=None):
        print("""This command hasn't been implemented yet,
         if you think this is an error contact the command author""")
        print("Current dir: " + self.dire.dir)
        print("Real dir: " + self.dire.realdir)
        print("Base dir: " + self.dire.bd)
        if not (args is None or args == ''):
            print("Some arguments were in the call: " + str(args))
        return 0

    def execute(self, comm):
        return self.percos.callcomm(comm)

    def getUsersInfo(self):
        return self.percos.getUsersInfo()

    def setUsersInfo(self, usersinfo):
        return self.percos.setUsersInfo(usersinfo)
