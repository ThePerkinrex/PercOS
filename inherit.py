from command import Command
import PercOS_filesystem.bin
import importlib, os, glob, inspect


def inheritors():
    subclasses = set()
    # work = [Command]
    # while work:
    #     parent = work.pop()
    #     print('Parent:', parent)
    #     for child in parent.__subclasses__():
    #         print('Child:', child)
    #         if child not in subclasses:
    #             subclasses.add(child)

    #  print(glob.glob(os.path.join(os.path.abspath('PercOS_filesystem/bin/')) + '/*.py'))
    #  print(os.path.join(os.path.abspath('PercOS_filesystem/bin')) + '/*.py')
    for file in glob.glob(os.path.join(os.path.abspath('PercOS_filesystem/bin/')) + '/*.py'):
        name = inspect.getmodulename(file)
        # print('PercOS_filesystem.bin.' + name, file)
        # add package prefix to name, if required
        module = importlib.import_module('PercOS_filesystem.bin.' + name)
        # print(module)
        for member in inspect.getmembers(module, predicate=inspect.isclass):
            # print(Command, type(Command()))
            if not member[1] is Command:
                # print(member[1])
                if Command in inspect.getmro(member[1]):
                    # print(member)
                    subclasses.add(member[1])
    # print(subclasses)
    return subclasses