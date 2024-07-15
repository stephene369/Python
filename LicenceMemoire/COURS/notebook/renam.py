


with open("MA.ipynb" , "r") as m:
    fil = m.read()
    m.close()

with open ("osci.ipynb" , "w") as w :
    w.write(fil.replace("boab","brvm").replace("BOAB","BRVM") )
    w.close()

t = open("tr.txt" , 'w')