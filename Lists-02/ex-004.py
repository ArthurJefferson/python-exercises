def soma(x, y):
    return x + y

def menos(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
resp = input("Digite a operação (+ ou - ou x ou /): ")

if resp == "+":
    print(soma(x, y))
elif resp == "x":
    print(mult(x, y))
elif resp == "/":
    print(div(x, y))
else:
    print(menos(x, y))