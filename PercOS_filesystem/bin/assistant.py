from command import Command


class Assistant(Command):
    name = "assistant"
    desc = "This command starts the assistant"
    author = "ThePerkinrex"
    usage = "assistant [question]"

    def call(self, args=None):
        print("this is my assistant")
