#62

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

pares = []
impares = []

for numero in range(numero1, numero2 + 1):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Los números pares son:", "-".join(map(str, pares)))
print("Los números impares son:", "-".join(map(str, impares)))
