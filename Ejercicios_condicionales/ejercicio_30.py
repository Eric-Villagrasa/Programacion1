#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif.

var1=input("Introduce una frase: ")

if len(var1)==11:
    print("La frase tiene 11 caracteres.")
elif len(var1)<11:
    print("La frase tiene menos de 11 caracteres.")
elif len(var1)>11:
    print("La frase tiene más de 11 caracteres.")