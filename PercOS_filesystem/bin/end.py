from command import Command

class Time(Command):
    name = "end"
    desc = "Ends PercOS"
    author = "native"
    usage = "end"

    def call(self, args=None):
        print("Ending PercOS")
        return 1
