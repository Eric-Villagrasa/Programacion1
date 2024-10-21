#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.

import math

var1=float(input("Introduce el diametro del círculo: "))
var2=var1//2

#Área: 
var3=math.pi*(var2**2)
#Perimetro
var4=2*math.pi*var2

print("El área del circulo es: ",round(var3,1))
print("El perímetro del circulo es: ",round(var4,1))