def esDecimal( num ):
    while "." not in num or not num.replace(".","").isdigit() or num.count(".")!=1 :
        print("Valor no válido")
        num = input("Ingrese número decimal: ")
    return float(num)


num = input("Ingrese número decimal: ")
numFloat = esDecimal(num)
print('numFloat: ', numFloat)








    