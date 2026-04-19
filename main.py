from pathlib import Path
import time
import os
from Process import endturn
from Process import Json
from Process import function
from Process import statcalc 
from Process import enemycalc
from Process import combat

#change values in battlalion json file

class Division:
      def __init__(self, filepath = "./json/division.json"):
         self.path = Path (filepath)  
         self.div = Json.loadjson (self.path)
         self.battalionpath = Path ("./json/battalion.json")
         self.bat = Json.loadjson (self.battalionpath)
         self.savepath = Path ("./json/save.json")
         self.save = Json.loadjson (self.savepath)
         self.batcostpath = Path ("./json/battalioncost.json")
         self.batc = Json.loadjson (self.batcostpath)
         self.tankera = self.save ["tankera"]
         self.IFVera = self.save ["IFVera"]
         self.Infera = self.save ["Infera"]
         self.artera = self.save ["artera"]
         self.AAera = self.save ["AAera"]
         self.ATera = self.save ["ATera"]
         self.a1 = self.div["a1"]
         self.a2 = self.div["a2"]
         self.a3 = self.div["a3"]              #loads all battalion types for each battalion in the division - will be used to find div stats
         self.a4 = self.div["a4"]
         self.b1 = self.div["b1"]
         self.b2 = self.div["b2"]
         self.b3 = self.div["b3"]
         self.b4 = self.div["b4"]
         self.c1 = self.div["c1"]
         self.c2 = self.div["c2"]
         self.c3 = self.div["c3"]
         self.c4 = self.div["c4"]
         self.d1 = self.div["d1"]
         self.d2 = self.div["d2"]
         self.d3 = self.div["d3"]
         self.d4 = self.div["d4"]
         self.hp = int(0)
         self.attack = int(0)
         self.org = int(0)
         self.defense = int(0)
         self.breakthrough = int(0)
         self.pierce = int(0)
         self.armour = int(0)
         self.AA = int(0)
         self.recon = int(0)
         self.entrenchment = int(0)
         self.steel = int(0)
         self.copper = int(0)
         self.rare = int(0)
         self.oil = int(0)
         self.cost = int(0)
         self.divlist = [self.a1, self.a2, self.a3, self.a4, self.b1, self.b2, self.b3, self.b4, self.c1, self.c2, self.c3, self.c4, self.d1, self.d2, self.d3, self.d4]

      def reload(self):
         self.div = Json.loadjson(self.path)
         self.tankera = self.save ["tankera"]
         self.IFVera = self.save ["IFVera"]
         self.Infera = self.save ["Infera"]
         self.artera = self.save ["artera"]
         self.AAera = self.save ["AAera"]
         self.ATera = self.save ["ATera"]
         self.a1 = self.div["a1"]
         self.a2 = self.div["a2"]
         self.a3 = self.div["a3"]
         self.a4 = self.div["a4"]
         self.b1 = self.div["b1"]
         self.b2 = self.div["b2"]
         self.b3 = self.div["b3"]
         self.b4 = self.div["b4"]
         self.c1 = self.div["c1"]
         self.c2 = self.div["c2"]
         self.c3 = self.div["c3"]
         self.c4 = self.div["c4"]
         self.d1 = self.div["d1"]
         self.d2 = self.div["d2"]
         self.d3 = self.div["d3"]
         self.d4 = self.div["d4"]
         self.divlist = [self.a1, self.a2, self.a3, self.a4, self.b1, self.b2, self.b3, self.b4, self.c1, self.c2, self.c3, self.c4, self.d1, self.d2, self.d3, self.d4]

      def divstat(self):
         self.hp = round (statcalc.hp(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)
         self.attack = round (statcalc.attack(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)
         self.org = round (statcalc.org(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)
         self.defense = round (statcalc.defense(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)
         self.breakthrough = round (statcalc.breakthrough(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)     #does the stats - passes through the battalions in each tile of a division based on the divlist list , then passes through the eras to work with
         self.pierce = round (statcalc.pierce(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)
         self.armour = round (statcalc.armour(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)
         self.AA = round (statcalc.AA(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)
         self.recon = round (statcalc.recon(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)
         self.entrenchment = round (statcalc.entrenchment(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)

         self.steel = round (statcalc.steel(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)
         self.copper = round (statcalc.copper(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)        #does the material and money cost
         self.rare = round (statcalc.rare(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera), 2)
         self.oil = round (statcalc.oil(self.divlist,	self.tankera,	self.IFVera,	self.Infera,	self.artera,	self.AAera,	self.ATera), 2)
         self.cost = round (statcalc.cost(self.divlist, self.tankera,	self.IFVera,	self.Infera,	self.artera,	self.AAera,	self.ATera), 2)        #please dont check the statcalc file - itll make yandev look like a god
      
      def eracheck(self , era):
         if era == "WW2":
            return 2
         elif era == "CW":   #this does nothing
            return 1
         elif era == "modern":
            return 0

      def statcheck(self):
         self.save = Json.loadjson (self.savepath)
         self.bat = Json.loadjson (self.battalionpath)
         counter = 0
         batlist = [self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera] #both stat and costcheck use a list containt each battalion types era 
         for x in self.bat["battalion"]:                                                         #it will then present the user the stats of that battalion for that era 
                                                                                                 #if i have a WW2 tank and Cw infantry, the program shows the stats for a WW2 tank and a CW infantry
            print (f" Unit:  {x['unit']}")
            for y in x ["list"]:
                if batlist[counter] == y["era"]["type"]:
                  print (f"  is from the {y['era']['type']} era")
                  print (f"  has { y["era"]["hp"]} hp")
                  print (f"  has { y["era"]["org"]} org")
                  print (f"  has { y["era"]["attack"]} attack")
                  print (f"  has { y["era"]["defense"]} defense")           #prints every single stat for every battalion based on what era it is upgraded to
                  print (f"  has { y["era"]["breakthrough"]} breakthrough") #the stats are stored in battalion.json , the era each unit is levelled to is stored in save file
                  print (f"  has { y["era"]["pierce"]} pierce")
                  print (f"  has { y["era"]["armour"]} armour")
                  print (f"  has { y["era"]["AA"]} AA")
                  print (f"  has { y["era"]["recon"]} recon")
                  print (f"  has { y["era"]["entrenchment"]} entrenchment")
                  print (f"  needs { y["era"]["amount"]} units/battalion\n")
            counter += 1

      def costcheck(self):
         self.save = Json.loadjson (self.savepath)
         self.bat = Json.loadjson (self.battalionpath)
         counter = 0
         batlist = [self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera]
         for x in self.batc["battalion"]:
            print (f" Unit:  {x['unit']}")
            for y in x ["list"]:
                if batlist[counter] == y["era"]["type"]:
                  print (f"  is from the {y['era']['type']} era")             #costs saved in battalioncost.json
                  print (f"  costs { y["era"]["cost"]} money")                #similar to above function - but will print the costs for 1 thing in the battalion 
                  print (f"  costs { y["era"]["steel"]} steel")               #gives price of 1 tank - a battalion will need 80
                  print (f"  costs { y["era"]["copper"]} copper")
                  print (f"  costs { y["era"]["rare metals"]} rare metals")
                  print (f"  costs { y["era"]["oil"]} oil\n")
                  print ("amount / unit made - amount of units/battalion is in statcheck")
         counter += 1

      def upgrade(self , unit):
         self.save = Json.loadjson (self.savepath)
         if unit == "infantry" and self.save ["Infera"] == "WW2":    #checks what unit is being upgraded and its current era to reflect what upgrade will be bought , doing this allows the user to type e.g infantry to both upgrade to CW and modern
            cost = self.save["infCWp"] #infcwp = infantry CW price - a constant value stored in the save file for the upgrade cost from WW2 to CW    
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["Infera"] = "CW"     #infera = "infantry era" refers to what era the unit is - stored in the save file
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)     
               time.sleep(2)          

         elif unit == "infantry" and self.save ["Infera"] == "CW":
            cost = self.save["infmodernp"]  #infmodernprice - price stored to upgrade from CW to modern
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["Infera"] = "modern"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)

         elif unit == "tank" and self.save ["tankera"] == "WW2":
            cost = self.save["tankCWp"] 
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["tankera"] = "CW"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)

         elif unit == "tank" and self.save ["tankera"] == "CW":
            cost = self.save["tankmodernp"] 
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["tankera"] = "modern"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)

         elif unit == "IFV" and self.save ["IFVera"] == "WW2":
            cost = self.save["IFVCWp"] 
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["IFVera"] = "CW"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)

         elif unit == "IFV" and self.save ["IFVera"] == "CW":
            cost = self.save["IFVmodernp"] 
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["IFVera"] = "modern"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)

         elif unit == "artillery" and self.save ["artera"] == "WW2":
            cost = self.save["artilleryCWp"] 
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["artera"] = "CW"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)

         elif unit == "artillery" and self.save ["artera"] == "CW":
            cost = self.save["artillerymodernp"] 
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["artera"] = "modern"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)

         elif unit == "AA" and self.save ["AAera"] == "WW2":
            cost = self.save["AACWp"] 
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["AAera"] = "CW"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)

         elif unit == "AA" and self.save ["AAera"] == "CW":
            cost = self.save["AAmodernp"] 
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["AAera"] = "modern"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)

         elif unit == "AT" and self.save ["ATera"] == "WW2":
            cost = self.save["ATCWp"] 
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["ATera"] = "CW"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)

         elif unit == "AT" and self.save ["ATera"] == "CW":
            cost = self.save["AAmodernp"] 
            money = self.save["money"]
            if money <= cost:
               print("not enough money had to upgrade your unit")
               time.sleep(2)
            else:
               money = money - cost
               save["money"] = money
               save["AAera"] = "modern"
               print("unit upgraded!")
               Json.writejson (self.save, self.savepath , 2)         

class Building:
   def __init__(self , filepath = "./json/building.json"):
      self.path = Path (filepath)
      self.data = Json.loadjson (self.path)
      self.savepath = Path ("./json/save.json")
      self.save = Json.loadjson (self.savepath)
      self.money = self.save["money"]

   def buybuilding (self , buildingname ) :
      if buildingname != "iron mine" or buildingname != "iron foundry" or buildingname != "coal mine" or buildingname != "steel mill" or buildingname != "copper mine" or buildingname != "copper foundry":
        self.save = Json.loadjson (self.savepath)
        for x in self.data ["type"]:
          if x ["details"]["building"] == buildingname :
             if self.money >=  int ( x ["details"]["cost"]):     #checks player can afford building Y
               self.money -= int ( x ["details"]["cost"])
               load.money = self.money
               amount = self.save [buildingname]   #increases amount of the building Y by one
               amount += 1        
               self.save [buildingname] = amount
               self.save ["money"] = self.money  #updates money value based on building cost
               Json.writejson (self.save, self.savepath , 2)
               if buildingname == "iron mine":        
                     cost = self.data["type"][1]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3            #this bit essentially increases the cost of each specific building by 1.3x everytime its bought
                     cost = round(cost,1)
                     self.data["type"][1]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)

               elif buildingname == "iron foundry":         
                      cost = self.data["type"][2]["details"]["cost"]
                      cost = int(cost)
                      cost = cost * 1.3
                      cost = round(cost,1)
                      self.data["type"][2]["details"]["cost"] = cost
                      Json.writejson (self.data, self.path , 2)
               
               elif buildingname == "copper mine":
                     cost = self.data["type"][4]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][4]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)
               
               elif buildingname == "copper foundry":
                     cost = self.data["type"][5]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][5]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)

               elif buildingname == "coal mine":
                      cost = self.data["type"][0]["details"]["cost"]
                      cost = int(cost)
                      cost = cost * 1.3
                      cost = round(cost,1)
                      self.data["type"][0]["details"]["cost"] = cost
                      Json.writejson (self.data, self.path , 2)

               elif buildingname == "steel mill":
                     cost = self.data["type"][3]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][3]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)
               
               elif buildingname == "rare metal foundry":
                     cost = self.data["type"][6]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][6]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)

               elif buildingname == "pumpjack":
                     cost = self.data["type"][7]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][7]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)

   def upgradebuilding(self , buildingname , change):  # pretend building name is what is being channged
         self.save = Json.loadjson (self.savepath)
         self.money = self.save["money"]
         if self.money >=  int ( self.save[change]):   #checks the user has enough money for the upgrade
               self.money -= int ( self.save[change])
               load.money = self.money
               self.save ["money"] = self.money   #overwrites money in the save file
               if buildingname == "iron mine":        
                     self.save["iron mine upg cost"] = self.save["iron mine upg cost"] * 5    #increases cost of upgrade by 5*
                     self.data["type"][1]["details"]["output"]["raw iron"] = self.data["type"][1]["details"]["output"]["raw iron"] * 2  #doubles output of that building in the building.json file
                     Json.writejson (self.data, self.path , 2)  #saves new output to building.json
                     Json.writejson (self.save, self.savepath , 2)  #saves upgrade cost to save file

               elif buildingname == "iron foundry":         
                     self.save["iron foundry upg cost"] = self.save["iron foundry upg cost"] * 5
                     self.data["type"][2]["details"]["output"]["iron"] = self.data["type"][2]["details"]["output"]["iron"] * 2  #the input integer is specific to the exact building called
                     Json.writejson (self.data, self.path , 2)                                                                  #the integer is the list position of the specific building in the "type" part of the json file
                     Json.writejson (self.save, self.savepath , 2)
               
               elif buildingname == "copper mine":
                     self.save["copper mine upg cost"] = self.save["copper mine upg cost"] * 5
                     self.data["type"][4]["details"]["output"]["raw copper"] = self.data["type"][4]["details"]["output"]["raw copper"] * 2
                     Json.writejson (self.data, self.path , 2)
                     Json.writejson (self.save, self.savepath , 2)
               
               elif buildingname == "copper foundry":
                     self.save["copper foundry upg cost"] = self.save["copper foundry upg cost"] * 5
                     self.data["type"][5]["details"]["output"]["copper"] = self.data["type"][5]["details"]["output"]["copper"] * 2
                     Json.writejson (self.data, self.path , 2)
                     Json.writejson (self.save, self.savepath , 2)

               elif buildingname == "coal mine":
                     self.save["coal mine upg cost"] = self.save["coal mine upg cost"] * 5
                     self.data["type"][0]["details"]["output"]["coal"] = self.data["type"][0]["details"]["output"]["coal"] * 2
                     Json.writejson (self.data, self.path , 2)
                     Json.writejson (self.save, self.savepath , 2)

               elif buildingname == "steel mill":
                     self.save["steel mill upg cost"] = self.save["steel mill upg cost"] * 5
                     self.data["type"][3]["details"]["output"]["steel"] = self.data["type"][3]["details"]["output"]["steel"] * 2
                     Json.writejson (self.data, self.path , 2)
                     Json.writejson (self.save, self.savepath , 2)
               
               elif buildingname == "rare metal foundry":
                     self.save["rare metals upg cost"] = self.save["rare metals upg cost"] * 5
                     self.data["type"][6]["details"]["output"]["raremetals"] = self.data["type"][6]["details"]["output"]["raremetals"] * 2
                     Json.writejson (self.data, self.path , 2)
                     Json.writejson (self.save, self.savepath , 2)

               elif buildingname == "pumpjack":
                     self.save["pumpjack upg cost"] = self.save["pumpjack upg cost"] * 5
                     self.data["type"][7]["details"]["output"]["oil"] = self.data["type"][7]["details"]["output"]["oil"] * 2
                     Json.writejson (self.data, self.path , 2)
                     Json.writejson (self.save, self.savepath , 2)


         else:
             print("ur too broke")
             time.sleep(2)
   
   def sellrescource (self , rescourcename , amount ):
      if rescourcename == "iron": #differnt prices for different rescources can be added here
         sellprice = 10
      elif rescourcename == "steel":
         sellprice = 25
      elif rescourcename == "copper":
         sellprice = 15
      elif rescourcename == "rare metals" :
         sellprice = 50
      elif rescourcename == "oil":
         sellprice = 100
      else:
         sellprice = 0
      amount = int (amount)
      while True:   
        self.save = Json.loadjson (self.savepath)
        if amount <= self.save [rescourcename]: #checks if the user has enough of a rescource to actually sell the amount they want to, 
           self.save["money"] += (sellprice * amount) #adds the money selling x of the rescouce would give to the save files money value 
           self.money = self.save["money"]  
           self.save [rescourcename] -= amount       #reduces the amount of rescource Y in the save file
           Json.writejson (self.save, self.savepath , 2) #overwrites save file with new values
           load.money = self.money
        else:
             print("you dont have that much to sell")
             time.sleep(2)
        break
      
               
class Load:
   def __init__(self , filepath = "./json/save.json"):
      self.path = Path (filepath)
      self.data = Json.loadjson (self.path)
      self.counter = self.data ["counter"]
      self.money = self.data ["money"]
      self.zone = self.data ["zone"]
      self.rawiron = self.data ["raw iron"]
      self.iron = self.data ["iron"]         
      self.coal = self.data ["coal"]
      self.ironmine = self.data ["iron mine"]
      self.ironfoundry = self.data ["iron foundry"]
      self.coalmine = self.data ["coal mine"]
   
   def moneyupd(self):
     self.money = self.data ["money"]

   def reload(self):
        self.counter = self.data["counter"]
        self.money = self.data["money"]
        self.zone = self.data["zone"]
        self.rawiron = self.data["raw iron"]
        self.iron = self.data["iron"]
        self.coal = self.data["coal"]
        self.ironmine = self.data["iron mine"]
        self.ironfoundry = self.data["iron foundry"]
        self.coalmine = self.data["coal mine"]


class Enemy:
   def __init__(self):
      self.savepath = Path ("./json/save.json")
      self.save = Json.loadjson (self.savepath)

      self.zone = self.save ["zone"]
      self.initialhp = enemycalc.hp(self.zone)
      self.initialattack = enemycalc.attack(self.zone)
      self.initialorg = enemycalc.org(self.zone)         #enemy stats arent calculated with a division template - but rather a set of formula that find a value by substituting the zone value
      self.initialdefense = enemycalc.defense(self.zone)
      self.initialbreakthrough = enemycalc.breakthrough(self.zone)
      self.initialpierce = enemycalc.pierce(self.zone)
      self.initialarmour = enemycalc.armour(self.zone)
      self.initialentrenchment = enemycalc.entrenchment(self.zone)
      self.hp = int(0)
      self.attack = int(0)
      self.org = int(0)
      self.defense = int(0)
      self.breakthrough = int(0)
      self.pierce = int(0)
      self.armour = int(0)
      self.entrenchment = int(0)
   
   def loadinitialstats(self):
      self.save = Json.loadjson(self.savepath)
      if self.save["enemyjustmade"] == 1:
         # recalculate initial stats based on current zone
         self.zone = self.save["zone"]
         self.initialhp = enemycalc.hp(self.zone)
         self.initialattack = enemycalc.attack(self.zone)
         self.initialorg = enemycalc.org(self.zone)
         self.initialdefense = enemycalc.defense(self.zone)
         self.initialbreakthrough = enemycalc.breakthrough(self.zone)
         self.initialpierce = enemycalc.pierce(self.zone)
         self.initialarmour = enemycalc.armour(self.zone)
         self.initialentrenchment = enemycalc.entrenchment(self.zone)
         self.hp = self.initialhp
         self.attack = self.initialattack
         self.org = self.initialorg
         self.defense = self.initialdefense  
         self.breakthrough = self.initialbreakthrough
         self.pierce = self.initialpierce
         self.armour = self.initialarmour
         self.entrenchment = self.initialentrenchment
         self.save["enemyhp"] = self.hp
         self.save["enemyattack"] = self.attack
         self.save["enemyorg"] = self.org
         self.save["enemydefense"] = self.defense
         self.save["enemybreakthrough"] = self.breakthrough
         self.save["enemypierce"] = self.pierce
         self.save["enemyarmour"] = self.armour
         self.save["enemyentrenchment"] = self.entrenchment
         self.save["enemyjustmade"] = 0
         Json.writejson(self.save, self.savepath, 2)
      else:
         self.hp = self.save["enemyhp"]
         self.attack = self.save["enemyattack"]
         self.org = self.save["enemyorg"]
         self.defense = self.save["enemydefense"]
         self.breakthrough = self.save["enemybreakthrough"]
         self.pierce = self.save["enemypierce"]
         self.armour = self.save["enemyarmour"]
         self.entrenchment = self.save["enemyentrenchment"]

   def damagedstats(self):
      self.save = Json.loadjson (self.savepath)
      self.attack , self.defense , self.breakthrough = combat.enemyorgstatchange(self.initialattack , self.initialdefense , self.initialbreakthrough , self.initialorg)
      self.save["enemyattack"] = self.attack
      self.save["enemydefense"] = self.defense
      self.save["enemybreakthrough"] = self.breakthrough
      Json.writejson(self.save , self.savepath , 2)

   def zoneupd(self):
      self.zone = self.save ["zone"]

class Combatdivision(Division):
   def __init__(self):
      super().__init__()
      self.divstat()  # Calculate stats before copying them
      self.savepath = Path ("./json/save.json")
      self.save = Json.loadjson (self.savepath)

      self.initialhp = self.hp
      self.initialattack = self.attack
      self.initialorg = self.org
      self.initialdefense = self.defense
      self.initialbreakthrough = self.breakthrough
      self.initialpierce = self.pierce
      self.initialarmour = self.armour
      self.initialAA = self.AA
      self.initialrecon = self.recon
      self.initialentrenchment = self.entrenchment
      self.dhp = int(0)
      self.dattack = int(0)
      self.dorg = int(0)
      self.ddefense = int(0)
      self.dbreakthrough = int(0)
      self.dpierce = int(0)
      self.darmour = int(0)
      self.dAA = int(0)
      self.drecon = int(0)
      self.dentrenchment = int(0)
   
   def loadinitialstats (self):
      self.save = Json.loadjson (self.savepath)
      if self.save ["divisionjustmade"] == 1:
         self.initialhp = self.hp
         self.initialattack = self.attack
         self.initialorg = self.org
         self.initialdefense = self.defense
         self.initialbreakthrough = self.breakthrough
         self.initialpierce = self.pierce
         self.initialarmour = self.armour
         self.initialAA = self.AA
         self.initialrecon = self.recon
         self.initialentrenchment = self.entrenchment
         self.divstat()
         self.dhp = self.initialhp
         self.dattack = self.initialattack
         self.dorg = self.initialorg
         self.ddefense = self.initialdefense
         self.dbreakthrough = self.initialbreakthrough
         self.dpierce = self.initialpierce
         self.darmour = self.initialarmour
         self.dAA = self.initialAA          #if a division has just been made at the end of last turn - the new divisions initial stats are calculated from the division templates stats - and then these values are updated to the save file
         self.drecon = self.initialrecon
         self.dentrenchment = self.initialentrenchment
         self.save ["divisionhp"] = self.dhp
         self.save ["divisionattack"] = self.dattack
         self.save ["divisionorg"] = self.dorg
         self.save ["divisiondefense"] = self.ddefense
         self.save ["divisionbreakthrough"] = self.dbreakthrough
         self.save ["divisionpierce"] = self.dpierce
         self.save ["divisionarmour"] = self.darmour
         self.save ["divisionrecon"] = self.drecon
         self.save ["divisionAA"] = self.dAA
         self.save ["divisionentrenchment"] = self.dentrenchment
         self.save ["divisionjustmade"] = 0
         Json.writejson (self.save, self.savepath , 2)
      else:
         self.dhp = self.save ["divisionhp"]
         self.dattack = self.save ["divisionattack"]
         self.dorg = self.save ["divisionorg"]
         self.ddefense = self.save ["divisiondefense"]     #if a division wasnt just made , the stats used in calculations are loaded from the save file
         self.dbreakthrough = self.save ["divisionbreakthrough"]    #once the division is damaged - many stats change
         self.dpierce = self.save ["divisionpierce"]
         self.darmour = self.save ["divisionarmour"]
         self.dAA = self.save ["divisionAA"]
         self.drecon = self.save ["divisionrecon"]
         self.dentrenchment = self.save ["divisionentrenchment"]

   def damagedstats(self):
      self.save = Json.loadjson (self.savepath)
      self.dattack , self.ddefense , self.dbreakthrough = combat.orgstatchange(self.initialattack , self.initialdefense , self.initialbreakthrough , self.initialorg)
      self.save["divisionattack"] = self.dattack
      self.save["divisiondefense"] = self.ddefense    #when a division has its organisation damaged - its attack defense and breakthrough are lowered
      self.save["divisionbreakthrough"] = self.dbreakthrough   #they are then saved to the save file - they will be called as the new stat values for the division at the start of the next turn
      Json.writejson(self.save , self.savepath , 2)
      


combatdivision = Combatdivision()
division = Division()
enemy = Enemy()
load = Load()
building = Building()

enemy.loadinitialstats()
combatdivision.loadinitialstats()

repeatmenu = 1
menu = "0"
#main menu loop - where the player selects what to do
#works by using a while loop and an if elif statement - when the menu loop is run through it prints whichever menu corresponds with the menu variable number
#when returning from any menu to the main menu - menu is set to 0 then the while loop re runs , as menu == 0, the main menu is displayed
while repeatmenu == 1:
   if menu == "0":
      os.system('cls' if os.name == 'nt' else 'clear')  #this line clears the console - arguably the most important feature of the entire program
      combatdivision.loadinitialstats()
      enemy.loadinitialstats()
      load.reload()
      rescource = Json.loadjson(Path("./json/save.json"))
      print("////////////////////////------main menu------////////////////////////")
      print(f"\n1 : build/upgrade structures      current money = {rescource["money"]}")
      print(f"2 : rescource interactions        coal = {rescource["coal"]} , raw iron = {rescource["raw iron"]} , raw copper = {rescource["raw copper"]} , oil = {rescource["oil"]}")
      print(f"3:  division designer             iron = {rescource["iron"]} , copper = {rescource["copper"]} , steel = {rescource["steel"]} , rare metals = {rescource["rare metals"]}")
      print("4 : end turn                      current turn = ", rescource["counter"]) 
      print("5 : tutorial")
      print("6 : exit")
      print("\n\n/////////////////////------Battle Overview------/////////////////////")
      print(f"\nyou are on zone {enemy.zone}")
      print("\nyour division:                                  enemy division:")
      print(f"  {combatdivision.dhp} hp                                              {enemy.hp} hp")
      print(f"  {combatdivision.dorg} org                                             {enemy.org} org")
      print(f"  {combatdivision.dattack} attack                                          {enemy.attack} attack")
      print(f"  {combatdivision.ddefense} defense                                         {enemy.defense} defense")
      print(f"  {combatdivision.dbreakthrough} breakthrough                                    {enemy.breakthrough} breakthrough")
      print(f"  {combatdivision.dpierce} pierce                                          {enemy.pierce} pierce")
      print(f"  {combatdivision.darmour} armour                                          {enemy.armour} armour")
      print(f"  {combatdivision.dAA} AA")
      print(f"  {combatdivision.drecon} recon")
      print(f"  {combatdivision.dentrenchment} entrenchment                                    {enemy.entrenchment} entrenchment")
      menu = input ("\nselect menu: ")
      
   elif menu == "1":
      while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("building interactions:")
        print("\n1 : buy building")
        print("2 : upgrade buildings")
        print("3 : return")
        submenu = input ("\nselect menu: ")
        if submenu == "1":
           while True:
             os.system('cls' if os.name == 'nt' else 'clear')
             build = Json.loadjson(Path("./json/building.json"))
             count = Json.loadjson(Path("./json/save.json"))
             #these lines state a building, amount owned, production rate and needs - only prints buildings like copper mines if unlocked
             #this couldve been much easier on the eyes if i understood OOP better at the time - i am NOT changing it 
             print(f"current money: {count["money"]}\n")
             print(f"coal mine:  {count["coal mine"]} owned , {build["type"][0]["details"]["output"]["coal"]} coal/turn,   {build["type"][0]["details"]["cost"]} cost")    
             print(f"iron mine: {count["iron mine"]} owned , {build["type"][1]["details"]["output"]["raw iron"]} raw iron/turn,   {build["type"][1]["details"]["cost"]} cost")
             if count["copperunlock"] == 1:
                print(f"copper mine: {count["copper mine"]} owned , {build["type"][4]["details"]["output"]["raw copper"]} raw copper/turn,   {build["type"][4]["details"]["cost"]} cost")
             print(f"iron foundry: {count["iron foundry"]} owned , {build["type"][2]["details"]["output"]["iron"]} iron/turn, uses {build["type"][2]["details"]["input"]["coal"]} coal and {build["type"][2]["details"]["input"]["raw iron"]} raw iron/turn,   {build["type"][2]["details"]["cost"]} cost")
             if count["copperunlock"] == 1:
                  print(f"copper foundry: {count["copper foundry"]} owned , {build["type"][5]["details"]["output"]["copper"]} copper/turn, uses {build["type"][5]["details"]["input"]["coal"]} coal and {build["type"][5]["details"]["input"]["raw copper"]} raw copper/turn,   {build["type"][5]["details"]["cost"]} cost")
             print(f"steel mill: {count["steel mill"]} owned , {build["type"][3]["details"]["output"]["steel"]} steel/turn, uses {build["type"][3]["details"]["input"]["coal"]} coal and {build["type"][3]["details"]["input"]["iron"]} iron/turn,   {build["type"][3]["details"]["cost"]} cost")
             if count["raremetalsunlock"] == 1:
                print(f"rare metal foundry: {count["rare metal foundry"]} owned , {build["type"][6]["details"]["output"]["raremetals"]} rare metals/turn, uses {build["type"][6]["details"]["input"]["coal"]} coal {build["type"][6]["details"]["cost"]} cost")
             if count["oilunlock"] == 1:
                print(f"pumpjack: {count["pumpjack"]} owned , {build["type"][7]["details"]["output"]["oil"]} oil/turn, uses {build["type"][7]["details"]["input"]["coal"]} coal,   {build["type"][7]["details"]["cost"]} cost")
             buy = input ("\npurchase ('exit' to leave): ")      
             if buy == "exit":
                break
             elif buy == "coal mine" or buy == "iron mine" or buy == "iron foundry" or buy == "steel mill" or buy == "copper mine" or buy == "copper foundry" or buy == "rare metal foundry" or buy == "pumpjack":
                building.buybuilding(buy)
             else:
                print("invalid building")
                time.sleep(2)

        elif submenu == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
              os.system('cls' if os.name == 'nt' else 'clear')
              build = Json.loadjson (Path("./json/building.json"))
              save = Json.loadjson (Path("./json/save.json"))
              print(f"\ncurrent money: {save["money"]}\n")
              print(f"coal mine  :  {save["coal mine upg cost"]}")
              print(f"iron mine  :  {save["iron mine upg cost"]}")
              if save ["copperunlock"] == 1:
                 print(f"copper mine  :  {save["copper mine upg cost"]}")
              print(f"\niron foundry  :  {save["iron foundry upg cost"]}")     
              if save ["copperunlock"] == 1:
                 print(f"copper foundry  :  {save["copper foundry upg cost"]}")                       
              print(f"steel mill  :  {save["steel mill upg cost"]}")
              if save ["raremetalsunlock"] == 1:
                 print(f"rare metal foundry  :  {save["rare metals upg cost"]}")
              if save ["oilunlock"] == 1:
                 print(f"pumpjack  :  {save["pumpjack upg cost"]}")
              buy = input("\nchoose which to upgrade ('upgrades double output, 5x cost for upgrade')  ")

              if buy == "coal mine" or buy == "iron mine" or buy == "iron foundry" or buy == "steel mill" or buy == "copper mine" or buy == "copper foundry" or buy == "rare metal foundry" or buy == "pumpjack":
                if buy == "coal mine" :
                   change = "coal mine upg cost"
                elif buy == "iron mine":
                   change = "iron mine upg cost"
                elif buy == "iron foundry":
                   change = "iron foundry upg cost"
                elif buy == "steel mill":
                   change = "steel mill upg cost"
                elif buy == "copper mine":
                   change = "copper mine upg cost"
                elif buy == "copper foundry":
                   change = "copper foundry upg cost"
                elif buy == "rare metal foundry":
                   change = "rare metals upg cost"
                elif buy == "pumpjack":
                   change = "pumpjack upg cost"
                
                building.upgradebuilding(buy , change)

              elif buy == "exit":
                    break
              else:
                   print("invalid building")
                   time.sleep(2)

        elif submenu == "3":
            menu = "0"
            break
        
   elif menu == "2":
        while True:
          os.system('cls' if os.name == 'nt' else 'clear')
          print("rescource interactions:")
          print("\n1 : sell rescources (coal and ore cant be sold)")
          print("2 : return")
          submenu = input ("\nselect menu: ")
          if submenu == "1":
            while True:
               os.system('cls' if os.name == 'nt' else 'clear')
               count = Json.loadjson ("./json/save.json")
               print(f"current money: {count["money"]}\n")
               print(f"iron: {count['iron']} owned  - for 10 money")
               if count["copperunlock"] == 1:
                 print(f"copper: {count['copper']} owned  - for 15 money")
               print(f"steel: {count['steel']} owned  - for 25 money")
               if count["raremetalsunlock"] == 1:
                 print(f"rare metals: {count['rare metals']} owned  - for 50 money")
               if count["oilunlock"] == 1:
                 print(f"oil: {count['oil']} owned  - for 100 money")
               sell = input ("\nsell ('exit' to leave): ")
               if sell == "exit":
                  break
               elif sell == "iron" or sell == "steel" or sell == "copper" or sell == "rare metals"  or sell == "oil": #or sell == blah blah blah
                  amount = input ("amount to sell: ")
                  x = amount.isnumeric()
                  if x == True:
                    amount = int(amount)
                    if amount >= 0: 
                        building.sellrescource(sell, amount)
                    else:
                        print("enter a number above 0")
                        time.sleep(2)
                  else:
                     print("input a number")
                     time.sleep(2)
               else:
                  print("invalid rescource")
                  time.sleep(2)
          elif submenu == "2":
              menu = "0"
              break

   elif menu == "3":
      while True:
         division.reload()
         os.system('cls' if os.name == 'nt' else 'clear')
         division.divstat()   
         print("division designer:")
         print("\n   1      2      3      4")
         print(f"a[ {division.a1}  ,  {division.a2}  ,  {division.a3}  ,  {division.a4} ]     {division.hp} hp,              {division.attack} attack,          {division.armour} armour,")
         print(f"b[ {division.b1}  ,  {division.b2}  ,  {division.b3}  ,  {division.b4} ]     {division.org} org,             {division.breakthrough} breakthrough,    {division.AA} AA,")
         print(f"c[ {division.c1}  ,  {division.c2}  ,  {division.c3}  ,  {division.c4} ]     {division.defense} defense,         {division.pierce} pierce,        {division.recon} recon,")
         print(f"d[ {division.d1}  ,  {division.d2}  ,  {division.d3}  ,  {division.d4} ]     {division.entrenchment} entrenchment,")
         print("\nkey: tank = Ta, IFV = IV, infantry = In, arty = Ar, Anti air = AA, Anti tank = AT   blank = --")
         print("\ncosts: \n  cost = ", division.cost, "  \n  steel = ", division.steel, " \n  copper = ", division.copper, " \n  rare metals = ", division.rare, " \n  oil = ", division.oil)

         print("\n1 : edit template")
         print("2 : view stats (shows stats for all battalions of a given stat)")
         print("3 : view costs (shows costs for all battalions)")
         print("4 : upgrade battalions")
         print("5 : return")
         submenu = input ("\nselect menu: ")
         if submenu == "5":
            menu = "0"
            break
         if submenu == "1":
            edit = input("select tile to edit (e.g. a1): ")
            if edit == "exit":
               pass
            elif edit == "a1" or edit == "a2" or edit == "a3" or edit == "a4" or edit == "b1" or edit == "b2" or edit == "b3" or edit == "b4" or edit == "c1" or edit == "c2" or edit == "c3" or edit == "c4" or edit == "d1" or edit == "d2" or edit == "d3" or edit == "d4":
               batt = input("choose battalion to replace with):  (Ta/IV/In/Ar/AA/AT/--) ")
               if batt == "Ta" or batt == "IV" or batt == "In" or batt == "Ar" or batt == "AA" or batt == "AT" or batt == "--":
                  function.divchange(edit, batt)
               else: 
                  print("invalid battalion")
                  time.sleep(2)
            else:
               print("invalid tile")
               time.sleep(2)

         if submenu == "2":
            while True:
               os.system('cls' if os.name == 'nt' else 'clear')
               division.statcheck()
               exit = input("type anything to return: ")
               break

         
         if submenu == "3":
            while True:
               os.system('cls' if os.name == 'nt' else 'clear')
               division.costcheck()
               exit = input("type anything to return: ")
               break
         
         if submenu == "4":
            while True:
               os.system('cls' if os.name == 'nt' else 'clear')
               save = Json.loadjson ("./json/save.json")
               if save ["infCW"] == 1 and save ["Infera"] == "WW2":
                  print(f"upgrade infantry to CW {save["infCWp"]} cost")
               if save ["infmodern"] == 1 and save ["Infera"] == "CW":
                  print(f"upgrade infantry to modern {save["infmodernp"]} cost") # repeat this a bit
               if save ["IFVCW"] == 1 and save ["IFVera"] == "WW2":
                  print(f"upgrade IFV to CW {save["IFVCWp"]} cost")
               if save ["IFVmodern"] == 1 and save ["IFVera"] == "CW":
                  print(f"upgrade IFV to modern {save["IVFmodernp"]} cost")
               if save ["tankCW"] == 1 and save ["tankera"] == "WW2":
                  print(f"upgrade tank to CW {save["tankCWp"]} cost")
               if save ["tankmodern"] == 1 and save ["tankera"] == "CW":
                  print(f"upgrade tank to modern {save["tankmodernp"]} cost")
               if save ["artilleryCW"] == 1 and save ["artera"] == "WW2":
                  print(f"upgrade artillery to CW {save["artilleryCWp"]} cost")
               if save ["artillerymodern"] == 1 and save ["artera"] == "CW":
                  print(f"upgrade artillery to modern {save["artillerymodernp"]} cost")
               if save ["AACW"] == 1 and save ["AAera"] == "WW2":
                  print(f"upgrade AA to CW {save["AACWp"]} cost")
               if save ["AAmodern"] == 1 and save ["AAera"] == "CW":
                  print(f"upgrade AA to modern {save["AAmodernp"]} cost")
               if save ["ATCW"] == 1 and save ["ATera"] == "WW2":
                  print(f"upgrade AT to CW {save["ATCWp"]} cost")
               if save ["ATmodern"] == 1 and save ["ATera"] == "CW":
                  print(f"upgrade AT to modern {save["ATmodernp"]} cost")

               unit = input("\n choose which to upgrade , exit to leave : ")

               if unit == "exit":
                  break
               elif unit == "infantry" or unit == "IFV" or unit == "tank" or unit == "artillery" or unit == "AA" or unit == "AT":
                  division.upgrade(unit)
               else:
                  print("invalid unit")
                  time.sleep(2)

      menu = "0"

            
   elif menu == "4":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("ending turn...")
      load.counter = endturn.buh(load.counter)
      endturn.rescource (load.iron, load.rawiron, load.coal, load.ironmine, load.ironfoundry, load.coalmine)
      time.sleep(3)

      savepath = Path ("./json/save.json")
      save =Json.loadjson (savepath)
      if save ["divisionmade"] ==  1:
        combat.divfight(combatdivision.dattack , combatdivision.dbreakthrough , combatdivision.dpierce , combatdivision.drecon , combatdivision.dentrenchment , enemy.hp , enemy.org  , enemy.defense  , enemy.armour , enemy.entrenchment)
        combat.enemyfight(enemy.attack , enemy.breakthrough , enemy.pierce  , enemy.entrenchment, combatdivision.dhp ,combatdivision.dorg  , combatdivision.ddefense ,  combatdivision.darmour, combatdivision.drecon , combatdivision.dentrenchment)
        
        combatdivision.damagedstats()   #after combat happens, the new hp and org of both is saved and overwrites the old values , the new damage defense and breakthrough values based on org loss are found and then too overwrites these over the old values for those stats
        enemy.damagedstats()
      time.sleep(3)
      enemy.zoneupd()
      endturn.unlock()
      # Automatically load a new enemy if needed
      save = Json.loadjson(Path("./json/save.json"))
      if save.get("enemyjustmade", 0) == 1:
         enemy.loadinitialstats()
        
      division.reload()
      division.divstat()
      endturn.divcreate(division.cost , division.steel , division.copper , division.rare , division.oil)
      load.reload()
      menu = "0"  

   elif menu == "5":
      while True:
         os.system('cls' if os.name == 'nt' else 'clear')
         print("you start with 1000 money , 1 iron mine, coal mine and iron foundry")
         print("you can use money to buy buildings to make rescources, to upgrade your units and to upgrade buildings - unit upgrades appear at zone 15")
         print("iron ore and copper ore are used to make iron and copper  -  coal and iron makes steel  -  steel, oil , copper and rare metals make your division")
         print("coal is also used to power buildings")
         print("rescources can also be sold for money")
         print("\nyou start with a weak divsision which can fight the enemy")
         print("victory move you forwards a zone and progress earns money and unlocks unit upgrades")
         print("the division designer is used to edit the division that you send to fight - stronger divisions are more expensive - keep that in mind")
         print("you will always attack before the enemy - sending waves of men and steel will eventually let you win")
         print("more attack, breakthrough and (armour) piercing = more damage dealt - more defense and armour = less damage taken")
         print("entrenchment gives a 1% bonus to attack and defense - recon reduces the effectiveness of entrenchment (the enemies dont have that one :face_holding_back_tears:)")
         print("you deal a little amount of hp damage and org damage to the enemy - but reducing an enemies organisation will reduce their attack , defense and breakthrough")
         print("AA actually stands for A(wesome)A(s hell) - not anti air! any reference to anti air is a mistranslation and it was never ever originally planned for the game")
         print("\nall menus that require typing are case sensitive and whatever")
         print("when a message saying your division has died - your division wont seem dead in the menu - but no combat turns will happen until a division is made again")
         print("if you want to return from a menu and no way is specified just type exit and it should work")

         choice = input("\nleave gng : ")
         if choice == "exit":
            menu = "0"
            break
         else:
            print("read the last bit")



   elif menu == "6":
      print("exiting and saving...")
      # add save function here???
      time.sleep(3)
      repeatmenu = "0"
    
   else:
     print("invalid menu")
     time.sleep(2)
     menu = "0"

      
        
    

