"""
Caso. Cree una función para precio unitario comparable. Dos paquetes pueden tener tamaños distintos;
no compare solo sus precios totales. Llame para dos paquetes y use los retornos para indicar el más
económico por gramo; si coinciden indique igualdad. Contrato: Precio unitario comparable: recibe
precio total real no negativo en pesos y cantidad real positiva en gramos y devuelve el precio real de un
gramo en pesos.
"""

def preciopg(valor, peso):
    resultado = valor/peso
    return resultado

"""
    if valor1 == valor2:
        print("valor por gram igual")
"""


while True:
    preciopaq1 = int(input("ingrese el valor del paquete 1: "))
    pesopaq1 = int(input("ingrese el peso(gr) del paquete 2: "))
    preciopaq2 = int(input("ingrese el valor del paquete 2: "))
    pesopaq2 = int(input("ingrese el peso(gr) del paquete 2: "))
    if preciopaq1 >= 0 and pesopaq1 > 0 and preciopaq2 >= 0 and pesopaq2 > 0:
        break
    else:
        print("El precio debe ser positivo o 0 y el peso debe ser positivo")
        input("Presione Enter para continuar...")

ppg1 = preciopg(preciopaq1, pesopaq1)
ppg2 = preciopg(preciopaq2, pesopaq2)

if ppg1 < ppg2:
    print("precios por gramo: ", ppg1, "y ", ppg2, "; conviene paquete 1")

elif ppg1 > ppg2:
    print("precios por gramo: ", ppg1, "y ", ppg2, "; conviene paquete 2")
else:
    print("precios por gramo: ", ppg1, "y ", ppg2, "; precio por gramo igual")



