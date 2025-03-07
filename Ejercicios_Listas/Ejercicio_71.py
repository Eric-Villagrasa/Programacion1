#71

var="s"
lista=[]

while var == "s":
    letra=input("Introduce una letra: ")
    if not letra.isnumeric():
        if letra not in lista:
            lista.append(letra)
        var = input("¿Quiere repetir la operación?(s/n): ")

print(lista)