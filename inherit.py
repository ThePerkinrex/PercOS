from command import Command
import importlib
import os
import glob
import inspect


def inheritors():
    subclasses = set()
    for file in glob.glob(os.path.join(
                                       os.path.abspath('PercOS_filesystem/bin/'
                                                       )) + '/*.py'):
        name = inspect.getmodulename(file)
        module = importlib.import_module('PercOS_filesystem.bin.' + name)
        for member in inspect.getmembers(module, predicate=inspect.isclass):
            if not member[1] is Command:
                if Command in inspect.getmro(member[1]):
                    subclasses.add(member[1])
    return subclasses
