from dataclasses import dataclass
from typing import ClassVar # pour cree des attribut de classe


@dataclass
class User () :
    fist_name : str
    last_name : str = ""
    c:ClassVar[int] = 0 # attribt de classe

    def __post_init__(self) : # cette methode est appeler directement apres la methode __init__
        self.full_name = f"{self.fist_name} {self.last_name} "

patrick = User("NANO" , "Patrick")
patrick.__dict__ # pour afficher les attribut d'intance de patrick
patrick.fist_name







#la methode dataclass permet deciter l'initialisattion de la class

"""class User () :
    def __init__(self , first_name:str 
                 , last_name: str) :
        self.first_name =  first_name
        self.last_name = last_name
        """