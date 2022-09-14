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

things_filepath = f"{data_folder}/things.json"
adjectives_filepath = f"{data_folder}/prompt-adjectives.txt"
n = args.n
similarity_threshold = args.s

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


def get_similarity_info(thing, all_things):
    thingNLP = nlp(thing)
    most_similar = (0, "")
    for t in all_things:
        tNLP = nlp(t)
        similarity = thingNLP.similarity(tNLP)
        if similarity > most_similar[0]:
            most_similar = (similarity, thing, t)
    return most_similar


def generate_prompt_examples_sample(n: int):
    return random.sample(samples, n)


def generate_prompt(prompt_examples_sample):
    with open(adjectives_filepath, "r") as adjectives_file:
        adjective_1 = random_line(adjectives_file).strip()

    prompt_start = f"Physically Improbable, {adjective_1}, Silly Things You Should Not Do (in the imperative tense):\n"

    prompt = prompt_start
    for sample_example in prompt_examples_sample:
        prompt += f"\n- {sample_example}"
    prompt += "\n-"

    return prompt


def generate(prompt) -> str:
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=1,
        max_tokens=500,
        top_p=1,
        best_of=2,
        frequency_penalty=0.1,  # Too high and we'll have opposite effect - remember the ratio of samples to insertions
        presence_penalty=0.7,
        stop=["\n"],
    )

    text = response.get("choices")[0]["text"]

    return text.strip()


def generate_n(n: int, similarity_threshold) -> dict:
    things = []
    for i in range(0, n):
        # Prepend things we've already generated so that penalties apply
        # Prepend because last thing in list has outsized influence
        samples = things + generate_prompt_examples_sample(n + i)
        prompt = generate_prompt(samples)
        thing = generate(prompt)
        thing_similarity = get_similarity_info(thing, all_things)
        things.append(thing_similarity)

    print("before sort")
    print(things)
    things_sorted_by_similarity = thing.sort(key=lambda x: x[0])
    print("after sort")
    print(things_sorted_by_similarity)
    return things_sorted_by_similarity


with open(f"{data_folder}/catalogue.json", "r") as catalogue_file:
    catalogue = json.load(catalogue_file)
    previousPart = catalogue["latest"]
    newPart = previousPart + 1

    newThings = generate_n(n, similarity_threshold)

    things = {"oldThings": [], "newThings": newThings}

    # Write the things file
    with open(f"{data_folder}/parts/{newPart}.json", "w") as json_file:
        json.dump(things, json_file)

    # Calculate new catalogue values
    previousCatalogueItem = catalogue["all"][f"{previousPart}"]
    previousStartNum = int(previousCatalogueItem["startNum"])
    previousCount = int(previousCatalogueItem["count"])
    newStartNum = previousStartNum + previousCount
    newCount = len(newThings)


with open(f"{data_folder}/catalogue.json", "w") as catalogue_file:
    # Update and write the catalogue
    catalogue["latest"] = newPart
    catalogue["all"][newPart] = {"startNum": newStartNum, "count": newCount}

    json.dump(catalogue, catalogue_file)
