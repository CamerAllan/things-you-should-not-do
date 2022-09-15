import os
import json
import argparse
from helpers.helpers import load_unused, load_used, write_unused, write_used


parser = argparse.ArgumentParser()
parser.add_argument("data_folder", help="path to data folder")
parser.add_argument("out_folder", help="path to output folder")
parser.add_argument("-n", type=int, default=10)

# Parse and print the results
args = parser.parse_args()
data_folder = args.data_folder
if data_folder is None:
    print("Uh oh!")
    exit(1)

out_folder = args.out_folder
if out_folder is None:
    print("Uh oh!")
    exit(1)

n = args.n

# BEGIN LOGIC -----------------------------------------------------------------

used = load_used(data_folder)
unused = load_unused(data_folder)

newThings = unused[0:n]

# Remove taken elements from unused
unused = unused[n:]

# Add taken elements to used
used += newThings

# Write back used and unused
write_used(used, data_folder)
write_unused(unused, data_folder)

with open(f"{data_folder}/catalogue.json", "r") as catalogue_file:
    catalogue = json.load(catalogue_file)
    previousPart = catalogue["latest"]
    newPart = previousPart + 1

    newThingsDict = {"oldThings": [], "newThings": newThings}

    # Write the things file
    with open(f"{out_folder}/parts/{newPart}.json", "w") as json_file:
        json.dump(newThingsDict, json_file)

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
