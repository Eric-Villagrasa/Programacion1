#40. Crea un programa que cuente todos los números pares hasta el número 50

pares = len([X for X in range(1, 51) if X % 2 == 0])
impares = 50 - pares
print(f"El total de pares es: {pares}")
print(f"El total de impares es: {impares}")
