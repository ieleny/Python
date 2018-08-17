#Tuplas nao modificam sao valores fixos
myTuple ='Ieleny', 2018,'Genius',3.465,'Y'
print("\n Items da Tuplas",myTuple)
print("\n Quantidade de Tuplas",len(myTuple))
print("\n Pela a Posicao",myTuple[1])

#Tuplas segundo Exemplo
print("\n Tuplas de Posicao")
MyNewTuple = tuple('ieleny')
print("\n Items da Tuplas",MyNewTuple)
print("\n Quantidade de Tuplas",len(MyNewTuple))
print("\n Pela a Posicao",MyNewTuple[0])

#Tuplas Terceiro Exemplo
myCarTuple = ('Ford','Focus',2018,2.0,'Branco')
(marca,modelo, ano, cc , cor) = myCarTuple

print("\n Marca",marca)
print("\n Modelo",modelo)
print("\n Ano",ano)
print("\n CC",cc)
print("\n Cor",cor)

#Sequencia Multidimensionais
print("Lista Multidimensionais")
myMultimensionalSequencia = [ [1,2,3] , [4,5,6] , [7,8,9] ]

for row in myMultimensionalSequencia:
    for item in row:
        #Da erro mais funciona
        print(item,end=" ")
    print()

#Dicionarios
print("Dicionarios de dados")
myMultimensionalSequencia = {"Teste":1.33 , "Teste1":1.33}
print("Toda a Linha",myMultimensionalSequencia)
print("O valor de Teste e",myMultimensionalSequencia['Teste'])

#Metodos do Dicionarios
print("Itens do Dicionario",myMultimensionalSequencia.items())
print("Itens do Dicionario",myMultimensionalSequencia.items())
print("Chaves",myMultimensionalSequencia.keys())
print("Valor",myMultimensionalSequencia.values())
print("Tamanho",len(myMultimensionalSequencia))

#Inserir 
MyInput = input("Insira seus dados")
MyInput = int(MyInput)

if(MyInput in myMultimensionalSequencia):
    print("Seus Dados sao",myMultimensionalSequencia[MyInput])
else:
    print("Nao Encontrado")











