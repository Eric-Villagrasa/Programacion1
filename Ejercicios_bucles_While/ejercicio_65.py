#65

pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
total = 0
mayor=0
menor=1000000000


while True:
    var = int(input("Introduce un número: "))


    if var == -99:
        break
    else:

        if var % 2 == 0:
            pares += 1
        if not var % 2 == 0:
            impares += 1
        if var > 0:
            positivos += 1
        if var < 0:
            negativos += 1
        if var == 0:
            ceros += 1
        
        total += var

        if var < menor:
            menor = var
        if var > mayor:
            mayor = var


print("Pares: ", pares)
print("Impares: ", impares)
print("Positivos: ", positivos)
print("Negativos: ", negativos)
print("Ceros: ", ceros)
print("Total: ", total)
print("El menor número: ", menor)
print("EL mayor número: ", mayor)
