
import random

contador = 0

while contador < 3:
    contador = contador + 1
    numero = int(input("Escolha um número de 1 à 10: "))
    x = random.randint (1,10) 


    if (numero == x ):
        print("Você ganhou!")
        break
    elif (numero != x):
        print("Você errou!")
        print("Chances usadas: {} " .format(contador))
        
    
   


 