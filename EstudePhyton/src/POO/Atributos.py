#Atributos
#Phyton nao possui atributos privados
class PrivateClassTest:
    
    def __init__(self):
        self.publicData = "public"
        self.__privateData = "Private"
             #^ - Maingle Ele troca o nome desse atributo para _PrivateClassTest__privateData

Classe = PrivateClassTest()
print(Classe.publicData)
print(Classe._PrivateClassTest__privateData)
Classe._PrivateClassTest__privateData = "TesteCoisado"
print(Classe._PrivateClassTest__privateData)     

#Destroyed
class Rectangle:
    
    resultArea = 0
    
    def __init__(self,sideA = 1, sideB = 1):
        self.calcArea(sideA,sideB)
    
    def calcArea(self,SideA,SideB):
        self.resultArea = SideA * SideB
        
myRectangle = Rectangle()
print("\n O resultado da Area do retangulo "+str(myRectangle.resultArea))

myRectangle2 = Rectangle(2,2)
print("\n O resultado da Area do retangulo "+str(myRectangle2.resultArea))

class point:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    #Destrusctor
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name + " Destruido")
        
p1 = point()
p2 = point()
p3 = point()
        
print(id(p1),id(p2),id(p3))    

del p1
del p2
del p3
    
    
    
    

        
              






