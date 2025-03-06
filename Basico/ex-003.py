#Impar e par

x = int(input())

resultado = x % 2

if resultado == 0:
    print(f"{x} é par")
else:
    print(f"{x} é impar")