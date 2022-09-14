import random


def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line


def random_insert(lst, item):
    lst.insert(random.randrange(len(lst) + 1), item)
