# import random as rd
from random import *

print("Estás en la carcel")
intentos = 0

#Opcion 2
respuesta = input("¿dados o multa?: ")
if respuesta == "multa" :
    print("Haz pagado $50, pero eres libre")
else:
    intentos+=1
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    print('Dados: ', dado1,dado2)
    while dado1 != dado2 and respuesta == "dados" and intentos!=3:
        respuesta = input("¿dados o multa?: ")
        if respuesta =="dados":
            dado1 = randint(1, 6)
            dado2 = randint(1, 6)
            intentos += 1
            print('Dados: ', dado1,dado2)
    
    if dado1 == dado2:
        print("¡Eres libre!")
    elif intentos == 3 or respuesta == "multa":
        print("Haz pagado $50, pero eres libre")
        
        
    
      
        
#Horrible opcion 1
# dado1 = -1
# dado2 = -2
# respuesta = "dados"
# while dado1 != dado2 and respuesta == "dados" and intentos!=3 :
#     respuesta = input("¿dados o multa?: ")
#     if respuesta =="dados":
#         dado1 = randint(1, 6)
#         dado2 = randint(1, 6)
#         intentos += 1
#         print('Dados: ', dado1,dado2)
# if dado1 == dado2:
#     print("¡Eres libre!")
# elif intentos == 3 or respuesta == "multa":
#     print("Haz pagado $50, pero eres libre")
        
        
    
        
        











        
    
    
    
    

    