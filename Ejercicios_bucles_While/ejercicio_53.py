#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While

suma=0
repeticiones=0

var="s"
while var=="s":
    num1=int(input("Introduzca un número: "))
    num2=int(input("Introduzca otro número: "))
    print("El resultado de la suma es: ",num1 + num2)
    suma+=num1
    suma+=num2
    repeticiones+=1
    var=input("Deseas repetir la operación s/n: ")

print("Programa finalizado")
print(f"La suma total es: {suma} y el número de repeticiones es: {repeticiones}")