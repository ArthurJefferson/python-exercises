import random
import os

x = random.randint(1, 100)

y = 101

while x != y:
    try:
        y = int(input("Numero: "))
        os.system('cls')

        if y > x:
            print("Diminua")
            print(y)
        elif y < x:
            print("Aumente")
            print(y)
    except ValueError:
        print("Numero Inválido")

if x == y:
    print("PARABÉNS!!")