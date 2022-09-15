import random
import json

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line


def random_insert(lst, item):
    lst.insert(random.randrange(len(lst) + 1), item)


def load_used(data_folder):
    with open(f"{data_folder}/used.json", "r") as file:
        file_things = json.load(file)
        return file_things


def load_unused(data_folder):
    with open(f"{data_folder}/unused.json", "r") as file:
        file_things = json.load(file)
        return file_things


def load_samples(data_folder):
    with open(f"{data_folder}/samples.json", "r") as file:
        file_things = json.load(file)
        return file_things

def write_used(things, data_folder):
    with open(f"{data_folder}/used.json", "w") as file:
        json.dump(things, file)


def write_unused(things, data_folder):
    with open(f"{data_folder}/unused.json", "w") as file:
        json.dump(things, file)


def write_samples(things, data_folder):
    with open(f"{data_folder}/samples.json", "w") as file:
        json.dump(things, file)