#58

import random

intentos=3
numero = random.randint(1,5)

while intentos > 0:
    var = int(input("introduce un número: "))

    intentos -=1

    if var != numero:
        print("Número incorrecto")

    if intentos == 0:
        print("Se le han acabado los intentos")
        break

    if var == numero:
        print("Número acertado")
        break