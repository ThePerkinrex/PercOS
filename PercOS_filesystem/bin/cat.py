from command import Command


class Cat(Command):
    name = 'cat'
    desc = 'Shows what\'s in a file'
    usage = 'cat <file>'
    author = 'native'

    def call(self, args=None):
        if args is not None and len(args) > 0:
            filename = self.dire.realdir + '/' + args[0]
            f = open(filename)
            lines = f.readlines()
            for line in lines:
                print(line.strip('\n'))
