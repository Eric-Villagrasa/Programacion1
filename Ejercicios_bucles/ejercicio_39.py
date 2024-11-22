#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.

cantidad = int(input("Introduce la cantidad de números que deseas introducir: "))
positivos, negativos, ceros = 0, 0, 0
for _ in range(cantidad):
    numero = int(input("Introduce un número: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1
print(f"La cantidad de números positivos es: {positivos}")
print(f"La cantidad de números negativos es: {negativos}")
print(f"La cantidad de números ceros es: {ceros}")