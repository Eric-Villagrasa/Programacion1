#56

total = 0
pedidos = 0
var = "s"

print("MENÚ")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")

print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")

print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")


while var == "s":

    pedidos+=1

    bocadillo=int(input("Introduzca el bocadillo que quiera (1,2,3): "))
    acompañamiento=int(input("Introduzca el acompañamiento que quiera (1,2,3): "))
    bebida=int(input("Introduzca la bebida que quiera (1,2,3): "))

    if bocadillo == 1:
        total += 9
    if bocadillo == 2:
        total += 4.5
    if bocadillo == 3:
        total += 2.5

    if acompañamiento == 1:
        total += 1.5
    if acompañamiento == 2:
        total += 1.75
    if acompañamiento == 3:
        total += 2

    if bebida == 1:
        total += 2 
    if bebida == 2:
        total += 1.5
    if bebida == 3:
        total += 1

    var=input("¿Desea hacer otro pedido? (s/n)?: ")


print("RESUMEN")
print("Número de pedidos: ", pedidos)
print("Total a pagar", total)

total_IVA=total + total*0.10
print("Total con IVA", total_IVA)

if 20 < total < 30:
    total_descuento = total_IVA - (total_IVA * 0.05)
    print("Total con descuento del 5%: ", round(total_descuento,2))

if total > 30:
    total_descuento = total_IVA - (total_IVA * 0.15)
    print("Total con descuento del 15%: ", round(total_descuento,2))