#Classes
class Pet:
    #Construtor
    def __init__(self,name,especie):
        self.name = name
        self.especie = especie
    
    #Atributo sempre tem que ter o Self - Seria o this no PHP
    def getName(self):
        return self.name
        
    def getEspecie(self):
        return self.especie

    #Atributo especial que serve para exibicao padrao
    def __str__(self):
        return "%s e a %s" % (self.name,self.especie)

#Objeto
MyPet1 = Pet("Pepita","Cachorro")
MyPet2 = Pet("Bob","Gato")
MyPet3 = Pet("Snow","Tamandua")

print(MyPet1)
print(MyPet2)
print(MyPet3)

print("MyPet1 nome do atributo " + str(MyPet1.getName()))
print("MyPet3 Especie do atributo " + str(MyPet3.getEspecie()))
print("MyPet2 nome do atributo " + str(MyPet2.getName()))
print("MyPet2 Especie do atributo " + str(MyPet2.getEspecie()))


class Employ:
    employesCount = 0
    
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
        
    def showEmploye(self):
        print("\nNome:", self.nome , ";Salario:" ,self.salario)
        
    def showCount(self):
        print("\Quantidade de Funcionarios e %d" % Employ.employesCount)
        

#Fazendo a chamada de outra classe dentro de outra pagina
from POO import Employ
Employ1 = Employ("Ieleny",111000)
Employ2 = Employ("Maria",111000)

Employ1.showEmploye()
Employ2.showEmploye()

Employ1.showCount()
Employ2.showCount()

#Atributos especiais
print("\n\nEmploy.__name__",Employ.__name__)
print("\n\nEmploy.__module__",Employ.__module__)
print("\n\nEmploy.__bases__",Employ.__bases__)
print("\n\nEmploy.__dict__",Employ.__dict__)
print("\n\nEmploy.__doc__",Employ.__doc__)


    
    