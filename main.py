import json 
from pathlib import Path

with open ("battalion.json" , "r") as file:
    f = json.load(file)
for x in f['tank']:
    print (x)


a = json.dumps(f , indent = 2)
print(a)

