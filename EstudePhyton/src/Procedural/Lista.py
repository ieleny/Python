#Lista salva uma sequencia de qualquer tipo
#lista 1
print("Teste de Listas")
myList = [54,23,69,45,12,30,98]

print("Numero da lista do posicao 0", myList[0])
print("Quantidade da lista e :",len(myList))

#lista 2 - INSERIR 
print("Definir Listas")
myNewList = []
myNewList.insert(0,'Ieleny')
myNewList.insert(1,'Teste')
myNewList.insert(2,'Coisa')
myNewList.insert(3,'Coisada')
myNewList.insert(4,'Coisadinha')

#Inserindo novo valor
myNewList[2] = 989

print("Numero da lista do posicao 2", myNewList[2])

#Lista 3 - Randomico
import random

myRandomList = []

for i in range(25):
    myRandomList.append(random.randrange(1,100,1))
    
print(myRandomList)
print("A quantidade da lista e :" , len(myRandomList));

#Lista 4 - Mostrando uma lista com array
print("Teste de Listas")
myList1 = [45,23,69,45,12,30,98]

for item in myList1:
    print(item,)
    
#Lista 5 - Ordenando Lista
myList1.sort()
print("Depois de Ordenado")
for item in myList1:
    print(item,)
    
#Lista 6 - Lista Reversa
myList1.reverse()
print("Depois de Revertido")
for item in myList1:
    print(item,)
    
#Contar a quantidade de vezes que um intem apareceu na lista
print("Quantidade de Vezes que o numero 45 apareceu:",myList1.count(45))








