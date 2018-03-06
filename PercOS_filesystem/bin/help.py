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
        msgs.append('Native commands:')
        for cls in inherit.inheritors():
            if cls.author == 'native':
                msg = ' -   ' + cls.name + " > " + cls.desc
                msgs.append(msg)
        msgs.append('')
        msgs.append('Custom commands:')
        for cls in inherit.inheritors():
            if cls.author != 'native':
                msg = ' +   ' + cls.name + " > " + cls.desc + " - Command made by " + cls.author
                msgs.append(msg)
        return msgs

    def call(self, args=None):
        print("Command list")
        print("If the command has an asterisk, it's invalid")
        #print("mkAdmin > Changes user rights (if the user is admin)")
        print('')
        #print("time > Prints the date and time")
        for msg in Help.getHelpMsgs():
            print(msg)
