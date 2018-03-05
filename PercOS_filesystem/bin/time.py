from command import Command
from time import gmtime, strftime

class Time(Command):
    name = "time"
    desc = "Shows the time"
    author = "native"
    usage = "time"

    def call(self, args=None):
        print(strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
        return self.execute('end')
