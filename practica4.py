texto = input("Ingrese una palabra: ")
while not texto.isalpha():
    print("Valor no válido")
    texto = input("Ingrese una palabra: ")
    