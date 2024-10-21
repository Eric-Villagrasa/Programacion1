#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.

print("La entrada cuesta 12 euros")
print("El descuento para adultos es del 10%")
print("El descuento para menores es del 50%")

var1=float(input("Introduce cuantos adultos asistirán al cine: "))
var2=float(input("Introduce cuantos menores asistirán al cine: "))

descuento_adultos=10/100
descuento_menores=50/100

precio_adulto_descuento=12*(1 - descuento_adultos)
precio_menor_descuento=12*(1 - descuento_menores)

var3=round(var1*precio_adulto_descuento,1)
var4=round(var2*precio_menor_descuento,1)
var5=float(var3+var4)

print("El precio total del cine para",var1,"adulto/s es: ",var3," euros")
print("El precio total del cine para",var2,"menor/es es: ",var4," euros")
print("El precio total a pagar es de: ",var5," euros")