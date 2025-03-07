#82

import random

lista=["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]

palabra=random.choice(lista)

while True:
    var=input("Introduce la palabra secreta: ")

    if var == palabra:
        print("Acertaste")
        break
    else:
        print("Sigue jugando")