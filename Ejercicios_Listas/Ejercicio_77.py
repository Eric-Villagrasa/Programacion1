#77

lista = ["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]

numeros = []
letras = []

for palabra in lista:
    if palabra.isdigit():
        numeros.append(palabra)

    if palabra.isalpha():
        letras.append(palabra)

var=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))

for palabra in letras:
    if palabra.isupper():
        letras.remove(palabra)

if var==1:

    print("Números: ", sorted(numeros))
    print("Letras: ", sorted(letras))

if var==2:

    numeros.sort(reverse=True)
    letras.sort(reverse=True)

    print("Números (descendente): ", numeros)
    print("Letras (descendente): ", letras)