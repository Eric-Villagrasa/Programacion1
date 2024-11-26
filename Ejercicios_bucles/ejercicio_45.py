#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes: 

palabra = input("Introduce una palabra: ").lower()
vocales = "".join([X for X in palabra if X in "aeiou"])
consonantes = "".join([X for X in palabra if X not in "aeiou" and X.isalpha()])
print(f"Las vocales de la palabra {palabra} son: {vocales}")
print(f"Las consonantes de la palabra {palabra} son: {consonantes}")
