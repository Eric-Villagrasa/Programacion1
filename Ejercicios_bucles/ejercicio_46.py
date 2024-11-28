#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.

palabra = input("Introduce una palabra: ").lower()
vocales = "".join([c for c in palabra if c in "aeiou"])
consonantes = "".join([c for c in palabra if c not in "aeiou" and c.isalpha()])
print(f"Las vocales de la palabra son: {vocales}")
print(f"Las consonantes de la palabra son: {consonantes}")
