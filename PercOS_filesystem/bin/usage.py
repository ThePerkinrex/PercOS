from PercOS_filesystem.bin import inherit
from PercOS_filesystem.bin.command import Command


class Usage(Command):
    name = "usage"
    desc = "Prints out the usage of a command"
    usage = "usage [command]"
    author = "ThePerkinrex"

    @staticmethod
    def call(dire, usr, args=None):
        if len(args) == 0:
            print("------- USAGES -------")
            for cls in inherit.inheritors():
                print(cls.name + " > " + cls.usage)
        else:
            for cls in inherit.inheritors():
                if cls.name == args[0]:
                    print("------- USAGE FOR " + args[0] + " -------")
                    print(cls.name + " > " + cls.usage)
                    return
            print("That command doesn't exist")
