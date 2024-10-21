#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales

var1=int(input("Introduce el primer número: "))
var2=int(input("Introduce el segundo número: "))

if var1>var2:
    print("El número",var1,"es mayor que el número",var2)
if var1<var2:
    print("El número",var2,"es mayor que el número",var1)
if var1==var2:
    print("El número",var1,"y el número",var2,"son iguales")