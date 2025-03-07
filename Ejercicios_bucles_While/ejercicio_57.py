#57

import random

numero = random.randint(1,5)
var = 6

while var != numero:
    var =int(input("Introduzca un número: "))

    if var != numero:
        print("Número incorrecto")

print("Número acertado")