#!/bin/bash
# This is a script to generate, commit, and push changes to the master branch of a git repo
# I can't recommend doing this but here we are

# Stay safe out there
set -Eeuox pipefail

# Get latest changes
git pull --rebase

# Run the thing
python3 src/1_generate_things.py ./data -n $1
python3 src/2_sort_things.py ./data 
python3 src/3_build_things.py ./data ./out -n $1

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


