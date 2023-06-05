
import random
import time

contador = 0

for contador in range (3):
    contador = contador + 1
    numero = int(input("Escolha um número de 1 à 10: "))
    x = random.randint (1,10) 


    if (numero == x ):
        print("Você ganhou!")
    elif (numero != x):
        print("Você errou!")
    continue 


 