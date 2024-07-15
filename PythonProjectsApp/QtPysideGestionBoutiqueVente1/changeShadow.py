import json
from numpy import random

def changeRandom() :
    try :
        color=["red","white","green","blue","#ff00d5",
            "#7649ff","#ff52ac","#ff9447","#57d9b9",
            "#7a69cf","#cf6599" ,"#005500","#e6813e","#e6813e"
            ,"#ff00bb","#8859ff"]

        r=random.randint(0,len(color))
        col=color[r]
        file=open('style.json',mode='r')
        data=json.load(file)
        file.close()
        data["QMainWindow"][0]['shadow'][0]['color']=col
        file=open('style.json',mode='w')
        file.write(json.dumps(data , indent=4))
        file.close()
    except  Exception  as e : print(e)
changeRandom()