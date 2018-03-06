from command import Command


class MkAdmin(Command):
    name = 'mkAdmin'
    desc = 'Changes user rights (if the user is admin)'
    usage = 'mkAdmin'
    author = 'native'
