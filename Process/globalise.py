from pathlib import Path
from Process import Json

def Globalise():
      data = Json.loadjson(Path("./json/save.json"))
      #global counter
      counter = data ["counter"]
      return counter