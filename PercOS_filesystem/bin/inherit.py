from PercOS_filesystem.bin import Command


def inheritors():
    subclasses = set()
    work = [Command]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return subclasses