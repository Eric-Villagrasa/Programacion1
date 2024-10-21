#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

var1=float(input("Introduce tu nota: "))

if var1<0 or var1>10:
    print("La nota que has introducido no está entre 0 y 10")
else:
    if var1<5:
        print("Has sacado un",var1,"y has suspendido")
    if var1>=5:
        print("Has sacado un",var1,"y has aprobado")

