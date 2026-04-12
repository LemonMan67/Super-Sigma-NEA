from pathlib import Path
import time
import os
from Process import endturn
from Process import Json
from Process import function
from Process import statcalc 

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
         elif era == "CW":
            return 1
         elif era == "modern":
            return 0

      def statcheck(self):
         counter = 0
         batlist = [self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera]
         for x in self.bat["battalion"]:

            print (f" Unit:  {x['unit']}")
            for y in x ["list"]:
                if batlist[counter] == y["era"]["type"]:
                  print (f"  is from the {y['era']['type']} era")
                  print (f"  has { y["era"]["hp"]} hp")
                  print (f"  has { y["era"]["org"]} org")
                  print (f"  has { y["era"]["attack"]} attack")
                  print (f"  has { y["era"]["defense"]} defense")
                  print (f"  has { y["era"]["breakthrough"]} breakthrough")
                  print (f"  has { y["era"]["pierce"]} pierce")
                  print (f"  has { y["era"]["armour"]} armour")
                  print (f"  has { y["era"]["AA"]} AA")
                  print (f"  has { y["era"]["recon"]} recon")
                  print (f"  has { y["era"]["entrenchment"]} entrenchment")
                  print (f"  needs { y["era"]["amount"]} units/battalion\n")
            counter += 1

      def costcheck(self):
         counter = 0
         batlist = [self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera]
         for x in self.batc["battalion"]:
            print (f" Unit:  {x['unit']}")
            for y in x ["list"]:
                if batlist[counter] == y["era"]["type"]:
                  print (f"  is from the {y['era']['type']} era")
                  print (f"  costs { y["era"]["cost"]} money")
                  print (f"  costs { y["era"]["steel"]} steel")
                  print (f"  costs { y["era"]["copper"]} copper")
                  print (f"  costs { y["era"]["rare metals"]} rare metals")
                  print (f"  costs { y["era"]["oil"]} oil\n")
                  print ("amount / unit made - amount of units/battalion is in statcheck")
         counter += 1

class Building:
   def __init__(self , filepath = "./json/building.json"):
      self.path = Path (filepath)
      self.data = Json.loadjson (self.path)
      self.savepath = Path ("./json/save.json")
      self.save = Json.loadjson (self.savepath)
      self.money = load.money

   def buybuilding (self , buildingname ) :
      if buildingname != "iron mine" or buildingname != "iron foundry" or buildingname != "coal mine" or buildingname != "steel mill" or buildingname != "copper mine" or buildingname != "copper foundry":
       for x in self.data ["type"]:
          if x ["details"]["building"] == buildingname :
             if self.money >=  int ( x ["details"]["cost"]):
               self.money -= int ( x ["details"]["cost"])
               load.money = self.money
               amount = self.save [buildingname]
               amount += 1        
               self.save [buildingname] = amount
               self.save ["money"] = self.money
               Json.writejson (self.save, self.savepath , 2)
               if buildingname == "iron mine":        
                     self.save["iron mine"] += 1
                     cost = self.data["type"][1]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][1]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)

               elif buildingname == "iron foundry":         
                      self.save["iron foundry"] += 1
                      cost = self.data["type"][2]["details"]["cost"]
                      cost = int(cost)
                      cost = cost * 1.3
                      cost = round(cost,1)
                      self.data["type"][2]["details"]["cost"] = cost
                      Json.writejson (self.data, self.path , 2)
               
               elif buildingname == "copper mine":
                     self.save["copper mine"] += 1
                     cost = self.data["type"][4]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][4]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)
               
               elif buildingname == "copper foundry":
                     self.save["copper foundry"] += 1
                     cost = self.data["type"][5]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][5]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)

               elif buildingname == "coal mine":
                      self.save["coal mine"] += 1
                      cost = self.data["type"][0]["details"]["cost"]
                      cost = int(cost)
                      cost = cost * 1.3
                      cost = round(cost,1)
                      self.data["type"][0]["details"]["cost"] = cost
                      Json.writejson (self.data, self.path , 2)

               elif buildingname == "steel mill":
                     self.save["steel mill"] += 1
                     cost = self.data["type"][3]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][3]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)
               
               elif buildingname == "rare metal foundry":
                     self.save["rare metal foundry"] += 1
                     cost = self.data["type"][6]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][6]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)

               elif buildingname == "pumpjack":
                     self.save["pumpjack"] += 1
                     cost = self.data["type"][7]["details"]["cost"]
                     cost = int(cost)
                     cost = cost * 1.3
                     cost = round(cost,1)
                     self.data["type"][7]["details"]["cost"] = cost
                     Json.writejson (self.data, self.path , 2)

      else:
        print("invalid building name")
        time.sleep(2)
   
   def sellrescource (self , rescourcename , amount ):
      if rescourcename == "iron": #differnt prices for different rescources can be added here
         sellprice = 2
      if rescourcename == "steel":
         sellprice = 5
      if rescourcename == "copper":
         sellprice = 3
      if rescourcename == "rare metals":
         sellprice = 15
      if rescourcename == "oil":
         sellprice = 25
      else:
         sellprice = 0
      amount = int (amount)
      print(rescourcename, amount, sellprice)
      cont = input("test")
      while True:   
        if amount <= self.save [rescourcename]: 
           self.money += sellprice * amount
           self.save [rescourcename] -= amount
           self.save ["money"] = self.money
           Json.writejson (self.save, self.savepath , 2)
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
      self.rawiron = self.data ["raw iron"]
      self.iron = self.data ["iron"]         #this does literally nothing
      self.coal = self.data ["coal"]
      self.ironmine = self.data ["iron mine"]
      self.ironfoundry = self.data ["iron foundry"]
      self.coalmine = self.data ["coal mine"]

class Enemy:
   def __init__(self):
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

enemy = Enemy()
load = Load()
building = Building()
division = Division()


repeatmenu = 1
menu = "0"

#main menu loop - where the player selects what to do

while repeatmenu == 1:
   if menu == "0":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("main menu:")
      print("\n1 : build/upgrade structures      current money = ", load.money)
      print("2 : rescource interactions")
      print("3:  division designer")
      print("4 : end turn                      current turn = ", load.counter) 
      print("5 : exit")
      menu = input ("\nselect menu: ")
      
   elif menu == "1":
      while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("building interactions:")
        print("\n1 : buy building")
        print("2 : return")
        submenu = input ("\nselect menu: ")
        if submenu == "1":
           while True:
             os.system('cls' if os.name == 'nt' else 'clear')
             build = Json.loadjson ("./json/building.json")
             count = Json.loadjson ("./json/save.json")
             #these lines state a building, amount owned, production rate and needs - only prints buildings like copper mines if unlocked
             print(f"current money: {load.money}\n")
             print(f"coal mine:  {count["coal mine"]} owned , {build["type"][0]["details"]["output"]["coal"]} coal/turn,   {build["type"][0]["details"]["cost"]} cost")    
             print(f"iron mine: {count["iron mine"]} owned , {build["type"][1]["details"]["output"]["raw iron"]} raw iron/turn,   {build["type"][1]["details"]["cost"]} cost")
             if count["copperunlock"] == 1:
                print(f"copper mine: {count["copper mine"]} owned , {build["type"][4]["details"]["output"]["raw copper"]} copper/turn,   {build["type"][4]["details"]["cost"]} cost")
             print(f"iron foundry: {count["iron foundry"]} owned , {build["type"][2]["details"]["output"]["iron"]} iron/turn, uses {build["type"][2]["details"]["input"]["coal"]} coal and {build["type"][2]["details"]["input"]["raw iron"]} raw iron/turn,   {build["type"][2]["details"]["cost"]} cost")
             if count["copperunlock"] == 1:
                  print(f"copper foundry: {count["copper foundry"]} owned , {build["type"][5]["details"]["output"]["copper"]} copper/turn, uses {build["type"][5]["details"]["input"]["coal"]} coal and {build["type"][5]["details"]["input"]["raw copper"]} raw copper/turn,   {build["type"][5]["details"]["cost"]} cost")
             print(f"steel mill: {count["steel mill"]} owned , {build["type"][3]["details"]["output"]["steel"]} steel/turn, uses {build["type"][3]["details"]["input"]["coal"]} coal and {build["type"][3]["details"]["input"]["iron"]} iron/turn,   {build["type"][3]["details"]["cost"]} cost")
             if count["raremetalsunlock"] == 1:
                print(f"rare metal foundry: {count["rare metal foundry"]} owned , {build["type"][6]["details"]["output"]["rare metals"]} rare metals/turn, uses {build["type"][6]["details"]["input"]["coal"]} coal {build["type"][6]["details"]["cost"]} cost")
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
               print(f"current money: {load.money}\n")
               print(f"iron: {count['iron']} owned")
               if count["copperunlock"] == 1:
                 print(f"copper: {count['copper']} owned")
               print(f"steel: {count['steel']} owned")
               if count["raremetalsunlock"] == 1:
                 print(f"rare metals: {count['rare metals']} owned")
               if count["oilunlock"] == 1:
                 print(f"oil: {count['oil']} owned")
               sell = input ("\nsell ('exit' to leave): ")
               if sell == "exit":
                  break
               elif sell == "iron" or sell == "steel" or sell == "copper": #or sell == blah blah blah
                  amount = input ("amount to sell: ")
                  building.sellrescource(sell, amount)
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
         print("4 : return")
         submenu = input ("\nselect menu: ")
         if submenu == "4":
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
   
      menu = "0"

            
   elif menu == "4":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("ending turn...")
      load.counter = endturn.buh(load.counter)
      endturn.rescource (load.iron, load.rawiron, load.coal, load.ironmine, load.ironfoundry, load.coalmine)
      time.sleep(4)
      endturn.unlock()
      endturn.divcreate(division.cost , division.steel , division.copper , division.rare , division.oil)
      
      menu = "0"  

   elif menu == "5":
      print("exiting and saving...")
      # add save function here???
      time.sleep(3)
      repeatmenu = "0"
    
   else:
     print("invalid menu")
     time.sleep(2)
     menu = "0"

 #when adding new rescources, edit all appearances of rescource in code, so endturn.rescouce , sellrescource, and rescource interactions
      
        
    
