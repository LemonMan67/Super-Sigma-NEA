import json 
from pathlib import Path

def loadjson (filepath):
    with open (filepath , "r" ) as f:    #used to load data from a json file
        return json.load (f)

def writejson (update , filepath , x ) : 
    with open (filepath , "w") as f:            #used to save data to a json file
        json.dump(update , f , indent = 2)