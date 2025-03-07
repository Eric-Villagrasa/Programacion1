#66

import random
import time

lanzamientos = 0

resultados = [0] * 6

tiempo_inicio = time.time()

while time.time() - tiempo_inicio < 3:
    resultado = random.randint(1, 6)
    resultados[resultado - 1] += 1
    lanzamientos += 1

tiempo_fin = time.time()

tiempo_total = tiempo_fin - tiempo_inicio

print("Resumen")
print(f"Tiempo: {tiempo_total}")
for i in range(6):
    print(f"{i+1}: {resultados[i]}")
