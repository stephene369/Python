from datetime import date

class Person :
    def __init__(self , name , age):
        self.name=name
        self.age =  age

   
    def displayInfo(self) :
        return f"Name {self.name } age {self.age}"


    @classmethod
    def fromBirthYear(cls , name , birth_year) :
        
        return cls(name = name , age = (date.today().year - birth_year))
    
p = Person(name=' ' , age=4)
p.displayInfo()

moi1 = Person(" " , 23)
moi= Person.fromBirthYear( name=' ' , birth_year=2020)
print(moi.age)

