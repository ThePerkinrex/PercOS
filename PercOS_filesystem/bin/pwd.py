from command import Command


class Pwd(Command):
    name = "pwd"
    desc = "Shows the directory where the user is"
    author = "ThePerkinrex"
    usage = "pwd"

    @staticmethod
    def call(dire, usr, args=None):
        print(dire.dir)
