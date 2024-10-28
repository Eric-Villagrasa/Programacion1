#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

var1="A quién madruga Dios ayuda."
print(var1)
var2=input("Introduce una palabra para buscar en la frase: ")

var3=var1.find(var2)
if var3 != -1:
    print(f"La palabra '{var2}' se encuentra en el índice {var3}.")
else:
    print(f"La palabra '{var2}' no se encuentra en la frase.")
