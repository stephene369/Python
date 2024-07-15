# Employee --> Teacher

class Employee :
    def __init__(self , name , age) :
        self.name=name
        self.age=age
    
    def getAge(self):
        return self.age

class Teacher (Employee) :
    def __init(self , name  , age , class_room) :
        self.class_room = class_room

        Employee.__init__(self, name , age )

new_teacher = Teacher(name = "WNATCHELON " , age = 60  )
print(new_teacher.getAge())
