#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas

var1 = "A quién madruga Dios ayuda."
print(var1)
var2 = input("Introduce una palabra para buscar en la frase: ")

var1_lower=var1.lower()
var2_lower=var2.lower()

var3=var1_lower.find(var2_lower)

if var3 != -1:
    print(f"La palabra '{var2}' se encuentra en el índice {var3}.")
else:
    print(f"La palabra '{var2}' no se encuentra en la frase.")
