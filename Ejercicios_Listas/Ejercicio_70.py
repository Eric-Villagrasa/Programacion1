#70

Lista = []

var = int(input("¿Cuantas palabras quiere introducir?: "))

for _ in range(var):
    numero = input("Introduce una palabra: ")
    Lista.append(numero)

print(Lista)
Lista.reverse()
print(Lista)