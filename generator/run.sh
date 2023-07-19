#!/bin/bash
# This is a script to generate, commit, and push changes to the master branch of a git repo
# I can't recommend doing this but here we are

# Stay safe out there
set -Eeuox pipefail

# Get latest changes
git pull --rebase

# Choose a random number of entries
NUM=$(shuf -i 10-18 -n 1)

# Run the thing (my python install is goobered and cron doesn't know about PATH so this is how it is)
/usr/lib/python-exec/python3.10/python src/1_generate_things.py ./data -n $NUM
/usr/lib/python-exec/python3.10/python src/2_sort_things.py ./data 
/usr/lib/python-exec/python3.10/python src/3_build_things.py ./data ./out -n $NUM

echo "Generatiom complete"

# Copy the outputs into the public directory of the UI
cp ./out/parts/* ../ui/public/data/parts
cp ./data/catalogue.json ../ui/public/data/catalogue.json

# Add all the changes
git add --all

# Commit em
COMMIT_MESSAGE="Generate content - $(date '+%Y-%m-%d')"
git commit -m "${COMMIT_MESSAGE}"

# Push em
git push

echo "Done!"
