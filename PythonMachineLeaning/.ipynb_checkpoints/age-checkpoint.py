from datetime import datetime 
import locale
from print_color import print

locale.setlocale(locale.LC_TIME , "fr_FR.UTF-8")


###
class BirthYear :
    """Retourne l'annee de naissance d'une personne
    """
    def __init__(self , name:str , age:int) -> None:    
        self.name=name
        self.age = age

    def birthYear(self) :
        return datetime.now().year - self.age

    def __repr__(self) -> str:
        return f"{self.name.capitalize()} vous etes né en {self.birthYear()}"

uma = BirthYear(name="uma" , age=11)
print(uma , color='blue')


### 
class PersonAge :
    """Retoure la date le jour et la date de naissance d'une personne
    et son age
    """
    def __init__(self , name:str , year:int , month:int , day:int) :
        self.name = name 
        self.year = year 
        self.month = month 
        self.day = day

    def birth (self) :        
        self.birthDate = f"{self.day}/{self.month}/{self.year}"
        return datetime.strptime(self.birthDate,"%d/%m/%Y").strftime(
            "%A %d %B , %Y")
    
    def age (self) : 
        return datetime.now().year-self.year

    def __repr__(self) -> str:
        return (f"{self.name.capitalize()} vous etes né le {self.birth()} "
                +f"\nEt aujourd'hui vous avez avez {self.age()} ans ")
        
    def __call__(self) :
        print("Person a ete appele")

uma = PersonAge('uma' , 2012,1,26)
print(uma,color='green')




