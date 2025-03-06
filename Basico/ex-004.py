#Tabuada
import os

print("Digite um numero para ver a tabuada: ")
x = int(input())
os.system('cls')

for i in range(1, 11):
    resultado = x * i
    print(f"{x} x {i} = {resultado}")