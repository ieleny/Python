# -*- coding: utf-8 -*-
#Numeros
#Variavel / Inserir o valor
numero1 = input("Entre com o primeiro numero:\n")
numero1 = int(numero1)
numero2 = input("Entre com o segundo numero:\n")
numero2 = int(numero2)

soma = numero1 + numero2 
print("O valor da soma e",soma)

substracion = numero1 - numero2
print("O valor da subtracao",substracion)

divisao = numero1/numero2
print("O valor da divisao",divisao)

multiplicacao = numero1*numero2
print("O valor da multiplicacao",multiplicacao)

#Strings
texto_string = "TestedeString\n" + "Testando concatencao de string"
print(texto_string)

#print("\n" * 100)
print("TestedeString sendo que estamos testando a multiplicacao")

print("Teste de formato de string")
myInteger = 12345
myFloat = 3.4654
myString = "TestedeString sendo que estamos testando alguma coisa interessante"

print("Integer",myInteger)
print("Decimal integer %d" % myInteger)
print("Decimal integer %d e o numero inteiro %d" % (myInteger,myInteger))
print("Decimal Hexadecimal %x" % myInteger)

print("Float",myFloat)
print("Principal %f" % myFloat)
print("Exponencial %e" % myFloat)
print("Direita Justificado (%10d)" % myFloat)
print("Esquerda Justificado (%-10d)" % myFloat)

print("Força 9 digitos %.9d" % myInteger)
print("3 digitos depois do decimal %.9d" % myFloat)
print("10 e 5 caracteres disponiveis pela a string")
print("(%.10s) (%5.s)" % (myString,myString))


#Operadores de igualdade e relacionamento
print("Teste de Equalidade e Relacionamento")

numero1 = input("Entre com o primeiro numero:\n")
numero1 = int(numero1)
numero2 = input("Entre com o segundo numero:\n")
numero2 = int(numero2)

#IF 
if numero1 == numero2:
        print("Numeros são Iguais")
elif numero1 != numero2:
        print("Numeros são Diferentes")
else:
        print("Infelizmente os numeros não são iguais")   

if numero1 < numero2:
        print("O numero 1 é menor que o 2")

if numero1 > numero2:
        print("O numero 1 é maior que o 2")

if numero1 >= numero2:
        print("O numero 1 é maior igual que o 2")

if numero1 >= numero2:
        print("O numero 1 é menor igual que o 2")
        
#while
while numero1 <= 4000:
        print("O valor %d" % numero1)
        numero1  =  numero1 + 1
        
print('END')

#FOR
print("Testando o for")

for x in range(1736):
    
    if x == 88:
        break
    print(x)

print("A execucao foi interrompida por que chegou no numero 88")

#Funcoes
print("Funcoes em Phyton")

def sum(arg1,arg2):
    total = arg1 + arg2
    print('O total do Valor e:',total);
    return total;

total_sum1 = sum(1,34)
total_sum2 = sum(3,56)

print(total_sum1)
print(total_sum2)
print(sum(3,5))

#Modulos e Modulos Math
import math 
#Para saber o que tem dentro de um modulo use DIR
dir(math)
print(math.pi)




    

