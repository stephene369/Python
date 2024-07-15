

class Voiture :
    voiture_cree = 0
    def __init__(self , marque, vitess,prix) :
        Voiture.voiture_cree +=1
        self.marque = marque
        self.vitess = vitess
        self.prix = prix

    @classmethod
    def lambo(cls) :
        return cls(marque = "par",vitess = 200 , prix =3)
    
    @classmethod
    def prorshe(cls):
        return cls(marque = "toya",vitess = 200 , prix =3)
    
    @staticmethod
    def print_figure_car () :
        print(f"LE nombre de voiture est cree {Voiture.voiture_cree}")

    # une methode magique qui permet de predifini l'affichage de notre instance

    def __str__(self) :
        return f"Voiture de marque {self.marque} , avec un vites max de {self.vitess}"


lamb = Voiture.lambo()
Voiture.print_figure_car()

# affichage de l'extance lamb2 avec laffichage predefini 
lamb2 = Voiture("pors" , 300,200000)
print(lamb2)