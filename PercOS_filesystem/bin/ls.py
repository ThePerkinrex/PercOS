from command import Command
import os


class Ls(Command):
    name = 'ls'
    desc = 'Shows what\'s in the directory'
    usage = 'ls [dir]'
    author = 'native'

    def call(self, args=None):
        if args is not None:
            ld = None
            wd = self.dire.realdir
            if len(args) != 0:
                wd = self.dire.cd(args[0], True).realdir
            ld = os.listdir(wd)
            # print(wd)
            for l in ld:
                if os.path.isdir(wd + '/' + l):
                    p = 'Dir:   '
                    print(p, l)
            for l in ld:
                if os.path.isfile(wd + '/' + l):
                    p = 'File:  '
                    print(p, l)
