#80

def es_decimal(numero):
    num_lista = list(numero) 
    return ',' in num_lista 

numero = input("Ingresa un número: ")

if es_decimal(numero):
    print("Es decimal.")
else:
    print("Es entero.")