#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla.

var1=input("Introduce una letra: ")

if var1.isalpha():
    if var1.isupper():
        print("La letra es may�scula")
    else:
        print("La letra es min�scula")
else:
    if var1.isnumeric():
        print("La entrada es un n�mero")
    else:
        print("La entrada no es ni una letra ni un n�mero")