
def buh (counter):
    counter += 1
    with open ("./save/turncount.txt" , "w") as f:
        f.write (str(counter))
        f.close()
    return counter