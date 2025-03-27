print("***GASOLINERA***")
print("1. Sin plomo 95  1,765€")
print("2. Sin plomo 98  1,913€")
print("Gasóleo A  1,746€")
print("Gasóleo A+  1,839€")

var1=int(input("Escoja el tipo de combustible: "))
var2=float(input("Intrduzca el número de litros a repostar: "))

if var1==1:
    print(var2*1.765,"€")
elif var1==2:
    print(var2*1,913,"€")
elif var1==3:
    print(var2*1,746,"€")
elif var1==4:
    print(var2*1,839,"€")
else:
    print("No existe el tipo de gasolina introducido")