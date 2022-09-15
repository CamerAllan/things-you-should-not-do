# Things Generator

## Prerequisites

Install requirements.txt, then grab the sentance similarity model with `python -m spacy download en_core_web_sm`

## How to use

- `python3 src/1_generate_things.py <path to data folder> -n <num things to generate>`
    - This will add n things to `data/unused.json`
- `python3 src/2_sort_things.py  <path to data folder>`
    - This will clean up `data/unused.json`
        - Remove duplicates
        - Sort by least similar to existing things
- `python3 src/3_build_things.py  <path to data folder> <path to output folder> -n <num things to take>`
    - Takes `n` things from the top of `unused.json`
    - Adds them to `used.json`
    - Creates a part file