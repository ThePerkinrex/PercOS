from command import Command


class cd(Command):
    name = 'cd'
    desc = 'Changes the working directory'
    usage = 'cd <place to go>'
    author = 'native'

    def call(self, args=None):
        if len(args) == 0:
            print('I need at least the place to go to work')
        else:
            self.dire.cd(args[0])
