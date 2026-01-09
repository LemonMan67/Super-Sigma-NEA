import json 
from pathlib import Path
import time
import os
from Process import endturn

def loadjson (filepath):
    with open (filepath , "r" ) as f:
        return json.load (f)

def writejson (filepath , update) :
    with open (filepath , "w") as f:
        json.dump(f , update , indent=5 )

class Battalion:
    def __init__(self, filepath = "battalion.json"):
        self.path = Path (filepath)  
        self.info = loadjson (self.path)

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


battalion = Battalion()

repeatmenu = 1
menu = "0"
with open ("./save/turncount.txt" , "r") as f:
   counter = f.read()
   counter = int(counter)
   f.close()

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
      with open ("turncount.txt" , "w") as f:
         f.write (counter)
         f.close()
      time.sleep(3)
      repeatmenu = "0"
    
   else:
     print("invalid menu")
     time.sleep(2)
     menu = "0"

 
    
      
        
    
