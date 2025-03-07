#74

lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
repetidas=[]
no_repetidas=[]

for palabra in lista1:
    if palabra in lista2:
        repetidas.append(palabra)

    if palabra not in lista2:
        no_repetidas.append(palabra)

for palabra in lista2:
    if palabra not in lista1:
        no_repetidas.append(palabra)


print("Repetidas: ",repetidas)
print("No repetidas: ",no_repetidas)