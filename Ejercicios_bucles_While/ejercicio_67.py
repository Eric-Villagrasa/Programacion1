#67

import re

def es_password_valido(password):
    if len(password) < 6 or len(password) > 8:
        return False

    numeros_1a5 = re.findall(r"[1-5]", password)
    numeros_mayores_o_iguales_a_6 = re.findall(r"[6-9]", password)
    letras_minusculas = re.findall(r"[a-z]", password)
    letras_mayusculas = re.findall(r"[A-Z]", password)
    simbolos = re.findall(r"[*_@&/#]", password)

    if (len(numeros_1a5) >= 2 and
        len(numeros_mayores_o_iguales_a_6) >= 1 and
        len(letras_minusculas) >= 2 and
        len(letras_mayusculas) >= 1 and
        len(simbolos) >= 2):
        return True
    return False

password = input("Introduce la contraseña: ")

if es_password_valido(password):
    print("password correcto")
else:
    print("password incorrecto")
