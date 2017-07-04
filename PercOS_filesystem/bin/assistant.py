from PercOS_filesystem.bin.command import Command


class Assistant(Command):
    name = "assistant"
    desc = "this command starts the assistant"
    author = "ThePerkinrex"

    @staticmethod
    def call(dire, usr, args=None):
        print("this is my assistant")

