#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.

var1=float(input("introduce el dividendo: "))
var2=float(input("introduce el divisor: "))
10
2
cociente=var1//var2
resto=var1%var2

print("el cociente es: ",var1//var2)
print("el resto es: ",var1%var2)

if var1%2==0:
    print("el dividendo es par")
else:
    print("el dividendo es impar")
