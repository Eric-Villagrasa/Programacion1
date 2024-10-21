#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

var1=float(input("Introduce tu nota: "))

if var1<0 or var1>10:
    print("La nota que has introducido no está entre 0 y 10")
else:
    if var1<5:
        print("Tu nota es un",var1,", has sacado un insuficiente")
    if var1>=5  and var1<6.5:
        print("Tu nota es un",var1,", has sacado un satisfactorio") 
    if var1>=6.5 and var1<8.5:
         print("Tu nota es un",var1,", has sacado un notable")
    if var1>=8.5 and var1<=10:
         print("Tu nota es un",var1,", has sacado un excelente")