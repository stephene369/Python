#### DUNDER or magic methodes

class Person :
    
    def __init__(self, name , age ) :
        self.name = name
        self.age = age

    def __del__(self) :
        print("Object is being deleted")

#p = Person("ste" , 12)


##
class  Vector:

    def __init__ (self , x , y) :
        self.x = x
        self.y = y 

    def __add__ (self , other ) : 
        return Vector(self.x + other.x , self.x + other.y)
    
    def __repr__(self) -> str:
        return f"X = {self.x} and Y = {self.y}"

    def __len__(self) :
        return 10

    def __call__(self) :
        print("hello i was called")

    

v1  = Vector(10,20)
v2 = Vector(20, 40)
v3 =  v1+v2

print(v3.x)
print(v3)
print(len(v3))
v3()
