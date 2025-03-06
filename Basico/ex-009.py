import os
r = True

while r == True:
    x = input("Escreva uma palavra:").replace(" ", "").lower()
    print(x)
    y = x[::-1]
    if y == x:
       print("É um Palíndromo")
       print(f"Original = {x}")
       print(f"Ao Contrário = {y}")
    else:
        print("Não é um Palíndromo")
        print(f"Original = {x}")
        print(f"Ao Contrário = {y}")
     
    r = str(input("Quer Continuar? (s/any):"))
    os.system('cls')
    if r == 's':
        r = True
    else:
        r = False

      