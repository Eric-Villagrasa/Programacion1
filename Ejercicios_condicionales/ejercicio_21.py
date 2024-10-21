#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo.

import math
var1=int(input("Introduce la variable a: "))
var2=int(input("Introduce la variable b: "))
var3=int(input("Introduce la variable c: "))

discriminante=var2**2 - 4*var1*var3

if discriminante<0:
    print("La raíz no puede ser un valor negativo")
else:
    print("El valor de x1 es:",(float(-var2 + math.sqrt(discriminante))/(2*var1)))
    print("El valor de x2 es:",(float(-var2 - math.sqrt(discriminante))/(2*var1)))
