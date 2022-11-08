#Variante 1
menu="""1.- Saludar
2.- El mejor canal de youtube
3.- Salir
"""
subMenu="""a) Saludar a Piogram
b) Saludar a Axell
"""
opcion=""
while opcion != "3" : #not opcion == "3"
    print(menu)
    opcion= input("Ingrese una opción: ")
    if opcion == "1":
        
        print(subMenu)
        literal = input("Ingrese una literal: ")
        if literal =="a":
            print("Hola Piogram")
        elif literal == "b":
            print("Hola Axell")
        else:
            print("Literal ingresado no valido")
        
    elif opcion== "2":
        print("Obviamente Piogram, sin dudarlo c:")
    elif opcion =="3":
        print("Nos vemos luego")
    else:
        print("Opción ingresada no valida")
        

#Variante 2
menu="""1.- Saludar
2.- El mejor canal de youtube
3.- Salir
"""
subMenu="""a) Saludar a Piogram
b) Saludar a Axell
"""
opcion=""
while opcion != "3" : #not opcion == "3"
    print(menu)
    opcion= input("Ingrese una opción: ")
    if opcion == "1":
        print(subMenu)
        literal = input("Ingrese una literal: ")
        while literal != "a" and  literal!="b":
            print("Literal ingresado no valido")
            literal = input("Ingrese una literal: ")
        if literal =="a":
            print("Hola Piogram")
        elif literal == "b":
            print("Hola Axell")   
    elif opcion== "2":
        print("Obviamente Piogram, sin dudarlo c:")
    elif opcion =="3":
        print("Nos vemos luego")
    else:
        print("Opción ingresada no valida")
    