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

    rawiron = data ["raw iron"]
    coal = data ["coal"]
    iron = data ["iron"]

    ironmine = data ["iron mine"]
    ironfoundry = data ["iron foundry"]
    coalmine = data ["coal mine"]
    
    rawironstart = rawiron
    coalstart = coal
    ironstart = iron

    #calculate coal needed, if not enough, then only mines will work for that turn and no industry will fire
    coalneeded = ironfoundry 

    #load raw resources first to enable proper usage of processing buildings
    rawiron = rawiron + (info ["type"] [1] ["details"] ["output"] ["raw iron"] * ironmine) #the 1 shows the index of the iron mine in "type"
    coal = coal + (info ["type"] [0] ["details"] ["output"] ["coal"] * coalmine) 

    if coal < coalneeded:
        print("there was not enough coal to fire your industry, but your mines still produced resources")
        #calcualate all processed resources
    else:
        iron = iron + (info ["type"] [2] ["details"] ["output"] ["iron"] * ironfoundry)
        rawiron = rawiron - (info ["type"] [2] ["details"] ["output"] ["iron"] * ironfoundry)
        if rawiron < 0: #if raw iron falls below 0, reverse what i just did 
            iron = iron - (info ["type"] [2] ["details"] ["output"] ["iron"] * ironfoundry)
            rawiron = rawiron + (info ["type"] [2] ["details"] ["output"] ["iron"] * ironfoundry)
        
        coal = coal - coalneeded


    #save all value to the save file
    data ["iron"] = iron
    data ["raw iron"] = rawiron
    data ["coal"] = coal
    Json.writejson (data, Path ("./json/save.json") , 2)

    ironchange = iron - ironstart
    rawironchange = rawiron - rawironstart
    coalchange = coal - coalstart

    print(f"coal change: {coalchange}")
    print(f"raw iron change: {rawironchange}")
    print(f"iron change: {ironchange}")

    return iron, rawiron, coal





