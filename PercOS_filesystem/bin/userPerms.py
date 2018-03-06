from command import Command

class UserPerms(Command):
    name = "userPerms|perms"
    desc = "A command for viewing user permissions"
    usage = "<userPerms|perms> [user]"
    author = "native"

    def showPerms(self, p, user):
        i = p.users.index(user)
        if not user == '':
            print(user + '\t>\t' + p.perms[i])
        else:
            print('devUser\t>\t' + p.perms[i])

    def call(self, args=None):
        p = self.getUsersInfo()
        if args is None or len(args) == 0:
            for user in p.users:
                self.showPerms(p, user)
        else:
            self.showPerms(p, args[0])
