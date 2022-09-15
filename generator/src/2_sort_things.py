import argparse
import spacy
from helpers.helpers import (
    load_samples,
    load_unused,
    load_used,
    random_line,
    write_unused,
)

parser = argparse.ArgumentParser()
parser.add_argument("data_folder", help="path to data folder")

# Parse and print the results
args = parser.parse_args()
data_folder = args.data_folder
if data_folder is None:
    print("Uh oh!")
    exit(1)

# BEGIN LOGIC -----------------------------------------------------------------

# Init NLP for determining sentance similarity
nlp = spacy.load("en_core_web_sm")

used = load_used(data_folder)
unused = load_unused(data_folder)
samples = load_samples(data_folder)
all_things = used + unused + samples

# De-dupe
dupes = []
for thing in unused:
    if thing == "" or thing in used or thing in samples:
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


# Sort used by least similarity
unused_sim_infos = []
for t in unused:
    t_sim_info = get_similarity_info(t, used + samples)
    if t_sim_info[0] < 0.85:
        unused_sim_infos.append(t_sim_info)

unused_sim_infos.sort(key=lambda sim_info: sim_info[0])
things_sorted = [s[1] for s in unused_sim_infos]
# print(things_sorted)
write_unused(things_sorted, data_folder)
