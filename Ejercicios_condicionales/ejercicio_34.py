#34. Corrige los 4 errores o añade el código que necesites para que el siguiente programa se ejecute correctamente

var_numero=67341
var_suma=0 


var_longitud=len(str(var_numero))
var_suma=sum(int(digito) for digito in str(var_numero))


if var_suma%2==0: 
    print (f"el valor de {var_suma} es impar")
else:
    print(f"El valor de {var_suma} es impar")