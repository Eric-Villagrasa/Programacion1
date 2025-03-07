#83

import random

lista=["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
puntuacion=[]

palabra=random.choice(lista)

print(lista)

puntos=8

while True:
    

    var=input("Introduce la palabra secreta: ")

    if var == palabra:
        print("Acertaste")
        puntuacion.append(puntos)
        
        var=input("¿Quiere seguir?(s/n): ")
        if var == "n":
            break
        if var=="s":
            puntos=8


    else:
        print("Sigue jugando")
        if puntos>0:
            puntos-=1


print("Puntuación: ",puntuacion)

print("Tu puntuación ha sido de: ", sum(puntuacion))

media=sum(puntuacion)/len(puntuacion)
print("La media de las partidas realizadas es: ", media)

if sum(puntuacion)>=media:
    print("Tienes buena suerte")
else:
    print("No se dedique a los juegos de azar")