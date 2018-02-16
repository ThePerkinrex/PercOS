from PercOS_filesystem.bin.command import Command
from PercOS_filesystem.bin import inherit


class Help(Command):

    name = "help"
    desc = "Shows this help message"
    author = "ThePerkinrex"

    @staticmethod
    def getHelpMsgs():
        msgs = []
        for cls in inherit.inheritors():
            msg = cls.name + " > " + cls.desc + " - Command made by " + cls.author
            msgs.append(msg)

        return msgs

    @staticmethod
    def call(dire, usr, args=None):
        print("Command list")
        print("If the command has an asterisk, it's invalid")
        print("calculator > opens the calculator, you can also use 'calc'")
        print("upDown > opens the game UpDown")
        print("balls > opens the game Balls")
        print("end > ends the os")
        print("mkUser > creates an users (if the user is admin)")
        print("mkAdmin > Changes user rights (if the user is admin)")
        print("time > Prints the date and time")
        for msg in Help.getHelpMsgs():
            print(msg)