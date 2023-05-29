parouimpar = str(input("Escolha PAR ou IMPAR: "))


import random
import time

numero = int(input("Escolha um número de 1 à 5: "))
x = random.randint (1,5) 

resultado = numero + x
resto = resultado % 2
print ("o resultado é", resultado)
print ("PROCESSANDO [/////   ]")
time.sleep(2)
if (parouimpar == "PAR" and resto == 0):
    print("Você ganhou!")
elif (parouimpar == "IMPAR" and resto != 0):
    print("Você ganhou!")
if (parouimpar == "PAR" and resto != 0):
    print("Você perdeu!")
elif (parouimpar == "IMPAR" and resto == 0):
    print("Você perdeu!")
 
    
