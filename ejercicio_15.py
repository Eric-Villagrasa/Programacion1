#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

import math
var1=float(input("Introduce el radio: "))
var2=float(input("Introduce el altura: "))

#Área
var3=2*math.pi*var1*(var2+var1)
#Volumen
var4=math.pi*var1**2*var2

print("El área es: ",round(var3,2))
print("El volumen es: ",round(var4,2))