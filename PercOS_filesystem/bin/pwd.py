from command import Command


class Pwd(Command):
    name = "pwd"
    desc = "Shows the directory where the user is"
    author = "ThePerkinrex"
    usage = "pwd"

    def call(self, args=None):
        print(self.dire.dir)
