#72

a=["à", "á", "a"]
e=["è", "é", "e"]
i=["ì", "í", "i"]
o=["ò","ó", "o"]
u=["ù", "ú", "u"]


var="s"
lista=[]

while var == "s":
    letra=input("Introduce una letra: ")
    if not letra.isnumeric():

        if letra in a:
                letra = "a"
        if letra in e:
                letra = "e"
        if letra in i:
                letra = "i"
        if letra in o:
                letra = "o"
        if letra in u:
                letra = "u"

        if letra not in lista:

            lista.append(letra)

        var = input("¿Quiere repetir la operación?(s/n): ")

print(lista)