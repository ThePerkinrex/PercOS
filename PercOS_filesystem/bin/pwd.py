from PercOS_filesystem.bin.command import Command


def getcomm():
    return Pwd


class Pwd(Command):
    name = "pwd"
    desc = "muestra la carpeta en la que se encuentra el usuario"
    author = "ThePerkinrex"

    @staticmethod
    def call(dire, usr, args=None):
        print(dire.dir)
