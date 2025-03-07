#85

ingles=[]
castellano=[]
catalan=[]

var="s"

while var=="s":

    nombre=input("Introduce estudiante: ")

    nota1=int(input("Nota de inglés: "))
    nota2=int(input("Nota de castellano: "))
    nota3=int(input("Nota de catalán: "))

    ingles.append(nota1)
    castellano.append(nota2)
    catalan.append(nota3)

    var=input("¿Quiere seguir?(s/n): ")

    if var=="n":
        break
    

print("Ingles: ",ingles)
print("Castellano: ",castellano)
print("Catalán: ",catalan)

print("\nMedia de inglés: ",sum(ingles)/len(ingles))
print("Media de castellano: ",sum(castellano)/len(castellano))
print("Media de catalán: ",sum(catalan)/len(catalan))

ingles.sort
castellano.sort
catalan.sort
mitad=int(len(ingles)//2)

print("\nMediana de inglés: ",ingles[mitad])
print("Mediana de castellano: ",castellano[mitad])
print("Mediana de catalán: ",catalan[mitad])