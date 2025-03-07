#63

import random

uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

for _ in range(100):
    numero = random.randint(1,6)
    if numero == 1:
        uno += 1
    if numero == 2:
        dos += 1
    if numero == 3:
        tres += 1
    if numero == 4:
        cuatro += 1
    if numero == 5:
        cinco += 1
    if numero == 6:
        seis += 1


print("Uno: ", uno)
print("Dos: ", dos)
print("Tres: ", tres)
print("Cuatro: ", cuatro)
print("Cinco: ", cinco)
print("Seis: ", seis)