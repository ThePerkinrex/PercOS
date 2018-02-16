from PercOS_filesystem.bin.command import Command


class Assistant(Command):
    name = "assistant"
    desc = "This command starts the assistant"
    author = "ThePerkinrex"
    usage = "assistant [question]"

    @staticmethod
    def call(dire, usr, args=None):
        print("this is my assistant")

