#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.

secreta = input("Introduce la palabra secreta: ")
intentos = len(secreta)
for _ in range(intentos):
    letra = input("Introduce una letra: ")
    if letra in secreta:
        posiciones = [i + 1 for i, c in enumerate(secreta) if c == letra]
        for pos in posiciones:
            print(f"La letra se encuentra en la posición {pos}")
    else:
        print("La letra no existe")
