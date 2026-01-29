from . import Json
from pathlib import Path

def buh (counter):
    data = Json.loadjson (Path ("./json/save.json"))
    counter = data ["counter"]
    counter += 1
    data["counter"] = counter
    Json.writejson (data, Path ("./json/save.json") , 2)
    return counter

def rescource (iron, rawiron, coal, ironmine, ironfoundry, coalmine):
    data = Json.loadjson (Path ("./json/save.json"))
    info = Json.loadjson (Path ("./json/building.json"))
    #load raw resources first to enable proper usage of processing buildings
    rawiron = rawiron + (info ["type"] [1] ["details"] ["output"] ["raw iron"] * ironmine) #the 1 shows the index of the iron mine in "type"
    coal = coal + (info ["type"] [0] ["details"] ["output"] ["coal"] * coalmine) 
    
    #calcualate all processed resources
    iron = iron + (info ["type"] [2] ["details"] ["output"] ["iron"] * ironfoundry)
    rawiron = rawiron - (info ["type"] [2] ["details"] ["output"] ["iron"] * ironfoundry)
    if rawiron < 0: #if raw iron falls below 0, reverse what i just did 
        iron = iron - (info ["type"] [2] ["details"] ["output"] ["iron"] * ironfoundry)
        rawiron = rawiron + (info ["type"] [2] ["details"] ["output"] ["iron"] * ironfoundry)

    #save all value to the save file
    data ["iron"] = iron
    data ["raw iron"] = rawiron
    data ["coal"] = coal
    Json.writejson (data, Path ("./json/save.json") , 2)

