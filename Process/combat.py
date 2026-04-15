from . import Json
from pathlib import Path
import math


savepath = Path ("./json/save.json")

#both divisions will fight full power for that turn - stat penalties applied after combat happens


def combatdef(defense, entrenchment, recon):
  if recon > 4:
    entrenchment = entrenchment / 5*recon
  defense = defense * (entrenchment / 100)
  return defense

def combatatt(attack, entrenchment, recon):
  if recon > 4:
    entrenchment = entrenchment / 5*recon
  attack = attack * (entrenchment / 100)
  return attack

def orgstatchange (Iatt , Idef , Ibreak , Iorg): #initialattack etc

  save = Json.loadjson (savepath)

  Corg = save["divisionorg"]  #current org
  orgmult = (Corg / Iorg) ** 2

  attack = orgmult * Iatt
  defense = orgmult * Idef
  breakthrough = orgmult * Ibreak

  if attack < 0.1 * Iatt:
    attack = 0.1 * Iatt
  if defense < 0.1 * Idef:
    defense = 0.1 * Idef
  if breakthrough < 0.1 * Ibreak:
    breakthrough = 0.1 * Ibreak

  attack = math.trunc(attack)
  defense = math.trunc(defense)
  breakthrough = math.trunc(breakthrough)

  return attack , defense , breakthrough

def enemyorgstatchange (Iatt , Idef , Ibreak , Iorg): #initialattack etc

  save = Json.loadjson (savepath)

  Corg = save["enemyorg"]  #current org
  orgmult = (Corg / Iorg) ** 2

  attack = orgmult * Iatt
  defense = orgmult * Idef
  breakthrough = orgmult * Ibreak

  if attack < 0.1 * Iatt:
    attack = 0.1 * Iatt
  if defense < 0.1 * Idef:
    defense = 0.1 * Idef
  if breakthrough < 0.1 * Ibreak:
    breakthrough = 0.1 * Ibreak

  attack = math.trunc(attack)
  defense = math.trunc(defense)
  breakthrough = math.trunc(breakthrough)

  return attack , defense , breakthrough

def divfight (attack , breakthrough , pierce , recon , entrenchment , opphp , opporg , oppdefense , opparmour , oppentrenchment):   #player fights enemy unit 

  save = Json.loadjson (savepath)

  attack = combatatt(attack , entrenchment , 0) #enemies have no recon stat , putting in 0 here ensures they get no recon bonuses
  oppdefense = combatdef(oppdefense , oppentrenchment , recon)

  if pierce > opparmour:
    attack = attack #unchanged duhh
  elif pierce < opparmour and pierce > 0.5 * opparmour:
    attack = attack * 0.7
  else:
    attack = attack * 0.4

  if attack > 2 * oppdefense:  #if the enemy is low on defense for any reason - do 3x damage
    attack = attack * 3

  damage = attack / ((10 * oppdefense) * (1 / breakthrough))
  damage = math.trunc(damage)
  opphp = opphp - damage

  orgdamage = breakthrough / oppdefense 
  orgdamage = math.trunc(orgdamage)
  opporg = opporg - orgdamage

  if orgdamage < 1:   #orgdamage doesnt fall below 1, so you can always deal at least something to the enemy
      opporg = opporg - 1
      orgdamage = 1

  if opporg < 0:
    opporg = 0

  if opporg == 0:     #the enemy takes more damage when their org is completely depleted to speed up turns
      opphp = opphp - (damage + (orgdamage / 3))
      opphp = math.trunc(opphp)

  if opphp < 1:
    zone = 0
    money = 0
    save ["enemyjustmade"] = 1
    zone = save ["zone"]
    zone = zone + 1
    save ["zone"] = zone
    reward = 100 * (zone ** 1.1)
    reward = math.trunc(reward)
    cuurentmoney = save["money"]
    money = cuurentmoney + reward
    save ["money"] = money
    print ("the enemy has been overrun!")
    print (f"we have earned {reward} money from the enemy!")
  else:
    print(f"we dealt {damage} damage to the enemy and {orgdamage} org damage")
    save ["enemyhp"] = opphp
    save ["enemyorg"] = opporg
  Json.writejson(save , savepath , 2)


def enemyfight(attack , breakthrough , pierce ,  entrenchment , opphp , opporg , oppdefense , opparmour , recon , oppentrenchment):   #enemy unit fights player

  save = Json.loadjson (savepath)

  attack = combatatt(attack , entrenchment , recon)
  oppdefense = combatdef(oppdefense , oppentrenchment , 0) #enemies have no recon stat , putting in 0 here ensures they get no recon bonuses

  if pierce > opparmour:
    attack = attack #unchanged duhh
  elif pierce < opparmour and pierce > 0.5 * opparmour:
    attack = attack * 0.7
  else:
    attack = attack * 0.4

  if attack > 2 * oppdefense:  #if the enemy is low on defense for any reason - do 3x damage
    attack = attack * 3

  if save["enemyjustmade"] == 0:
    damage = attack / ((10 * oppdefense) * (1 / breakthrough))   #calculate damage done
    damage = math.trunc(damage)
    opphp = opphp - damage

    orgdamage = breakthrough / oppdefense   #calculate org damage done
    orgdamage = math.trunc(orgdamage)
    opporg = opporg - orgdamage

    if orgdamage < 1:   #orgdamage doesnt fall below 1, so you can always deal at least something to the enemy
      opporg = opporg - 1
      orgdamage = 1

    if opporg < 0:   #dont let org become negative
      opporg = 0
    
    if opporg == 0:     #the enemy takes more damage when their org is completely depleted to speed up turns
      opphp = opphp - (damage + (orgdamage / 3))
      opphp = math.trunc(opphp)

    if opphp < 1:
      save["divisionmade"] = 0
      print ("our forces have been defeated!")
    else:
      print(f"they dealt {damage} damage to us and {orgdamage} org damage")
      save ["divisionhp"] = opphp
      save ["divisionorg"] = opporg
    Json.writejson(save , savepath , 2)


  

