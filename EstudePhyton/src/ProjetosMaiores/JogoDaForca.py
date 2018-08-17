# -*- coding: utf-8 -*-
#Jogo da Forca
import time
import random 

name = input("Qual o seu nome? ")
#name1 = str(name1)
print("\n hey " + name,"hora de jogar o jogo da forca!\n")

#Esperar 5 segundos
time.sleep(5);
print("Espere para comecar")
time.sleep(1);
print("1")
time.sleep(1);
print("2")
time.sleep(1);
print("3")
time.sleep(1);
print("4")
time.sleep(1);
print("5")

print("Agora!!")

#Lista de palavras
listofWords = ("teste","ieleny","coisadas","coisas")
randomNumber = random.randint(0, len(listofWords) - 1)
guessWordl = listofWords[randomNumber]
word = guessWordl
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char),
        else:
            print("_"),
            failed += 1
            
    if failed == 0:
        print("\nVoce Ganhou!!")
        break
    print
            
    guess = input("Digite a letra que deseja: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Errado")
        print("Voce tem mais", turns , "mais tentativas")

    if turns == 0:
        print("Voce perdeu!!!")






