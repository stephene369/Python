# un objet constituer de 1-type 2-d'attribut et de 3-methodes
num=5   # type : int
num.numerator #tr 

## introduction au class
class User :
    pass


Jonh = User() # on dit que john est une instance de user
## definition des attributs pour l'objet Jonh
Jonh.id=12
Jonh.age=35
Jonh.nom="stephene"
Jonh.password = "mot de pass"

print("Information : .. "+
      " id : {}, age : {} , nom : {}".format(
     Jonh.id , Jonh.age , Jonh.nom))

# pour supprimer un objet
del num


# # exemple concret
def check_password(user , password) :
    return user.password == password
check_password(Jonh , "ste")
check_password(Jonh , 'mot de pass')


## les classes et les methodes
class User :
    def check_pass(self , password ) :
        return self.password == password
    
User.check_pass(self=Jonh , password="stre")

## definition d;une classe et initialisation des objets
"""
Les différents attributs de notre
objet forment un état de
cet objet, normalement stable. 

"""
class Utilisateur :
    def __init__(self , id, name , password) :
        self.id=id
        self.name=name
        self.password=password
    
    def check_pass (self , password):
        for i in range(self.id):
            print(i)
        return self.password 
    
stephene=Utilisateur(1,'stephe','mot de pass')
print(stephene.check_pass('mot de pass'))

## Encapsulation 
""" 
C'est la notion de protection des attributs et methodes
d'un objet 
"""
import crypt

class User : 
    def __init__(self,id,name,password) :
        self.id=id
        self.name=name
        self._salt=crypt.mksalt()
        self._password = self._crypt_password(password)

    def _crypt_password (self,password) :
        return crypt.crypt(password,self._salt)

    def check_password(self , password) :
        return self._password == self._crypt_password(password)
                            
crypt.crypt('stephen' , crypt.mksalt())


"""
X= [0,1,2,3,4,5,6,7,8,9]
N = [5,6,9,7,6,5,4,3,3,2]
mean = 0
for i in range(10) : 
    mean = mean+(X[i] * N[i])

sum(X)
mean/10  
"""

