import random as axell

print("Lanzamientos de dados")
cont=1
dado = rd.randint(1, 6)
print('dado: ', dado)
while dado != 6 and cont!=3:
    cont+=1
    dado = rd.randint(1, 6)
    print('dado: ', dado)

if dado==6:
    print("Ocurrieron {} lanzamientos".format(cont))
    print("Ganaste")
else:
    print("Perdiste")
