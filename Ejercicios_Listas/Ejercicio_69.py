#69

Lista = []

var=int(input("¿Cuantos números quiere introducir?: "))

for _ in range(var):
    numero = int(input("Introduce un número: "))
    Lista.append(numero)

print(Lista)