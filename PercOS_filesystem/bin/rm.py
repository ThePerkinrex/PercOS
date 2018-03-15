from command import Command
import os


class Rm(Command):
    name = 'rm'
    desc = 'Removes a file or directory'
    usage = 'rm <file|dir>'
    author = 'native'

    def call(self, args=None):
        if args is not None and len(args) > 0:
            path = self.dire.realdir + '/' + args[0]
            try:
                os.remove(path)
            except OSError:
                os.rmdir(path)
