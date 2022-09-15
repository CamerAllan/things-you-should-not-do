set -Eeuo pipefail

python3 src/1_generate_things.py ./data -n $1
python3 src/2_sort_things.py ./data 
python3 src/3_build_things.py ./data ./out -n $1

cp ./out/parts/* ../ui/public/data/parts
cp ./data/catalogue.json ../ui/public/data/catalogue.json