
class Employee : 
    def __init__(self , id, name , age, email) :
        self.id = id 
        self.name =  name 
        self.age  = age 
        self.email =  email

    
    def getEmail(self) :
        return self.email
    
     
employer_01 =  Employee(id = 1 
                        , name= "Stephene",
                        age=23 , email="stephenew36@gmail.com")

employer_01.getEmail()