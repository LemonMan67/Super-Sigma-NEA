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
         self.hp = statcalc.hp(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera)
         self.attack = statcalc.attack(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera)
         self.org = statcalc.org(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera)
         self.defense = statcalc.defense(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera)
         self.breakthrough = statcalc.breakthrough(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera)
         self.pierce = statcalc.pierce(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera)
         self.armour = statcalc.armour(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera)
         self.AA = statcalc.AA(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera)
         self.recon = statcalc.recon(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera)
         self.entrenchment = statcalc.entrenchment(self.divlist, self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera)


class Battalion:
    def __init__(self, filepath = "./json/battalion.json"):
        self.path = Path (filepath)  
        self.data = Json.loadjson (self.path)
        self.savepath = Path ("./json/save.json")
        self.save = Json.loadjson (self.savepath)
        self.tankera = self.save ["tankera"]
        self.IFVera = self.save ["IFVera"]
        self.Infera = self.save ["Infera"]
        self.artera = self.save ["artera"]
        self.AAera = self.save ["AAera"]
        self.ATera = self.save ["ATera"]
        self.sortlist = [self.tankera, self.IFVera, self.Infera, self.artera, self.AAera, self.ATera]
        self.passthrough = int(-1)

    def Statcheck (self):
        repeat = 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nwhich stat do you want to check? (hp, attack, org, defense, breakthrough, pierce, armour, AA, recon, entrenchment) or type stop to exit: ")
        stat = input ("\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        while repeat == 1:
          self.passthrough = int(-1)
          if stat == "stop":
            repeat = 0
          elif stat == "hp" or stat == "attack" or stat == "org" or stat == "defense" or stat == "breakthrough" or stat == "pierce" or stat == "armour" or stat == "AA" or stat == "recon" or stat == "entrenchment":
            print("for", stat ,":")
            for x in self.data ["battalion"]:
              self.passthrough += 1
              print (f" Unit:  {x['unit']} ")
              for y in x ["list"]:
                check = y["era"]["type"]
                check = str(check)                                 #this function sorts through the json batallion file to return the required stat for each unit
                listcheck = str(self.sortlist[self.passthrough])
                if check == listcheck:  
                  print (f"  has { y["era"][stat]} {stat}   ( {y["era"]["type"]} )")
            stat = input ("\nwhich stat do you want to check? (hp, attack, org, defense, breakthrough, pierce, armour, AA, recon, entrenchment) or type stop to exit: ")
          else:
            print("invalid stat")
            stat = input ("\nwhich stat do you want to check? (hp, attack, org, defense, breakthrough, pierce, armour, AA, recon, entrenchment) or type stop to exit: ")

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
      self.iron = self.data ["iron"]         # the difference in rescources is correctly figured, but the values arent properly updated and the amount owned is seemingly the amount of change every turn, this is likely to be an issue with how values are loaded, thus a possible redesign of how i do this may be in order
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
battalion = Battalion()
building = Building()
division = Division()


repeatmenu = 1
menu = "0"

#main menu loop - where the player selects what to do

while repeatmenu == 1:
   if menu == "0":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("main menu:")
      print("\n1 : battalion interactions")
      print("2 : build/upgrade structures      current money = ", load.money)
      print("3 : rescource interactions")
      print("4:  division designer")
      print("5 : end turn                      current turn = ", load.counter) 
      print("6 : exit")
      menu = input ("\nselect menu: ")
      
   elif menu == "1":
      while True:
         os.system('cls' if os.name == 'nt' else 'clear')
         print("battalion interactions:")
         print("\n1 : stat check")
         print("2 : return")
         submenu = input ("\nselect menu: ")
         if submenu == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            battalion.Statcheck()
         elif submenu == "2":
            menu = "0"
            break
         else:
            print("invalid menu")
            time.sleep(2)

   elif menu == "2":
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
             buy = input ("\npurchase ('exit' to leave): ")      
             if buy == "exit":
                break
             elif buy == "coal mine" or buy == "iron mine" or buy == "iron foundry" or buy == "steel mill" or buy == "copper mine" or buy == "copper foundry":
                building.buybuilding(buy)
             else:
                print("invalid building")
                time.sleep(2)
        elif submenu == "2":
            menu = "0"
            break
        
   elif menu == "3":
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

   elif menu == "4":
      while True:
         division.reload()
         os.system('cls' if os.name == 'nt' else 'clear')
         division.divstat()   
         print("division designer:")
         print("\n   1     2     3     4")
         print(f"a[ {division.a1}  ,  {division.a2}  ,  {division.a3}  ,  {division.a4} ]     {division.hp} hp,              {division.attack} attack,          {division.armour} armour,")
         print(f"b[ {division.b1}  ,  {division.b2}  ,  {division.b3}  ,  {division.b4} ]     {division.org} org,             {division.breakthrough} breakthrough,    {division.AA} AA,")
         print(f"c[ {division.c1}  ,  {division.c2}  ,  {division.c3}  ,  {division.c4} ]     {division.defense} defense,         {division.pierce} pierce,          {division.recon} recon,")
         print(f"d[ {division.d1}  ,  {division.d2}  ,  {division.d3}  ,  {division.d4} ]     {division.entrenchment} entrenchment,")
         print("\nkey: tank = Ta, IFV = IV, infantry = In, arty = Ar, Anti air = AA, Anti tank = AT   blank = --")

         print("\n1 : return")
         print("2 : edit template")
         submenu = input ("\nselect menu: ")
         if submenu == "1":
            menu = "0"
            break
         if submenu == "2":
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
            
      menu = "0"

            
   elif menu == "5":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("ending turn...")
      load.counter = endturn.buh(load.counter)
      endturn.rescource (load.iron, load.rawiron, load.coal, load.ironmine, load.ironfoundry, load.coalmine)
      time.sleep(4)
      endturn.unlock()
      menu = "0"  

   elif menu == "6":
      print("exiting and saving...")
      # add save function here???
      time.sleep(3)
      repeatmenu = "0"
    
   else:
     print("invalid menu")
     time.sleep(2)
     menu = "0"

 
 #when adding new rescources, edit all appearances of rescource in code, so endturn.rescouce , sellrescource, and rescource interactions
      
        
    
