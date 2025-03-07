#51. A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el número de veces que desea que repita la frase Buenos días. Con While

contador=0
var=int(input("Introduzca un número: "))

while contador < var:
    print("Buenos días")
    contador+=1