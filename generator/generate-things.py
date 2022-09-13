import os
import openai
import json
import argparse

openai.api_key = os.getenv("OPENAI_API_KEY")


parser = argparse.ArgumentParser()
parser.add_argument("data-folder", help="path to data folder")
parser.add_argument("-n", type=int, default=18)

# Parse and print the results
args = parser.parse_args()
data_folder = args.data_folder
if data_folder is None:
    print("Uh oh!")
    exit(1)

n = args.n


def generate() -> str:
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Silly, Dangerous Things You Should Not Do:\n\n- Eat Tide Pods\n- Walk on stilts in a thunderstorm\n- Set off fireworks at a gas station\n- Feed your cat treats that are the exact shape and texture of a human hand\n- Lean over a geyser vent and try to look down into it\n- Fly a hot-air balloon over a firing range\n- Peel away the earth's crust\n- Try to paint the Sahara Desert by hand\n- Remove someone's bones without asking\n- Spend 100% of your government's budget on mobile game in-app purchases\n- Fill a lava lamp with actual lava\n- Drink the blood of someone with a viral hemorraghic (sic) fever\n- Eat meat from rabid animals\n- Perform your own laser eye surgery\n- Tell California poultry regulators that your farm is selling Pokemon eggs\n- Funnel the entire flow of Niagara Falls into the open window of a physics lab\n- Pump ammonia into your abdomen\n- Suspend yourself inside a 10-meter ball of sunscreen and fall into the Sun\n-",
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        best_of=1,
        frequency_penalty=0.11,
        presence_penalty=0.32,
        stop=["\n"],
    )

    print(response)

    text = response.get("choices")[0]["text"]

    return text.strip()


def generate_n(n: int) -> dict:

    things = []
    for i in range(0, n):
        thing = generate()
        things += thing
        print(thing)

    return things


with open(f"{data_folder}/catalogue.json", "r+") as catalogue_file:
    catalogue = json.load(catalogue_file)
    previousPart = catalogue["latest"]
    newPart = previousPart + 1

    newThings = generate_n(n)

    things = {"oldThings": [], "newThings": newThings}

    # Write the things file
    with open(f"{data_folder}/parts/.json", "w") as json_file:
        json.dump(things, json_file)

    # Calculate new catalogue values
    previousCatalogueItem = catalogue["all"][-1]
    previousStartNum = int(previousCatalogueItem["startNum"])
    previousCount = int(previousCatalogueItem["count"])
    newStartNum = previousStartNum + previousCount
    newCount = len(newThings)

    # Update and write the catalogue
    catalogue["latest"] = newPart
    catalogue["all"][newPart] = {"startNum": newStartNum, "count": newCount}

    json.dump(catalogue, catalogue_file)
