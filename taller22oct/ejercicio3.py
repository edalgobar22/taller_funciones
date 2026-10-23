"""
Caso. Cree las funciones necesarias para tolerancia de una medición. Debe reutilizar una función de
valor absoluto que recibe un real y devuelve su distancia al cero. Los extremos de tolerancia se aceptan.
La función de aceptación utiliza el retorno de valor absoluto. El escenario consulta dos mediciones por
separado. Contratos en orden de parámetros: Valor absoluto: recibe real finito y devuelve real no
negativo. Aceptación: recibe medición y objetivo reales, tolerancia real no negativa y devuelve lógico.
"""

def valor_absoluto (numero):
    if numero < 0:
        resultado = numero * -1
    else:
        resultado = numero = numero

    return resultado

def aceptacion (medicion, objetivo, tolerancia):
    error = valor_absoluto (medicion - objetivo)

    if error <= tolerancia:
        resultado = True

    else:
        resultado = False
    return resultado

objetivo = float(input("objetivo?: "))
tolerancia = float(input("Tolerancia?: "))

medida1 = float(input("Medida 1?: "))
medida2 = float(input("Medida 2?: "))    

resultado1 = aceptacion(medida1, objetivo, tolerancia)
resultado2 = aceptacion(medida2, objetivo, tolerancia)

print("aceptables:\nMedida 1: ", resultado1, "\nMedida 2: ", resultado2 )