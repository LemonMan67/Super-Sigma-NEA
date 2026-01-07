import json 
from pathlib import Path

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

    def Bcheck (self ,stat):
        print("for", stat ,":")
        for x in self.info ["battalion"]:
            print (f" Unit:  {x['unit']} ")
            for y in x ["list"]:
                print (f"  { y["era"]["type"] } has { y["era"][stat]} {stat} ")


battalion = Battalion()
while True:
  stat = input ("\nstat? ")
  if stat == "stop":
      False
  battalion.Bcheck(stat)
    
