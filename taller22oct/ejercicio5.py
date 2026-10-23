
def subtotal_descontado(base, descuento):
    subtotal = base * (1 - descuento / 100)
    return subtotal


def total_impuesto(subtotal, impuesto):
    total = subtotal * (1 + impuesto / 100)
    return total


base = float(input("Ingrese el precio base: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
impuesto = float(input("Ingrese el porcentaje de impuesto: "))

subtotal = subtotal_descontado(base, descuento)
total = total_impuesto(subtotal, impuesto)

print("Subtotal con descuento:", subtotal)
print("Total con impuesto:", total)
