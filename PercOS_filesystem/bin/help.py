import inherit
from command import Command


class Help(Command):

    name = "help"
    desc = "Shows this help message"
    author = "native"
    usage = "help"

    @staticmethod
    def getHelpMsgs():
        """
        A function that fetches the help messages from every command. \n
        Returns a list with them
        """
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
                msg = ' +   ' + cls.name + " > " + cls.desc
                msg = msg + " - Command made by " + cls.author
                msgs.append(msg)
        return msgs

    def call(self, args=None):
        print("Command list")
        print("If the command has an asterisk, it's invalid")
        print('')
        for msg in Help.getHelpMsgs():
            print(msg)
