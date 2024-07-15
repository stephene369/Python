## decorators

def MyDecorator(function) :
    def wripper() :
        print("i am a decorating your fonction")
        function()
    return wripper

def MyDecorator2(function) :
    def wripper() :
        function()
        print("i am a decorating your fonction")
    
    return wripper


def hello() :
    print("Mon decorateur")

#MyDecorator(hello)()
#MyDecorator2(hello)()

def RealDecorator (function) :
    def wripper(*args, **kwargs) :
        print("i am a decorating your fonction")
        function(*args, **kwargs)
    return wripper

@RealDecorator
def hello(person):
    print(f"Hello word {person}")

#hello("Stephene")



##partical application
def logged(function) :
    def wrapper(*args, **kwargs) :
        value = function(*args,**kwargs)
        with open("loggin.txt" , "a+") as f :
            fname = function.__name__
            print(f"{fname} return value {value}")
            f.write(f"{fname} return value {value}")
        return value
    return wrapper

import time

def timed(function):
    def wrapper(*args,**kwargs) :
        before = time.time()
        value = function(*args,**kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} to excute!")
        return value
    return wrapper


@timed
def add(x,y) :
    return x+y

@timed
def pass_(v) :
    for i in range(v) :
        pass

#print(add(12,12))
print(pass_(30000000))

