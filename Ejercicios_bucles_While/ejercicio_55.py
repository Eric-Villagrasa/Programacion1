#55

suma=0
repeticiones=0


while True :
    num1=int(input("Introduzca un número: "))
    num2=int(input("Introduzca otro número: "))
    print("El resultado de la suma es: ",num1 + num2)
    suma+=num1
    suma+=num2
    repeticiones+=1
    print(suma)
    
    if suma > 50 or suma %2==0:
        break
   
print(f"La suma total es: {suma} y el número de repeticiones es: {repeticiones}")
print("Programa finalizado")