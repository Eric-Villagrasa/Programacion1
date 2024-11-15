#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.

var1=float(input("Introduce tu peso en Kg: "))
var2=float(input("Introduce tu altura en metros: "))

var3=round(var1/var2**2,2)

if var3==25 or var3>25:
    print("Si pesas",var1,"kilos y mides", var2,"metros, tu IMC es: ",var3,"Hay sobrepeso")
else:
    print("Si pesas",var1,"kilos y mides", var2,"metros, tu IMC es: ",var3,"No hay sobrepeso")