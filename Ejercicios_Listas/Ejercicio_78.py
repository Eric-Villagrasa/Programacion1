#78

lista = ['a', 'b', 'D', 'x', 'r', 'X', 3, 'h', 'w', 2, 'i']

var = "s"

print(lista)

while var.lower() == "s": 

    palabra = input("¿Qué número quieres borrar?: ")

    if palabra.isdigit():
        numero = int(palabra)

        if numero in lista:
            lista.remove(numero)
            print(f"Elemento '{numero}' borrado.")
        else:
            print(f"El número {numero} no está en la lista.")
    else:
        print("Introduce un número válido.")

    print("Lista actual:", lista)
    
    var = input("¿Quiere seguir(s/n)?: ").lower() 
