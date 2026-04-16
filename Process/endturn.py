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


    print(f"\ncoal change: {coalchange}")
    print(f"raw iron change: {rawironchange}")
    print(f"iron change: {ironchange}")
    print(f"raw copper change: {rawcopperchange}")
    print(f"copper change: {copperchange}")
    print(f"steel change: {steelchange}")
    print(f"oil change: {oilchange}")
    print(f"rare metals change: {raremetalschange}")


    return iron, rawiron, coal, steel

def unlock():     #checks if a condition is met and if that unlock hasnt been done before - if the condition is met and the unlock hasnt happend before - the thing is unlocked and a message is displayed
    save = Json.loadjson (Path ("./json/save.json"))
    os.system('cls' if os.name == 'nt' else 'clear')

    if save ["steel"] >= 10 and save ["copperunlock"] == 0:
        print("you have unlocked copper!!!")
        time.sleep(2)                                                 #rescources are unlocked here 
        save ["copperunlock"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 5 and save ["oilunlock"] == 0:
        print("you have unlocked oil!!! - this is used in fuelling vehicles - like AT and IFVs")
        time.sleep(2)
        save ["oilunlock"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 10 and save ["raremetalsunlock"] == 0:
        print("you have unlocked rare metals!!! - this is used in building advanced equipment like tanks and more modern equipment")
        time.sleep(2)
        save ["raremetalsunlock"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2) 



    if save ["zone"] >= 15 and save ["infCW"] == 0:
        print("you can upgrade your infantry to the cold war era now!")
        time.sleep(2)                                                             #CW upgrades are unlocked here 
        save ["CW"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2) 
    
    if save ["zone"] >= 16 and save ["artilleryCW"] == 0:
        print("you can upgrade your artillery to the cold war era now!")
        time.sleep(2)
        save ["artilleryCW"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 17 and save ["AACW"] == 0:
        print("AA can be upgraded to CW era now")
        time.sleep(2)
        save ["AACW"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 18 and save ["IFVCW"] == 0:
        print("IFV can be upgraded to the CW now")
        time.sleep(2)
        save ["IFVCW"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 19 and save ["ATCW"] == 0:
        print("AT can be upgraded to the CW era now!")
        time.sleep(2)
        save ["ATCW"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 20 and save ["tankCW"] == 0:
        print("tanks can be upgraded to the CW now")
        time.sleep(2)
        save ["tankCW"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)



    if save ["zone"] >= 25 and save ["infmodern"] == 0:
        print("infantry can be upgraded to the modern era now")         #moddern upgrades unlocked here 
        time.sleep(2)
        save ["infmodern"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 27 and save ["artillerymodern"] == 0:
        print("artillery can be upgraded to modern now!")
        time.sleep(2)
        save ["artillerymodern"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 29 and save ["AAmodern"] == 0:
        print("AA can be made modern now")
        time.sleep(2)
        save ["AAmodern"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 31 and save ["IFVmodern"] == 0:
        print("IFVs can be made modern")
        time.sleep(2)
        save ["IFVmodern"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 33 and save ["ATmodern"] == 0:
        print("AT can be made modern")
        time.sleep(2)
        save ["ATmodern"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)

    if save ["zone"] >= 35 and save ["tankmodern"] == 0:
        print("tanks can be upgraded to the modern era now!")
        time.sleep(2)
        save ["tankmodern"] = 1
        Json.writejson (save, Path ("./json/save.json") , 2)


def divcreate(cost , steel , copper , raremetals , oil):
    os.system('cls' if os.name == 'nt' else 'clear')
    data = Json.loadjson (Path ("./json/save.json"))
    if data ["divisionmade"] == 0:   #loads the save file to see if the division is dead 
      
      div = 0 #a counter
      moneyhad = data ["money"]
      steelhad = data ["steel"]
      copperhad = data ["copper"]     #save file rescources are loaded
      raremetalshad = data ["rare metals"]
      oilhad = data ["oil"]
  
      if moneyhad >= cost:
          div = div + 1  #a counter increases for each successful check
      else:
          print("\nnot enough money to create division")
    
      if steelhad >= steel:
          div += 1
      else:
          print("\nnot enough steel to create division")
    
      if copperhad >= copper:
          div += 1
      else:
          print("\nnot enough copper to create division")
  
      if raremetalshad >= raremetals:
          div += 1
      else:
          print("\nnot enough rare metals to create division")
   
      if oilhad >= oil:
          div += 1
      else:
          print("\nnot enough oil to create division")
    
      if div == 5:    #if all 5 checks pass - i have enough material and money to make the division!
          print("division created")
          data ["money"] = moneyhad - cost
          data ["steel"] = steelhad - steel
          data ["copper"] = copperhad - copper
          data ["rare metals"] = raremetalshad - raremetals
          data ["oil"] = oilhad - oil
          data ["divisionmade"] = 1 #sets the division to be alive - when this is 0 , it allows for a new division to be made 
          data ["divisionjustmade"] = 1   #setting this to one allows for the stats of a new division to be loaded into the division object - it is set to 0 then
          Json.writejson (data, Path ("./json/save.json") , 2)
      time.sleep(3)
    








