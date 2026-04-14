import Json
from pathlib import Path


savepath = Path ("./json/save.json")
save = Json.loadjson (savepath)


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
  
  Corg = save["divisionorg"]  #current org
  orgmult = (Corg / Iorg) ** 2

  attack = orgmult * Iatt
  defense = orgmult * Idef
  breakthrough = orgmult * Ibreak

  return attack , defense , breakthrough

def enemyorgstatchange (Iatt , Idef , Ibreak , Iorg): #initialattack etc
  
  Corg = save["enemyorg"]  #current org
  orgmult = (Corg / Iorg) ** 2

  attack = orgmult * Iatt
  defense = orgmult * Idef
  breakthrough = orgmult * Ibreak

  return attack , defense , breakthrough
  

