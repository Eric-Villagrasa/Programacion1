#59

import random

numero = random.randint(1,1000)
intentos = 0

while True:
    var=int(input("Introduce un número entre 1 y 1000: "))
    intentos += 1

    if var < numero:
        print("El número que ha introducido es demasiadao bajo")

    if var > numero:
        print("El número que ha introducido es demasiado alto")

    if var == numero:
        print(f"El número es correcto, ha realizado {intentos} intentos.")
        break