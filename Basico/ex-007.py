#Calculadora
import os

def calcular(op, x ,y):
    if op == "x":
        return x * y
    elif op == "+":
        return x + y
    elif op == "-":
        return x - y
    else:
       return "ERRO! Operador invalido"
r = True
   
while r == True:
    try:
        op = str(input("Qual operação? (x/+/-)? "))
        if op != "x" and op != "+" and op != "-":
            print("ERRO! Operador invalido")
            break
        x = int(input("valor1: "))
        y = int(input("valor2: "))
        resultado = calcular(op, x, y)
    
        print(resultado)
        
        print("Quer continuar (s/n)? :")
        r = input()
        os.system('cls')
        if r == "s":
            r = True
        else:
            r = False
            
    except ValueError:
        print("ERRO")