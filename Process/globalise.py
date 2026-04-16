from pathlib import Path
from Process import Json

def Globalise():
      data = Json.loadjson(Path("./json/save.json"))     #this function is never used 
      #global counter  
      counter = data ["counter"]
      return counter