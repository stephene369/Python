
class Employee : 
    salary = 20000
    
    def getSalary(cls):
        return cls.salary

Employee.getSalary=classmethod(Employee.getSalary)

Employee.getSalary()


##   # #  ##  ### 


class Employee : 
    salary = 20000
    
    @classmethod
    def getSalary(cls):
        return cls.salary

Employee.getSalary()


 # # # ##  # # ##


