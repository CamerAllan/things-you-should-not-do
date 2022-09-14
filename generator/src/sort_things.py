import os
import openai
import json
import argparse
import random
import spacy
from helpers.helpers import random_line

openai.api_key = os.getenv("OPENAI_API_KEY")


parser = argparse.ArgumentParser()
parser.add_argument("data_folder", help="path to data folder")
parser.add_argument("-n", type=int, default=18)

# Parse and print the results
args = parser.parse_args()
data_folder = args.data_folder
if data_folder is None:
    print("Uh oh!")
    exit(1)

# BEGIN LOGIC -----------------------------------------------------------------

# Init NLP for determining sentance similarity
nlp = spacy.load("en_core_web_sm")


def load_used():
    with open(f"{data_folder}/used.json", "r") as file:
        file_things = json.load(file)
        return file_things


def load_unused():
    with open(f"{data_folder}/unused.json", "r") as file:
        file_things = json.load(file)
        return file_things


def load_samples():
    with open(f"{data_folder}/samples.json", "r") as file:
        file_things = json.load(file)
        return file_things


used = load_used()
unused = load_unused()
samples = load_samples()
all_things = used + unused + samples

# De-dupe
dupes = []
for thing in unused:
    if thing in used or thing in samples:
        dupes.append(thing)
for d in dupes:
    unused.remove(d)
unused = list(dict.fromkeys(unused))


def get_similarity_info(thing, all_things):
    thingNLP = nlp(thing)
    most_similar = (0, "", "")
    for t in all_things:
        if t == thing:
            # Comparing to itself, ignore
            continue
        tNLP = nlp(t)
        similarity = thingNLP.similarity(tNLP)
        if similarity > most_similar[0]:
            most_similar = (similarity, thing, t)
    return most_similar


with open(f"{data_folder}/unused.json", "w") as file:

    # Sort used by least similarity
    unused_sim_infos = []
    for t in unused:
        t_sim_info = get_similarity_info(t, used + samples)
        if t_sim_info[0] < 0.95:
            unused_sim_infos.append(t_sim_info)

    unused_sim_infos.sort(key=lambda sim_info: sim_info[0])
    things_sorted = [s[1] for s in unused_sim_infos]
    # print(things_sorted)
    json.dump(things_sorted, file)
