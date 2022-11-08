productos=["Americano","Capuchino","Expresso","Mocachino"]

texto = input("Ingrese producto de cafetería: ")
while texto.capitalize() not in productos:
    texto = input("Ingrese producto de cafetería: ")

print("Producto Ingresado: ",texto)
    
