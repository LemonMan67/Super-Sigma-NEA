from . import Json

Bpath = Json.loadjson (Json.Path ("./json/battalion.json"))
BCpath = Json.loadjson (Json.Path ("./json/battalioncost.json"))

def hp(divlist, tankera, IFVera, Infera, artera, AAera, ATera):    #hp is a total of all units 
    hp = 0
    era = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            hp += Bpath["battalion"] [0] ["list"] [era] ["era"] ["hp"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            hp += Bpath["battalion"] [1] ["list"] [era] ["era"] ["hp"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            hp += Bpath["battalion"] [2] ["list"] [era] ["era"] ["hp"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            hp += Bpath["battalion"] [3] ["list"] [era] ["era"] ["hp"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            hp += Bpath["battalion"] [4] ["list"] [era] ["era"] ["hp"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            hp += Bpath["battalion"] [5] ["list"] [era] ["era"] ["hp"]
        else:
            hp += 0
    return hp
            

def attack(divlist, tankera, IFVera, Infera, artera, AAera, ATera):  #attack is a total of all units
    attack = 0
    era = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            attack += Bpath["battalion"] [0] ["list"] [era] ["era"] ["attack"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            attack += Bpath["battalion"] [1] ["list"] [era] ["era"] ["attack"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            attack += Bpath["battalion"] [2] ["list"] [era] ["era"] ["attack"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            attack += Bpath["battalion"] [3] ["list"] [era] ["era"] ["attack"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            attack += Bpath["battalion"] [4] ["list"] [era] ["era"] ["attack"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            attack += Bpath["battalion"] [5] ["list"] [era] ["era"] ["attack"]
        else:
            attack += 0

    return attack

def org(divlist, tankera, IFVera, Infera, artera, AAera, ATera):   #org is an average of all units 
    org = 0
    orgtotal = 0
    era = 0
    unitcount = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            orgtotal += Bpath["battalion"] [0] ["list"] [era] ["era"] ["org"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            orgtotal += Bpath["battalion"] [1] ["list"] [era] ["era"] ["org"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            orgtotal += Bpath["battalion"] [2] ["list"] [era] ["era"] ["org"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            orgtotal += Bpath["battalion"] [3] ["list"] [era] ["era"] ["org"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            orgtotal += Bpath["battalion"] [4] ["list"] [era] ["era"] ["org"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            orgtotal += Bpath["battalion"] [5] ["list"] [era] ["era"] ["org"]
        else:
            orgtotal += 0

    for x in divlist:
        if x != "Ta" and x != "IV" and x != "In" and x != "Ar" and x != "AA" and x != "AT":
            unitcount = unitcount
        else:
            unitcount += 1
    if unitcount > 0:
       org = orgtotal / unitcount

    return org

def defense(divlist, tankera, IFVera, Infera, artera, AAera, ATera):  #defense is a total of all units
    defense = 0
    era = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            defense += Bpath["battalion"] [0] ["list"] [era] ["era"] ["defense"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            defense += Bpath["battalion"] [1] ["list"] [era] ["era"] ["defense"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            defense += Bpath["battalion"] [2] ["list"] [era] ["era"] ["defense"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            defense += Bpath["battalion"] [3] ["list"] [era] ["era"] ["defense"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            defense += Bpath["battalion"] [4] ["list"] [era] ["era"] ["defense"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            defense += Bpath["battalion"] [5] ["list"] [era] ["era"] ["defense"]
        else:
            defense += 0

    return defense

def breakthrough(divlist, tankera, IFVera, Infera, artera, AAera, ATera):  #total of all units
    breakthrough = 0
    era = 0 
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            breakthrough += Bpath["battalion"] [0] ["list"] [era] ["era"] ["breakthrough"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            breakthrough += Bpath["battalion"] [1] ["list"] [era] ["era"] ["breakthrough"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            breakthrough += Bpath["battalion"] [2] ["list"] [era] ["era"] ["breakthrough"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            breakthrough += Bpath["battalion"] [3] ["list"] [era] ["era"] ["breakthrough"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            breakthrough += Bpath["battalion"] [4] ["list"] [era] ["era"] ["breakthrough"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            breakthrough += Bpath["battalion"] [5] ["list"] [era] ["era"] ["breakthrough"]
        else:
            breakthrough += 0

    return breakthrough

def pierce(divlist, tankera, IFVera, Infera, artera, AAera, ATera):  #70% of highest + 30% of average
    pierce = 0
    piercetotal = 0
    era = 0
    unitcount = 0
    highpierce = 0
    batpierce = 0
    pierceavg = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            piercetotal += Bpath["battalion"] [0] ["list"] [era] ["era"] ["pierce"]
            batpierce = Bpath["battalion"] [0] ["list"] [era] ["era"] ["pierce"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            piercetotal += Bpath["battalion"] [1] ["list"] [era] ["era"] ["pierce"]
            batpierce = Bpath["battalion"] [1] ["list"] [era] ["era"] ["pierce"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            piercetotal += Bpath["battalion"] [2] ["list"] [era] ["era"] ["pierce"]
            batpierce = Bpath["battalion"] [2] ["list"] [era] ["era"] ["pierce"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            piercetotal += Bpath["battalion"] [3] ["list"] [era] ["era"] ["pierce"]
            batpierce = Bpath["battalion"] [3] ["list"] [era] ["era"] ["pierce"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            piercetotal += Bpath["battalion"] [4] ["list"] [era] ["era"] ["pierce"]
            batpierce = Bpath["battalion"] [4] ["list"] [era] ["era"] ["pierce"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            piercetotal += Bpath["battalion"] [5] ["list"] [era] ["era"] ["pierce"]
            batpierce = Bpath["battalion"] [5] ["list"] [era] ["era"] ["pierce"]
        else:
            piercetotal += 0
            batpierce = 0
        
        if batpierce > highpierce:
            highpierce = batpierce

    for x in divlist:
        if x != "Ta" and x != "IV" and x != "In" and x != "Ar" and x != "AA" and x != "AT":
            unitcount = unitcount

        else:
            unitcount += 1
    
    if unitcount > 0:
      pierceavg = piercetotal / unitcount
    pierce = (highpierce * 0.7) + (pierceavg * 0.3)

    return pierce

def armour(divlist, tankera, IFVera, Infera, artera, AAera, ATera): #30% of highest + 70% of average
    armour = 0
    armourtotal = 0
    era = 0
    unitcount = 0
    higharmour = 0
    batarmour = 0
    armouravg = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            armourtotal += Bpath["battalion"] [0] ["list"] [era] ["era"] ["armour"]
            batarmour = Bpath["battalion"] [0] ["list"] [era] ["era"] ["armour"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            armourtotal += Bpath["battalion"] [1] ["list"] [era] ["era"] ["armour"]
            batarmour = Bpath["battalion"] [1] ["list"] [era] ["era"] ["armour"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            armourtotal += Bpath["battalion"] [2] ["list"] [era] ["era"] ["armour"]
            batarmour = Bpath["battalion"] [2] ["list"] [era] ["era"] ["armour"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            armourtotal += Bpath["battalion"] [3] ["list"] [era] ["era"] ["armour"]
            batarmour = Bpath["battalion"] [3] ["list"] [era] ["era"] ["armour"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            armourtotal += Bpath["battalion"] [4] ["list"] [era] ["era"] ["armour"]
            batarmour = Bpath["battalion"] [4] ["list"] [era] ["era"] ["armour"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            armourtotal += Bpath["battalion"] [5] ["list"] [era] ["era"] ["armour"]
            batarmour = Bpath["battalion"] [5] ["list"] [era] ["era"] ["armour"]
        else:
            armourtotal += 0
            batarmour = 0
        
        if batarmour > higharmour:
            higharmour = batarmour

    for x in divlist:
        if x != "Ta" and x != "IV" and x != "In" and x != "Ar" and x != "AA" and x != "AT":
            unitcount = unitcount

        else:
            unitcount += 1
    
    if unitcount > 0:
      armouravg = armourtotal / unitcount
    armour = (higharmour * 0.3) + (armouravg * 0.7)
    return armour

def AA(divlist, tankera, IFVera, Infera, artera, AAera, ATera): #AA is a total of all units
    AAtotal = 0
    era = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            AAtotal += Bpath["battalion"] [0] ["list"] [era] ["era"] ["AA"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            AAtotal += Bpath["battalion"] [1] ["list"] [era] ["era"] ["AA"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            AAtotal += Bpath["battalion"] [2] ["list"] [era] ["era"] ["AA"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            AAtotal += Bpath["battalion"] [3] ["list"] [era] ["era"] ["AA"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            AAtotal += Bpath["battalion"] [4] ["list"] [era] ["era"] ["AA"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            AAtotal += Bpath["battalion"] [5] ["list"] [era] ["era"] ["AA"]
        else:
            AAtotal += 0

    return AAtotal

def recon(divlist, tankera, IFVera, Infera, artera, AAera, ATera): #recon is a total of all units
    recon = 0
    era = 0 
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            recon += Bpath["battalion"] [0] ["list"] [era] ["era"] ["recon"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            recon += Bpath["battalion"] [1] ["list"] [era] ["era"] ["recon"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            recon += Bpath["battalion"] [2] ["list"] [era] ["era"] ["recon"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            recon += Bpath["battalion"] [3] ["list"] [era] ["era"] ["recon"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            recon += Bpath["battalion"] [4] ["list"] [era] ["era"] ["recon"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            recon += Bpath["battalion"] [5] ["list"] [era] ["era"] ["recon"]
        else:
            recon += 0

    return recon

def entrenchment(divlist, tankera, IFVera, Infera, artera, AAera, ATera): #entrenchment is a total of all units
    entrenchment = 0
    era = 0 
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            entrenchment += Bpath["battalion"] [0] ["list"] [era] ["era"] ["entrenchment"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            entrenchment += Bpath["battalion"] [1] ["list"] [era] ["era"] ["entrenchment"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            entrenchment += Bpath["battalion"] [2] ["list"] [era] ["era"] ["entrenchment"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            entrenchment += Bpath["battalion"] [3] ["list"] [era] ["era"] ["entrenchment"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            entrenchment += Bpath["battalion"] [4] ["list"] [era] ["era"] ["entrenchment"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            entrenchment += Bpath["battalion"] [5] ["list"] [era] ["era"] ["entrenchment"]
        else:
            entrenchment += 0

    return entrenchment

def cost(divlist, tankera, IFVera, Infera, artera, AAera, ATera): #cost is a total of all units
    cost = 0
    era = 0 
    actualcost = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            cost = BCpath["battalion"] [0] ["list"] [era] ["era"] ["cost"]
            actualcost += cost * Bpath["battalion"] [0] ["list"] [era] ["era"] ["amount"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            cost = BCpath["battalion"] [1] ["list"] [era] ["era"] ["cost"]
            actualcost += cost * Bpath["battalion"] [1] ["list"] [era] ["era"] ["amount"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            cost = BCpath["battalion"] [2] ["list"] [era] ["era"] ["cost"]
            actualcost += cost * Bpath["battalion"] [2] ["list"] [era] ["era"] ["amount"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            cost = BCpath["battalion"] [3] ["list"] [era] ["era"] ["cost"]
            actualcost += cost * Bpath["battalion"] [3] ["list"] [era] ["era"] ["amount"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            cost = BCpath["battalion"] [4] ["list"] [era] ["era"] ["cost"]
            actualcost += cost * Bpath["battalion"] [4] ["list"] [era] ["era"] ["amount"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            cost = BCpath["battalion"] [5] ["list"] [era] ["era"] ["cost"]
            actualcost += cost * Bpath["battalion"] [5] ["list"] [era] ["era"] ["amount"]
        else:
            cost += 0
        
    return actualcost

def steel(divlist, tankera, IFVera, Infera, artera, AAera, ATera): #steel is a total of all units
    steel = 0
    era = 0 
    actualsteel = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            steel = BCpath["battalion"] [0] ["list"] [era] ["era"] ["steel"]
            actualsteel += steel * Bpath["battalion"] [0] ["list"] [era] ["era"] ["amount"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            steel = BCpath["battalion"] [1] ["list"] [era] ["era"] ["steel"]
            actualsteel += steel * Bpath["battalion"] [1] ["list"] [era] ["era"] ["amount"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            steel = BCpath["battalion"] [2] ["list"] [era] ["era"] ["steel"]
            actualsteel += steel * Bpath["battalion"] [2] ["list"] [era] ["era"] ["amount"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            steel = BCpath["battalion"] [3] ["list"] [era] ["era"] ["steel"]
            actualsteel += steel * Bpath["battalion"] [3] ["list"] [era] ["era"] ["amount"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            steel = BCpath["battalion"] [4] ["list"] [era] ["era"] ["steel"]
            actualsteel += steel * Bpath["battalion"] [4] ["list"] [era] ["era"] ["amount"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            steel = BCpath["battalion"] [5] ["list"] [era] ["era"] ["steel"]
            actualsteel += steel * Bpath["battalion"] [5] ["list"] [era] ["era"] ["amount"]
        else:
            steel += 0
        
    return actualsteel

def copper (divlist, tankera, IFVera, Infera, artera, AAera, ATera): #copper is a total of all units
    copper = 0
    era = 0 
    actualcopper = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            copper = BCpath["battalion"] [0] ["list"] [era] ["era"] ["copper"]
            actualcopper += copper * Bpath["battalion"] [0] ["list"] [era] ["era"] ["amount"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            copper = BCpath["battalion"] [1] ["list"] [era] ["era"] ["copper"]
            actualcopper += copper * Bpath["battalion"] [1] ["list"] [era] ["era"] ["amount"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            copper = BCpath["battalion"] [2] ["list"] [era] ["era"] ["copper"]
            actualcopper += copper * Bpath["battalion"] [2] ["list"] [era] ["era"] ["amount"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            copper = BCpath["battalion"] [3] ["list"] [era] ["era"] ["copper"]
            actualcopper += copper * Bpath["battalion"] [3] ["list"] [era] ["era"] ["amount"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            copper = BCpath["battalion"] [4] ["list"] [era] ["era"] ["copper"]
            actualcopper += copper * Bpath["battalion"] [4] ["list"] [era] ["era"] ["amount"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            copper = BCpath["battalion"] [5] ["list"] [era] ["era"] ["copper"]
            actualcopper += copper * Bpath["battalion"] [5] ["list"] [era] ["era"] ["amount"]
        else:
            copper = 0

    return actualcopper

def oil (divlist, tankera, IFVera, Infera, artera, AAera, ATera): #oil is a total of all units
    oil = 0
    era = 0 
    actualoil = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            oil = BCpath["battalion"] [0] ["list"] [era] ["era"] ["oil"]
            actualoil += oil * Bpath["battalion"] [0] ["list"] [era] ["era"] ["amount"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            oil = BCpath["battalion"] [1] ["list"] [era] ["era"] ["oil"]
            actualoil += oil * Bpath["battalion"] [1] ["list"] [era] ["era"] ["amount"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            oil = BCpath["battalion"] [2] ["list"] [era] ["era"] ["oil"]
            actualoil += oil * Bpath["battalion"] [2] ["list"] [era] ["era"] ["amount"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            oil = BCpath["battalion"] [3] ["list"] [era] ["era"] ["oil"]
            actualoil += oil * Bpath["battalion"] [3] ["list"] [era] ["era"] ["amount"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            oil = BCpath["battalion"] [4] ["list"] [era] ["era"] ["oil"]
            actualoil += oil * Bpath["battalion"] [4] ["list"] [era] ["era"] ["amount"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            oil = BCpath["battalion"] [5] ["list"] [era] ["era"] ["oil"]
            actualoil += oil * Bpath["battalion"] [5] ["list"] [era] ["era"] ["amount"]
        else: 
            oil = 0

    return actualoil

def rare(divlist, tankera, IFVera, Infera, artera, AAera, ATera): #rare metal cost is a total of all units
    rare = 0
    era = 0 
    actualrare = 0
    for x in divlist:
        if x == "Ta":
            unit = "tank"
        elif x == "IV":
            unit = "IFV"
        elif x == "In":
            unit = "infantry"
        elif x == "Ar":
            unit = "artillery"
        elif x == "AA":
            unit = "AA"
        elif x == "AT":
            unit = "AT"
        else:
            unit = ""
        if unit == "tank":
            if tankera == "WW2":
                era = 2
            elif tankera == "CW":
                era = 1
            elif tankera == "Modern":
                era = 0
            rare = BCpath["battalion"] [0] ["list"] [era] ["era"] ["rare metals"]
            actualrare += rare * Bpath["battalion"] [0] ["list"] [era] ["era"] ["amount"]
        elif unit == "IFV":
            if IFVera == "WW2":
                era = 2
            elif IFVera == "CW":
                era = 1
            elif IFVera == "Modern":
                era = 0
            rare = BCpath["battalion"] [1] ["list"] [era] ["era"] ["rare metals"]
            actualrare += rare * Bpath["battalion"] [1] ["list"] [era] ["era"] ["amount"]
        elif unit == "infantry":
            if Infera == "WW2":
                era = 2
            elif Infera == "CW":
                era = 1
            elif Infera == "Modern":
                era = 0
            rare = BCpath["battalion"] [2] ["list"] [era] ["era"] ["rare metals"]
            actualrare += rare * Bpath["battalion"] [2] ["list"] [era] ["era"] ["amount"]
        elif unit == "artillery":
            if artera == "WW2":
                era = 2
            elif artera == "CW":
                era = 1
            elif artera == "Modern":
                era = 0
            rare = BCpath["battalion"] [3] ["list"] [era] ["era"] ["rare metals"]
            actualrare += rare * Bpath["battalion"] [3] ["list"] [era] ["era"] ["amount"]
        elif unit == "AA":
            if AAera == "WW2":
                era = 2
            elif AAera == "CW":
                era = 1
            elif AAera == "Modern":
                era = 0
            rare = BCpath["battalion"] [4] ["list"] [era] ["era"] ["rare metals"]
            actualrare += rare * Bpath["battalion"] [4] ["list"] [era] ["era"] ["amount"]
        elif unit == "AT":
            if ATera == "WW2":
                era = 2
            elif ATera == "CW":
                era = 1
            elif ATera == "Modern":
                era = 0
            rare = BCpath["battalion"] [5] ["list"] [era] ["era"] ["rare metals"]
            actualrare += rare * Bpath["battalion"] [5] ["list"] [era] ["era"] ["amount"]
        else:
            rare = 0

    return actualrare
