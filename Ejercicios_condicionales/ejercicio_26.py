#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

var1=input("Introduce una letra: ")

if var1.isalpha():
    if var1.isupper():
        print("La letra es mayúscula")
    else:
        print("La letra es minúscula")
else:
    print("La entrada no es una letra")