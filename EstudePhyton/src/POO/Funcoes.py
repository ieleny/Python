
class Car:
    
    #Construtor
    def __init__(self,automaker,model):
        self.automaker = automaker
        self.model     = model
    
    def __getattr__(self,name):
        return "Nao Existente"
    
    def __setattr__(self,name,value):
        if name == "automaker":
            if name == "GM":
                self.__dict__["automaker"] = "Chevrolet"
            else:
                self.__dict__["automaker"] = value
        else:
            self.__dict__[name] = value
    
    def __delattr__(self,name):
        print("Atributo foi Deletado")
        
    
myCar = Car("Ford","Focus")
print(myCar.automaker)
print(myCar.model)
print(myCar.year)

myCar2 = Car("GM","CELTA")
print(myCar2.automaker)
print(myCar2.model)

del myCar.model


#Exemplo 2
class Tamanho:
    
    __metric = {"nm" : 0.001 , "cm" : 0.01 ,"m" : 1,"km" : 1000}
    
    def __init__(self,value,unit = "m"):
        self.value = value;
        self.unit  = unit;
        
    def convertToMetros(self):  
        return self.value * Tamanho.__metric[self.unit]
        
    #overloading
    def __add__(self,other):
        self.other = self.convertToMetros() + other.convertToMetros()
        return Tamanho(self.other/Tamanho.__metric[self.unit],self.unit)
    
    def __repr__(self):
        return "Tamanho (" + str(self.value) + " ," + self.unit + ")"
    
z = Tamanho(3,"km") + Tamanho(200)
print(repr(z))