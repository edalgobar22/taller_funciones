"""
Caso. Cree una función para pago semanal con horas extra. Es un modelo ficticio: las primeras 40 horas
se pagan a la tarifa ordinaria; solo las horas que exceden 40 se pagan a 1,5 veces esa tarifa. Llame para
dos personas y sume los retornos, sin redondearlos antes de sumar. Contrato: Pago semanal con horas
extra: recibe horas semanales reales no negativas y tarifa real no negativa en pesos por hora y devuelve
el pago real semanal en pesos.
"""


def pago_semanal(horas, tarifa):
    if horas <= 40:
        pago = horas * tarifa
    else:
        pago = 40 * tarifa + (horas - 40) * tarifa * 1.5

    return pago


horas1 = float(input("Ingrese las horas trabajadas de la persona 1: "))
tarifa1 = float(input("Ingrese la tarifa por hora de la persona 1: "))

horas2 = float(input("Ingrese las horas trabajadas de la persona 2: "))
tarifa2 = float(input("Ingrese la tarifa por hora de la persona 2: "))

pago1 = pago_semanal(horas1, tarifa1)
pago2 = pago_semanal(horas2, tarifa2)

total = pago1 + pago2

print("Pago de la persona 1:", pago1)
print("Pago de la persona 2:", pago2)
print("Pago total:", total)
