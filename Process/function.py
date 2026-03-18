from . import Json
from pathlib import Path

def divchange (edit , batt):
    div = Json.loadjson (Path ("./json/division.json"))
    div [edit] = batt
    Json.writejson (div, Path ("./json/division.json") , 2)
