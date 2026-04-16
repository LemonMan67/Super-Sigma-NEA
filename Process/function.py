from . import Json
from pathlib import Path

def divchange (edit , batt):             
    div = Json.loadjson (Path ("./json/division.json"))
    div [edit] = batt                                        #this is solely used for changing the contents of the division.json file - allowing for division editing
    Json.writejson (div, Path ("./json/division.json") , 2)  #did this need its own file? absoltely not - but hey ho
