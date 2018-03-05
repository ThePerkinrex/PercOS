import inherit
from command import Command


class Help(Command):

    name = "help"
    desc = "Shows this help message"
    author = "native"
    usage = "help"

    @staticmethod
    def getHelpMsgs():
        msgs = []
        for cls in inherit.inheritors():
            msg = ''
            if cls.author == 'native':
                msg = cls.name + " > " + cls.desc
            else:
                msg = cls.name + " > " + cls.desc + " - Command made by " + cls.author
            msgs.append(msg)

        return msgs

    def call(self, args=None):
        print("Command list")
        print("If the command has an asterisk, it's invalid")
        #print("calculator > opens the calculator, you can also use 'calc'")
        print("upDown > opens the game UpDown")
        print("balls > opens the game Balls")
        print("end > ends the os")
        #print("*mkUser > creates an users (if the user is admin)")
        print("mkAdmin > Changes user rights (if the user is admin)")
        print("time > Prints the date and time")
        for msg in Help.getHelpMsgs():
            print(msg)
