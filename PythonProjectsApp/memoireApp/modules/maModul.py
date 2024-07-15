from Ui.library import OBJECT


class getParameter :
    def __init__(self) -> None:
        self.horizon = OBJECT["horizon"] 
        self.objectif = OBJECT["objectif"]
        self.tolerance = OBJECT["tolerance"]

        
    def parameter(self) : 
        match self.horizon.currentText() :
            case "Court terme" :
                return 5 , 10
            case "Moyen terme" :
                return 20 , 50 
            case "Long terme" :
                return 50, 100 



            



