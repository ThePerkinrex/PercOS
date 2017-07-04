import os

import PercOSUtils as Utils
from PercOS_filesystem.bin.command import Command
from PercOS_filesystem.bin.inherit import inheritors

path = os.path.dirname(os.path.abspath(__file__))

for py in [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f != '__init__.py']:
    mod = __import__('.'.join([__name__, py]), fromlist=[py])
    classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
    for cls in classes:
        print(cls)
        if cls is not Command:
            print("this is not the command class")
            print(inheritors())

