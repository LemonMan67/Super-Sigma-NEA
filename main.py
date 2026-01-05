import json 
from pathlib import Path

def loadjson (filepath):
    with open (filepath , "r" ) as f:
        return json.load (f)

def writejson (filepath , update) :
    with open (filepath , "w") as f:
        json.dump(f , update , indent=4 )

class Battalion:
    def __init__(self, filepath = "battalion.json"):
        self.path = Path (filepath)  
        self.info = loadjson (self.path)

    def Bcheck (self ,stat):
        for stat , details  in self.info ["tank"].tank : 
            print (f" {type} : {details ['hp']} ") #ask for help with json and oop tmr gng 


battalion = Battalion()
battalion.Bcheck("hp")
    
