#61

numero = int(input("Introduzca un número: "))
var = 1

while var <= 10:
    if numero*var > 40:
        print("Programa finalizado")
        break

    print(numero*var)
    var +=1