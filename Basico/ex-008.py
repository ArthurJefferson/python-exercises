#Qual Maior

x = int(input("Valor1: "))
y = int(input("Valor2: "))
z = int(input("Valor3: "))

r = True

while r == True:
    try:
        if x > y and x > z:
            print(x, "é o maior")
        elif y > x and y > z:
            print(y, "é o maior")
        elif z > x and z > y:
            print(z, "é o maior")
        r = str(input("Quer Continuar? (s/n):"))
        try:
            if r == 's':
                r = True
            else:
                r = False
        except ValueError:
            print("Opção Inválida")
    except ValueError:
       print("Numeros Inválidos")
       