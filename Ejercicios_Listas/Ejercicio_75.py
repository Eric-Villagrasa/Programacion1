#75

lista = ["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]

valores=[]
numeros=[]
letras=[]
mayusculas=[]
suma=[]

valores.append(len(lista))

for palabra in lista:
    if palabra.isnumeric():
        numeros.append(palabra)

    if palabra.isalpha():
        letras.append(palabra)

    if palabra.isupper():
        mayusculas.append(palabra)

    if palabra.isdigit():
        suma.append(int(palabra))



print("Valores: ",valores[0])
print("Números: ",len(numeros))
print("Letras: ",len(letras))
print("Mayúsculas: ",len(mayusculas))
print("Suma: ",sum(suma))