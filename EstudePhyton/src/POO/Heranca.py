class Person:
    
    def __init__(self,first,last):
        self.firstname = first
        self.lastname  = last
    
    def name(self):
        return self.firstname + " " + self.lastname
    

#  Heranca da classe Person
class Employe(Person):
    
    def __init__(self,first,last,employeId):
        #HERDANDO CLASSE PERSON
        Person.__init__(self,first,last)
        self.employeId = employeId
    
    def getEmploye(self):
        return self.name() + " , " + self.employeId
    
x = Person("Euclides","Chuna")
y = Employe("Jose","Silva","1007")

print(x.name())
print(y.getEmploye())


#Exemplo 2
class Vehicle:
    
    def __init__(self,vehicleType):
        self.vehicleType = vehicleType
        
    def __str__(self):
        return self.vehicleType

class Car(Vehicle):
    
    def __init__(self,automaker,model,combustible):
        super().__init__("car")
        self.automaker      = automaker
        self.model          = model
        self.combustible    = combustible
        
    def __str__(self):
        return super().__str__() + " ," + self.automaker + " ," + self.model + " ," + self.combustible
    
class Truck(Vehicle):
    
    def __init__(self,automaker,model):
        super().__init__("truck")
        self.automaker      = automaker
        self.model          = model
        self.combustible    = "diesel"
    
    def __str__(self):
        return super().__str__() + " ," + self.automaker + " ," + self.model + " ," + self.combustible

myCar = Car("Fiat","Uno","Gasolina")
myTruck = Truck("Volvo","D100")


print(myCar);
print(myTruck);
