#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

var1=input("Introduce un carácter: ")

if var1.isalpha():
    if var1.isupper():
        print("La letra es mayúscula.")
    if var1.islower():
        print("La letra es minúscula.")
elif var1.isdigit():
    print("El valor introducido es un número.")
else:
    print("El valor introducido es un símbolo.")
