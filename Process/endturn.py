from . import Json
from pathlib import Path

def buh (counter):
    data = Json.loadjson (Path ("./json/save.json"))
    counter = data ["counter"]
    counter += 1
    data["counter"] = counter
    Json.writejson (data, Path ("./json/save.json") , 2)
    return counter