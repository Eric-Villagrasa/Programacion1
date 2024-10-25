#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

var1=input("Introduce una letra: ")

if var1.isalpha():
    if var1.isupper():
        print("La letra es mayúscula")
    elif var1.islower():
        print("La letra es minúscula")
    elif var1.isnumeric():
        print("La entrada es un número")
    else:
        print("La entrada no es ni una letra ni un número")
