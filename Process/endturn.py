from . import Json
from pathlib import Path

def buh (counter):
    data = Json.loadjson (Path ("./json/save.json"))
    counter = data ["counter"]
    counter += 1
    Json.writejson (Path ("./json/save.json") , counter , 2)
    return data ["counter"]