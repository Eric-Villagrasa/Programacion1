#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10

var1=int(input("Introduce el primer número: "))
var2=int(input("Introduce el segundo número: "))

if var1>10 or var2>10 or var1<1 or var2<1:
    print("Uno o los dos números están fuera de los límites establecidos")
else:
    if var1>var2:
        print("El número",var1,"es mayor que el número",var2)
    if var1<var2:
        print("El número",var2,"es mayor que el número",var1)
    if var1==var2:
        print("El número",var1,"y el número",var2,"son iguales")
