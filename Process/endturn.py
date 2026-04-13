from . import Json
from pathlib import Path
import time
import os

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
    steel = data ["steel"]
    rawcopper = data ["raw copper"]
    copper = data ["copper"]
    oil = data ["oil"]
    raremetals = data ["rare metals"]


    ironmine = data ["iron mine"]
    ironfoundry = data ["iron foundry"]
    coalmine = data ["coal mine"]
    steelmill = data ["steel mill"]
    coppermine = data ["copper mine"]
    copperfoundry = data ["copper foundry"]
    pumpjack = data ["pumpjack"]
    raremetalfoundry = data ["rare metal foundry"]
    
    rawironstart = rawiron
    coalstart = coal
    ironstart = iron
    steelstart = steel
    rawcopperstart = rawcopper
    copperstart = copper
    oilstart = oil
    raremetalsstart = raremetals


    #calculate coal needed, if not enough, then only mines will work for that turn and no industry will fire
    coalneeded = ironfoundry + info ["type"] [3] ["details"] ["input"] ["coal"] * steelmill + raremetalfoundry * info ["type"] [6] ["details"] ["input"] ["coal"] + pumpjack * info ["type"] [7] ["details"] ["input"] ["coal"] + copperfoundry * info ["type"] [5] ["details"] ["input"] ["coal"]
    rawcopperneeded = info ["type"] [5] ["details"] ["input"] ["raw copper"] * copperfoundry
    rawironneeded = info ["type"] [2] ["details"] ["output"] ["iron"] * ironfoundry
    ironneeded = info ["type"] [3] ["details"] ["input"] ["iron"] * steelmill


    #load raw resources first to enable proper usage of processing buildings
    rawiron = rawiron + (info ["type"] [1] ["details"] ["output"] ["raw iron"] * ironmine) #the 1 shows the index of the iron mine in "type"
    rawcopper = rawcopper + (info ["type"] [4] ["details"] ["output"] ["raw copper"] * coppermine)
    coal = coal + (info ["type"] [0] ["details"] ["output"] ["coal"] * coalmine) 
    

    if coal < coalneeded:
        print("there was not enough coal to fire your industry, but your mines still produced resources")
        time.sleep(2)
        #calcualate all processed resources
    else:
        if rawiron >= rawironneeded:
            iron = iron + (info ["type"] [2] ["details"] ["output"] ["iron"] * ironfoundry)
            rawiron = rawiron - rawironneeded
        else:
            print("there was no ore to smelt in your iron foundries...")
            time.sleep(2)

        if iron >= ironneeded:
            steel = steel + (info ["type"] [3] ["details"] ["output"] ["steel"] * steelmill)
            iron = iron - ironneeded
        else:
            print("there was not enough iron to smelt in your steel mills...")
            time.sleep(2)
        
        if rawcopper >= rawcopperneeded:
            copper = copper + (info ["type"] [5] ["details"] ["output"] ["copper"] * copperfoundry)
            rawcopper = rawcopper - rawcopperneeded
        else:
            print("there was no ore to smelt in your copper foundries...")
            time.sleep(2)

        coal = coal - coalneeded


    #save all value to the save file
    data ["iron"] = iron
    data ["raw iron"] = rawiron
    data ["coal"] = coal
    data ["steel"] = steel
    data ["copper"] = copper
    data ["raw copper"] = rawcopper
    data ["oil"] = oil
    data ["rare metals"] = raremetals
    Json.writejson (data, Path ("./json/save.json") , 2)

    ironchange = iron - ironstart
    rawironchange = rawiron - rawironstart
    coalchange = coal - coalstart
    steelchange = steel - steelstart
    copperchange = copper - copperstart
    rawcopperchange = rawcopper - rawcopperstart
    oilchange = oil - oilstart
    raremetalschange = raremetals - raremetalsstart


    print(f"coal change: {coalchange}")
    print(f"raw iron change: {rawironchange}")
    print(f"iron change: {ironchange}")
    print(f"raw copper change: {rawcopperchange}")
    print(f"copper change: {copperchange}")
    print(f"steel change: {steelchange}")
    print(f"oil change: {oilchange}")
    print(f"rare metals change: {raremetalschange}")


    return iron, rawiron, coal, steel

def unlock():
    data = Json.loadjson (Path ("./json/save.json"))

    if data ["steel"] >= 10:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("you have unlocked copper!!!")
        time.sleep(2)
        data ["copperunlock"] = 1
        Json.writejson (data, Path ("./json/save.json") , 2)


def divcreate(cost , steel , copper , raremetals , oil):
    os.system('cls' if os.name == 'nt' else 'clear')
    data = Json.loadjson (Path ("./json/save.json"))
    if data ["divisionmade"] == 0:
      
      div = 0
      moneyhad = data ["money"]
      steelhad = data ["steel"]
      copperhad = data ["copper"]     #save file rescources
      raremetalshad = data ["rare metals"]
      oilhad = data ["oil"]
      print(moneyhad , cost)
      print(steelhad, steel)
      print(copperhad , copper)
      print(raremetalshad , raremetals) 
      print(oilhad , oil)
  
      if moneyhad >= cost:
          div = div + 1
      else:
          print("not enough money to create division")
    
      if steelhad >= steel:
          div += 1
      else:
          print("not enough steel to create division")
    
      if copperhad >= copper:
          div += 1
      else:
          print("not enough copper to create division")
  
      if raremetalshad >= raremetals:
          div += 1
      else:
          print("not enough rare metals to create division")
   
      if oilhad >= oil:
          div += 1
      else:
          print("not enough oil to create division")
    
      if div == 5:
          print("division created")
          data ["money"] = moneyhad - cost
          data ["steel"] = steelhad - steel
          data ["copper"] = copperhad - copper
          data ["rare metals"] = raremetalshad - raremetals
          data ["oil"] = oilhad - oil
          data ["divisionmade"] = 1
          data ["divisionjustmade"] = 1
          Json.writejson (data, Path ("./json/save.json") , 2)
      time.sleep(5)
    








