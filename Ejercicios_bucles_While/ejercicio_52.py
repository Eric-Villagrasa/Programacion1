#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While

var="s"
while var=="s":
    num1=int(input("Introduzca un número: "))
    num2=int(input("Introduzca otro número: "))
    print("El resultado de la suma es: ",num1 + num2)
    var=input("Deseas repetir la operación s/n: ")

print("Programa finalizado")