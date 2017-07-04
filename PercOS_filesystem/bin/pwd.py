from PercOSApps import Command


def getcomm():
    return Pwd


class Pwd(Command):
    name = "pwd"
    desc = "This command prints out the current directory"
    author = "ThePerkinrex"

    @staticmethod
    def call(dire, args):
        print(dire.dir)
