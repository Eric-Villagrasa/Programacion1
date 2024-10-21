#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

var1 = float(input("Introduce tu nota: "))

if var1 < 5 and var1>=0:
     print("Tu nota es un", var1, ", has sacado un insuficiente")
elif var1 >= 5 and var1 < 6.5:
      print("Tu nota es un", var1, ", has sacado un satisfactorio")
elif var1 >= 6.5 and var1 < 8.5:
        print("Tu nota es un", var1, ", has sacado un notable")
elif var1>=8.5 and var1<=10:
        print("Tu nota es un", var1, ", has sacado un excelente")
else:
       print("La nota que has introducido no está entre 0 y 10") 