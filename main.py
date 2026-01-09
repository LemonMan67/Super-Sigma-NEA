from pathlib import Path
import time
import os
from Process import endturn
from Process import Json


#gng we need to figure out how to write back to json properly

class Battalion:
    def __init__(self, filepath = "./json/battalion.json"):
        self.path = Path (filepath)  
        self.info = Json.loadjson (self.path)

    def Bcheck (self):
        repeat = 1
        while repeat == 1:
          stat = input ("\nstat? ")
          if stat == "stop":
            repeat = 0
          else:
            print("for", stat ,":")
            for x in self.info ["battalion"]:
              print (f" Unit:  {x['unit']} ")
              for y in x ["list"]:
                print (f"  { y["era"]["type"] } has { y["era"][stat]} {stat} ")

class Load:
   def __init__(self , filepath = "./json/save.json"):
      self.path = Path (filepath)
      self.data = Json.loadjson (self.path)

   def saveload (self) :
      global counter
      counter = self.data ["counter"]
      

load = Load()
battalion = Battalion()

load.saveload()

repeatmenu = 1
menu = "0"

while repeatmenu == 1:
   if menu == "0":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("1 : battalion interactions")
      print("2 : end turn       current turn = ", counter) 
      print("3 : exit")
      menu = input ("\nselect menu: ")

   elif menu == "1":
      os.system('cls' if os.name == 'nt' else 'clear')
      battalion.Bcheck()
      menu = "0"
   
   elif menu == "2":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("ending turn...")
      counter = endturn.buh(counter)
      time.sleep(2)
      menu = "0"  

   elif menu == "3":
      print("exiting and saving...")

      time.sleep(3)
      repeatmenu = "0"
    
   else:
     print("invalid menu")
     time.sleep(2)
     menu = "0"

 
    
      
        
    
