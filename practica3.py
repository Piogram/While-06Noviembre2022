num = input("Ingrese un número: ") 
while not num.isdigit():
    print("Valor no válido")
    num = input("Ingrese un número: ")

resultado = int(num)
print("Fin")

