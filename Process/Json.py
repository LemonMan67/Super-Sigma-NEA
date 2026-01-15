import json 
from pathlib import Path

def loadjson (filepath):
    with open (filepath , "r" ) as f:
        return json.load (f)

def writejson (update , filepath , x ) :
    with open (filepath , "w") as f:
        json.dump(update , f , indent = 2)