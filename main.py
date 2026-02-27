from pathlib import Path
import time
import os
from Process import endturn
from Process import Json

#change values in battlalion json file

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
          if stat == "stop":
            repeat = 0
          elif stat == "hp" or stat == "attack" or stat == "org" or stat == "defense" or stat == "breakthrough" or stat == "pierce" or stat == "armour" or stat == "AA" or stat == "recon" or stat == "entrenchment":
            print("for", stat ,":")
            for x in self.data ["battalion"]:
              self.passthrough += 1
              print (f" Unit:  {x['unit']} ")
              for y in x ["list"]:
                check = y["era"]["type"]
                check = str(check)
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
      if buildingname != "iron mine" or buildingname != "iron foundry" or buildingname != "coal mine":
       for x in self.data ["type"]:
          if x ["details"]["building"] == buildingname :
             if self.money >=  int ( x ["details"]["cost"]):
               self.money -= int ( x ["details"]["cost"])
               load.money = self.money
               amount = self.save [buildingname]
               amount += 1         #make way to print the correct value in the building menu
               self.save [buildingname] = amount
               self.save ["money"] = self.money
               Json.writejson (self.save, self.savepath , 2)
               if buildingname == "iron mine":        
                     load.ironmine += 1
               elif buildingname == "iron foundry":         #must add more lines here to actually increase the building count for a specific building
                      load.ironfoundry += 1
               elif buildingname == "coal mine":
                      load.coalmine += 1
      else:
        print("invalid building name")
        time.sleep(2)

               
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

load = Load()
battalion = Battalion()
building = Building()


repeatmenu = 1
menu = "0"


while repeatmenu == 1:
   if menu == "0":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("main menu:")
      print("\n1 : battalion interactions")
      print("2 : build/upgrade structures      current money = ", load.money)
      print("3 : end turn       current turn = ", load.counter) 
      print("4 : exit")
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
           os.system('cls' if os.name == 'nt' else 'clear')
           build = Json.loadjson ("./json/building.json")
           count = Json.loadjson ("./json/save.json")
           print(f"coal mine:  {count["coal mine"]} owned , {build["type"][0]["output"]["coal"]} coal/sec, {build["type"][0]["cost"]} cost")    # here we need to add cost of building and amount owned and production rate
           print(f"iron mine: {count["iron mine"]} owned , {build["type"][1]["output"]["raw iron"]} raw iron/sec, {build["type"][1]["cost"]} cost")
           print(f"iron foundry: {count["coal mine"]} owned , {build["type"][2]["output"]["iron"]} iron/sec, this uses {build["type"][2][input]["coal"]} coal and {build["type"][2][input]["raw iron"]} raw iron/sec {build["type"][0]["cost"]} cost")
           buy = input ("\npurchase : ")        #completely remake this menu
           building.buybuilding (buy)
           menu = "0"

      
            
   elif menu == "3":
      os.system('cls' if os.name == 'nt' else 'clear')
      print(load.iron, load.rawiron, load.coal)
      print("ending turn...")
      load.counter = endturn.buh(load.counter)
      endturn.rescource (load.iron, load.rawiron, load.coal, load.ironmine, load.ironfoundry, load.coalmine)
      print(load.iron, load.rawiron, load.coal)
      time.sleep(5)
      menu = "0"  

   elif menu == "4":
      print("exiting and saving...")
      # add save function here???
      time.sleep(3)
      repeatmenu = "0"
    
   else:
     print("invalid menu")
     time.sleep(2)
     menu = "0"

 
    
      
        
    
