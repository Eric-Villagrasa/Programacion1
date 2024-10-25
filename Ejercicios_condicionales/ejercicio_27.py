#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un n√∫mero, aparezca un aviso por pantalla.

var1=input("Introduce una letra: ")

if var1.isalpha():
    if var1.isupper():
        print("La letra es mayúscula")
    else:
        print("La letra es minúscula")
else:
    if var1.isnumeric():
        print("La entrada es un número")
    else:
        print("La entrada no es ni una letra ni un número")