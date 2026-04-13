import math

def hp(zone):
      zone = zone * 2
      hp = 10 * math.log(zone , 1.2)
      hp = math.trunc(hp)
      return hp

def attack (zone):
    if zone < 5:
      zone = zone - 1
      mult = math.pow(math.e, 0.2 * zone)
      attack = 10 + 5 * mult
      attack = math.trunc(attack)
      return attack
    elif zone > 50: #wanted to somewhat limit attack later 
      zone = zone
      thingy = math.pow(0.9, zone-49)
      mult = (math.pow(math.e, 0.15 * zone) + math.pow(math.e, 0.1 * zone)) * thingy
      attack = 10 + 5 * mult
      attack = math.trunc(attack)
      return attack
    else:    #simulates artillery bveing added
      zone = zone
      mult = (math.pow(math.e, 0.125 * zone) + math.pow(math.e, 0.1 * zone))
      attack = 10 + 5 * mult
      attack = math.trunc(attack)
      return attack

def org (zone):
      zone = zone * 8
      org = 10 * math.log(zone , 2)
      org = math.trunc(org)
      return org

def defense (zone):
    if zone < 10:
      defense = 20 + math.pow(zone , 1.2)
      defense = math.trunc(defense)
      return defense
    else:    #simulates tanks being added
        defense = 100 + math.pow(1.5 , math.log(zone * 50 , 1.65))
        defense = math.trunc(defense)
        return defense

def breakthrough (zone):
    if zone < 10:
      breakthrough = 20 + math.pow(zone , 1.2)
      breakthrough = math.trunc(breakthrough)
      return breakthrough
    else:    #simulates tanks being added
        breakthrough = 20 + math.pow(1.5 , math.log(zone * 50 , 1.75))
        breakthrough = math.trunc(breakthrough)
        return breakthrough
    

def pierce (zone):
    zone = zone * 1.5
    pierce = 10 * math.log(zone , 1.67)
    pierce = math.trunc(pierce)

    return pierce

def armour (zone):
    if zone < 10:
      armour = 0
      return armour
    elif zone > 9 and zone < 50:    #simulates tanks being added
      armour = 25 + (7 * math.log(zone - 8 , 1.5))
      armour = math.trunc(armour)
      return armour
    else:
      armour = 25 + (7 * math.log(zone - 8 , 1.2))
      armour = math.trunc(armour)
      return armour


def entrenchment (zone): #provices a % increase to defense and attack when defending
    entrenchment = zone
    entrenchment = math.trunc(entrenchment)
    return entrenchment