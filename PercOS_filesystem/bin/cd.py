from command import Command
from os import path


class cd(Command):
    name = 'cd'
    desc = 'Changes the working directory'
    usage = 'cd <place to go>'
    author = 'native'

    def call(self, args=None):
        if len(args) == 0:
            print('I need at least the place to go to work')
        else:
            toGo = self.dire.cd(args[0], True)
            if path.exists(toGo.realdir):
                if path.isdir(toGo.realdir):
                    self.dire.cd(args[0], False)
                else:
                    print('That isn\'t a directory')
            else:
                print('That doesn\'t exist')
