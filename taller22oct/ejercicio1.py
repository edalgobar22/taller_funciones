"""
Caso. Cree una función para área de un triángulo por base y altura. La altura es perpendicular a la base.
Use dos llamadas y muestre las dos áreas y su suma, calculada con los retornos. Contrato: Área de un
triángulo por base y altura: recibe base y altura, reales positivos expresados en centímetros y devuelve
el área real en centímetros cuadrados.
"""
def area(base, altura):
    resultado = base * altura / 2
    return resultado

while True:
    base1 = int(input("Ingrese la base 1: "))
    altura1 = int(input("Ingrese la altura 1: "))
    base2 = int(input("Ingrese la base 2: "))
    altura2 = int(input("Ingrese la altura 2: "))
    if base1 > 0 and altura1 > 0 and base2 > 0 and altura2 > 0:
        break
    else:
        print("Las medidas tienen que ser positivas")
        input("Presione Enter para continuar ...")
        

    
    
areas1 = area(base1, altura1)
areas2 = area(base2, altura2)
sumaareas = areas2 + areas1
print("Areas: ", areas1, "y ", areas2,"; suma total: ", sumaareas )
    


        



