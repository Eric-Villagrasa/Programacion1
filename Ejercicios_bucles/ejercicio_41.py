#41. Imprime el siguiente patrón utilizando for:

for X in range(5, 0, -1):
    print("".join(str(j) for j in range(X, 0, -1)))