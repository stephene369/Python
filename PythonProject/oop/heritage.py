projets = ["pu_spiderman" , "pr_naruto" , "pr_avangers"]

class Utilisateur :
    def __init__(self , nom , prenom) :
        self.nom = nom
        self.prenom = prenom 

    def __str__(self) :
        return f"Utilisateur {self.nom}  {self.prenom}"

    def affiche_projet(self) :
        for projet in projets :
            if projet.startswith("pr") : 
                print(projet)


class Junior(Utilisateur) :
    def __init__(self , nom,prenom) :
        Utilisateur.__init__(self,nom,prenom)
        pass

paul = Utilisateur("Paul" ,"WANT")
paul.affiche_projet() 


paul = Junior("Paul" ,"WANT")
paul.affiche_projet() 
