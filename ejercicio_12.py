#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.

var1=float(input("Introduce la medida del lado: "))
var2=float(input("Introduce la medida de la base menor: "))
var3=float(input("Introduce la medida de la base mayor: "))
var4=float(input("Introduce la medida de la altura: "))

print("El perímetro es: ",var3+var2+2*var1)
print("El area es: ", (var2+var3)*var4//2)