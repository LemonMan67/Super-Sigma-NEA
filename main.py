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
        self.passthrough = -1

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
                print ([self.sortlist[self.passthrough]])
                if check == [self.sortlist[self.passthrough]]:    #make this check pass, correct value passed, but the value has extra characters making it not equal
                  print (f"  { y["era"]["type"] } has { y["era"][stat]} {stat} ")
            stat = input ("\nwhich stat do you want to check? (hp, attack, org, defense, breakthrough, pierce, armour, AA, recon, entrenchment) or type stop to exit: ")
          else:
            print("invalid stat")
            stat = input ("\nwhich stat do you want to check? (hp, attack, org, defense, breakthrough, pierce, armour, AA, recon, entrenchment) or type stop to exit: ")

class Load:
   def __init__(self , filepath = "./json/save.json"):
      self.path = Path (filepath)
      self.data = Json.loadjson (self.path)

   def saveload (self) :
      global counter
      counter =   self.data ["counter"]
      

load = Load()
battalion = Battalion()

load.saveload()

repeatmenu = 1
menu = "0"


while repeatmenu == 1:
   if menu == "0":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("main menu:")
      print("\n1 : battalion interactions")
      print("2 : end turn       current turn = ", counter) 
      print("3 : exit")
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
      os.system('cls' if os.name == 'nt' else 'clear')
      print("ending turn...")
      counter = endturn.buh(counter)
      time.sleep(2)
      menu = "0"  

   elif menu == "3":
      print("exiting and saving...")
      # add save function here???
      time.sleep(3)
      repeatmenu = "0"
    
   else:
     print("invalid menu")
     time.sleep(2)
     menu = "0"

 
    
      
        
    
