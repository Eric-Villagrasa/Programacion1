positivos, negativos = 0, 0
for _ in range(6):
    numero = int(input("Introduce un número: "))
    if numero > 0:
        positivos += numero
    elif numero < 0:
        negativos += numero
        
print("Suma de números positivos: ",positivos)
print("Suma de números negativos: ",negativos)
