import json

file = "data/All_Beauty.jsonl"

with open(file, 'r') as fp:
    for line in fp:
        print(json.loads(line.strip()))