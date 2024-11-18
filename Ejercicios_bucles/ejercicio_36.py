#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

n = int(input("Introduce el valor n: "))
suma = sum(range(1, 1 + n))
print(f"La suma total de números naturales es: {suma}")