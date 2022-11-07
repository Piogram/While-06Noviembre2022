password= input("Ingrese contraseña: ")
size= len(password)
while not (6<=size<=12) or not ("-" in password or "_" in password):
    if not (6<=size<=12):
        print("La contraseña debe tener entre 6 y 12 caracteres")
    if not ("-" in password or "_" in password):
        print("La contraseña debe tener al menos un - o _") 
    password= input("Ingrese contraseña: ")
    size= len(password)

    
    