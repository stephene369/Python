class Voiture :
    marque  = "b"   # marque est un attribut de classe

voiture_01 = Voiture () # voiture_01 est une estance de la classe  voiture
voiture_01.marque

Voiture.marque = "Porche" # modifivation de l attribut de classe

# modification de l'attribut de l'extence
voiture_01.marque = 'toyota'
voiture_01.marque


# # la methode init permet d'initialiser les instance
class Voiture :

    def __init__(self, marque) :
        self.marque = marque

voiture2 = Voiture("nike")
voiture2.marque



## un reel exemple
class Voiture :
    def __init__(self,marque) :
        self.marque = marque 
    
    def afficher_marque (self , nom) :
        print(nom)
        print(self.marque)